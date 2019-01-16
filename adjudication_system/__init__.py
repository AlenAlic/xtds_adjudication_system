from flask import Flask, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap
from wtforms import PasswordField
import adjudication_system.values as values


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('main.index'))
        else:
            if current_user.is_authenticated:
                return self.render(self._template)
            else:
                return redirect(url_for('main.index'))


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
admin = Admin(template_mode='bootstrap3', index_view=MyAdminIndexView())
bootstrap = Bootstrap()


class AdjudicatorSystemView(ModelView):
    column_hide_backrefs = False
    page_size = 1000

    def is_accessible(self):
        if current_user.is_authenticated:
            return True
        return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('main.index'))


class UserView(AdjudicatorSystemView):
    column_exclude_list = ['password_hash', ]
    form_excluded_columns = ['password_hash', ]
    form_extra_fields = {'password2': PasswordField('Password')}

    # noinspection PyPep8Naming
    def on_model_change(self, form, User, is_created):
        if form.password2.data != '':
            User.set_password(form.password2.data)


def create_app():
    # Import for creating WebCie account
    from adjudication_system.models import User, Event, Competition, DancingClass, Discipline, Dance, Round, \
        Heat, Couple, Adjudicator, Mark, CouplePresent, RoundResult, FinalPlacing, DanceActive, CompetitionMode, Dancer

    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    # Init add-ons
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite:'))
    login.init_app(app)
    login.login_view = 'main.index'
    bootstrap.init_app(app)
    admin.init_app(app)
    admin.add_view(UserView(User, db.session))
    admin.add_view(AdjudicatorSystemView(Event, db.session))
    admin.add_view(AdjudicatorSystemView(Competition, db.session))
    admin.add_view(AdjudicatorSystemView(DancingClass, db.session))
    admin.add_view(AdjudicatorSystemView(Discipline, db.session))
    admin.add_view(AdjudicatorSystemView(Dance, db.session))
    admin.add_view(AdjudicatorSystemView(Adjudicator, db.session))
    admin.add_view(AdjudicatorSystemView(Dancer, db.session))
    admin.add_view(AdjudicatorSystemView(Couple, db.session))
    admin.add_view(AdjudicatorSystemView(Round, db.session))
    admin.add_view(AdjudicatorSystemView(DanceActive, db.session))
    admin.add_view(AdjudicatorSystemView(Heat, db.session))
    admin.add_view(AdjudicatorSystemView(Mark, db.session))
    admin.add_view(AdjudicatorSystemView(FinalPlacing, db.session))
    admin.add_view(AdjudicatorSystemView(CouplePresent, db.session))
    admin.add_view(AdjudicatorSystemView(RoundResult, db.session))

    # Shell command for creating first account
    def create_admin(password):
        with app.app_context():
            user = User()
            user.username = 'admin'
            user.set_password(password)
            user.is_active = True
            db.session.add(user)
            db.session.commit()

    @app.shell_context_processor
    def make_shell_context():
        return {'create_admin': create_admin}

    @app.before_request
    def before_request_callback():
        g.data = values
        g.event = Event.query.first()
        g.competitions = Competition.query.all()
        g.competition_mode = CompetitionMode

    # Register blueprints
    from adjudication_system.main import bp as main_bp
    app.register_blueprint(main_bp)

    from adjudication_system.adjudication_system import bp as adjudication_system_bp
    app.register_blueprint(adjudication_system_bp, url_prefix='/adjudication_system')

    from adjudication_system.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/adjudication_system/api')

    return app


from adjudication_system import models