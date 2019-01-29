# xTDS Adjudication System

A standalone version of the adjudication system that is integrated with the xTDS WebPortal.

## Installation (on Ubuntu)
This will assume a fresh installation of Ubuntu 18.04.

Before we start installing the system, start with the following commands to update te system:

    sudo ubuntu-drivers autoinstall
    sudo apt -y update
    sudo apt -y upgrade

### Base dependencies
First, we will need install a few base dependencies:

    sudo apt -y install python3 python3-venv python3-dev mysql-server supervisor nginx git

### Installing the application
Install the application through git:

    # clone the repository
    git clone https://github.com/AlenAlic/xtds_adjudication_system
    cd xtds_adjudication_system

#### Dependencies
Create a virtualenv and activate it. Then install all the package dependencies in the virtualenv:

    python3 -m venv venv
    source venv/bin/activate
    pip install pip --upgrade
    pip install setuptools --upgrade
    pip install -r requirements.txt
    pip install gunicorn

#### Config
Create a file named the config.py file in the instance folder.

The file should contain the following variables:

    ENV = 'production'
    DEBUG = False
    SECRET_KEY = 'random_string'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://xtdsas:<db_password>@localhost:3306/xtdsas'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = False

You can create the SECRET_KEY for the website, and password for the MySQL database using the following command:

    python3 -c "import uuid; print(uuid.uuid4().hex)"

Finally, you need to set the FLASK_APP environment variable in the system:

    export FLASK_APP=run.py
    echo "export FLASK_APP=run.py" >> ~/.profile
The second line sets it so that the command is automatically run when you log in.

### MySQL Database
Enter the MySQL server with the following command:

    sudo mysql

Create a new database called **xtdsas**, along with a user with the same name, that has full access to the database.

    create database xtdsas character set utf8 collate utf8_bin;
    create user 'xtdsas'@'localhost' identified by '<db-password>';
    grant all privileges on xtdsas.* to 'xtdsas'@'localhost';
    flush privileges;
    quit;

Make sure you replace <db-password> with the password that was set in the *config.py* file.

Next, we need to initialize the database structure:

    flask db upgrade

### Set up admin account for website
Before you can log in to the site, you will need to create the admin account (and floor manager account) through the shell:

    flask shell
    create_tournament_office('admin_password', 'floor_manager_password')
    exit()

You can log in with the usernames *admin*, and *floor* as the tournament office manager and floor manager respectively.

### Gunicorn
Gunicorn is a pure Python web server that will be used in stead of the built in Flask server. Though in stead of running gunicorn directly, we'll let it run through the supervisor package. Supervisor will then have it running in the background instead. Should something happen to the server, or if the machine is rebooted, the server will be restarted on its own.

Create a file called *xtdsas.conf* in the folder */etc/supervisor/conf.d/*

    sudo nano /etc/supervisor/conf.d/xtdsas.conf

Copy the data from below into that file and replace *<username>* with the username of the machine account.

    [program:xtdsas]
    command=/home/<username>/xtds_adjudication_system/venv/bin/gunicorn -b localhost:8000 -w 2 run:app
    directory=/home/<username>/xtds_adjudication_system
    user=<username>
    autostart=true
    autorestart=true
    stopasgroup=true
    killasgroup=true

After saving this file, reload the supervisor.

    sudo supervisorctl reload

The gunicorn web server should now be up and running on localhost:8000.

### Nginx
Nginx is used to serve the pages that are generated by Gunicorn to the outside world.

After installation, Nginx already comes with a test site. remove it first:

    sudo rm /etc/nginx/sites-enabled/default

 Create a file called *xtdsas. in the folder */etc/nginx/sites-enabled/*

    sudo nano /etc/nginx/sites-enabled/xtdsas

Copy the data from below into that file and replace *<username>* with the username of the machine account.

    server {
        # listen on port 80 (http)
        listen 80;
        server_name _;

        location / {
            # forward application requests to the gunicorn server
            proxy_pass http://localhost:8000;
            proxy_redirect off;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        location /static {
            # handle static files directly, without forwarding to the application
            alias /home/<username>/xtds_adjudication_system/adjudication_system/static;
            expires 30d;
        }
    }

After saving this file, reload nginx:

    sudo service nginx reload

### Congratulations!

The xTDS Adjudication System should be available on the local network through the local ip address of the machine you're on.

### Allow external access
If you wish to reach the site through the internet, you'll need a firewall and allow outside access to the server.

We'll install ufw (the Uncomplicated Firewall), and configure to allow external traffic on port 80 (http). We'll add port 22 (ssh) so that you do not always need to be physically next to the server.

    sudo apt install -y ufw
    sudo ufw allow http
    sudo ufw allow ssh
    sudo ufw --force enable