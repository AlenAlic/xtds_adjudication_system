# Requests
GET = "GET"
POST = "POST"
PATCH = "PATCH"
PUT = "PUT"
DELETE = "DELETE"


# Responses
OK = "", 200
NO_CONTENT = "", 204
BAD_REQUEST = "", 400
UNAUTHORIZED = "", 401
FORBIDDEN = "", 403
NOT_FOUND = "", 404
PAYLOAD_TOO_LARGE = "", 413
PRECONDITION_REQUIRED = "", 428
SERVER_ERROR = "", 500
SERVER_OFFLINE = "", 503
SERVER_TIMEOUT = "", 504


# Second conversions
SECONDS_QUARTER = 900
SECONDS_DAY = 86400
SECONDS_MONTH = 2592000
SECONDS_YEAR = 31536000


# Security
MINIMAL_PASSWORD_LENGTH = 12


# Date related
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


# ACCESS
AL_TOURNAMENT_OFFICE_MANAGER = 0
AL_FLOOR_MANAGER = 2
AL_ADJUDICATOR = 4
AL_PRESENTER = 10


# Floor mapping
FLOOR_MAP = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}


# DANCE modes
TOURNAMENT = "TOURNAMENT"
XTDS = "xTDS"
ODK = "ODK"
SOND = "SOND"


def dance2(dance):
    return f"{dance} 2"


def tag2(tag):
    return f"{tag}2"


# Dances
SLOW_WALTZ = "Slow Waltz"
TANGO = "Tango"
VIENNESE_WALTZ = "Viennese Waltz"
SLOW_FOXTROT = "Slow Foxtrot"
QUICKSTEP = "Quickstep"
SAMBA = "Samba"
CHA_CHA_CHA = "Cha Cha Cha"
RUMBA = "Rumba"
PASO_DOBLE = "Paso Doble"
JIVE = "Jive"
SALSA = "Salsa"
POLKA = "Polka"
BACHATA = "Bachata"
MERENGUE = "Merengue"
DANCE_TAGS = {
    SLOW_WALTZ: "SW",
    TANGO: "TG",
    VIENNESE_WALTZ: "VW",
    SLOW_FOXTROT: "SF",
    QUICKSTEP: "QS",
    SAMBA: "SB",
    CHA_CHA_CHA: "CC",
    RUMBA: "RB",
    PASO_DOBLE: "PD",
    JIVE: "JV",
    SALSA: "SS",
    BACHATA: "BC",
    MERENGUE: "MG",
    POLKA: "PK",
}


BASIC_STANDARD_DANCES = [SLOW_WALTZ, TANGO, QUICKSTEP]
BASIC_LATIN_DANCES = [CHA_CHA_CHA, RUMBA, JIVE]
STANDARD_DANCES = [SLOW_WALTZ, TANGO, VIENNESE_WALTZ, SLOW_FOXTROT, QUICKSTEP]
LATIN_DANCES = [SAMBA, CHA_CHA_CHA, RUMBA, PASO_DOBLE, JIVE]
BALLROOM_DANCES = STANDARD_DANCES + LATIN_DANCES

BASE_DANCES = [
    {"name": dance, "tag": DANCE_TAGS[dance], "order": idx} for idx, dance in enumerate(BALLROOM_DANCES, 1)
]
SECOND_BASE_DANCES = [
    {"name": dance2(dance), "tag": tag2(DANCE_TAGS[dance]), "order": idx}
    for idx, dance in enumerate(BALLROOM_DANCES, len(BASE_DANCES) + 1)
]
DANCES = BASE_DANCES + SECOND_BASE_DANCES
BONUS_DANCES = [{
    "name": dance,
    "tag": DANCE_TAGS[dance],
    "order": idx
} for idx, dance in enumerate(BALLROOM_DANCES, len(DANCES) + 1)]

STANDARD_DANCES = STANDARD_DANCES + [dance2(dance) for dance in STANDARD_DANCES]
LATIN_DANCES = LATIN_DANCES + [dance2(dance) for dance in LATIN_DANCES]


# Disciplines
BALLROOM = "Ballroom"
STANDARD = "Standard"
LATIN = "Latin"
BALLROOM_DISCIPLINES = [STANDARD, LATIN]
BONUS = "Bonus"
ALL_COMPETITIONS = [c for c in BALLROOM_DISCIPLINES] + [BONUS]


# Dancing roles
LEAD = "Lead"
FOLLOW = "Follow"
ALL_ROLES = [LEAD, FOLLOW]
OPPOSITE_ROLES = {LEAD: FOLLOW, FOLLOW: LEAD}


# Dancing classes
# xTDS classes
TEST = "TEST"
BEGINNERS = "Beginners"
BREITENSPORT_QUALIFICATION = "Breitensport"
AMATEURS = "Amateurs"
PROFESSIONALS = "Professionals"
MASTERS = "Masters"
CHAMPIONS = "Champions"
CLOPEN_QUALIFICATION = "ClOpen"
CLOSED = "CloseD"
OPEN_CLASS = "Open Class"

XTDS_CLASSES = [
    TEST,
    BEGINNERS,
    BREITENSPORT_QUALIFICATION,
    AMATEURS,
    PROFESSIONALS,
    MASTERS,
    CHAMPIONS,
    CLOPEN_QUALIFICATION,
    CLOSED,
    OPEN_CLASS
]
BREITENSPORT_COMPETITIONS = [AMATEURS, PROFESSIONALS, MASTERS, CHAMPIONS]
CLOPEN_COMPETITIONS = [CLOSED, OPEN_CLASS]


# ODK classes
ODK_CLASSES = [
    TEST,
    BREITENSPORT_QUALIFICATION,
    AMATEURS,
    CHAMPIONS,
    OPEN_CLASS,
    BONUS,
]


# SOND classes
ASPIRANTEN_JUNIOREN = "Aspiranten Junioren"
NIEUWELINGEN_JUNIOREN = "Nieuwelingen Junioren"
D_KLASSE_JUNIOREN = "D-Klasse Junioren"
C_KLASSE_JUNIOREN = "C-Klasse Junioren"
B_KLASSE_JUNIOREN = "B-Klasse Junioren"
A_KLASSE_JUNIOREN = "A-Klasse Junioren"
OPEN_KLASSE_JUNIOREN = "Open Klasse Junioren"
ASPIRANTEN_SENIOREN = "Aspiranten Senioren"
NIEUWELINGEN_SENIOREN = "Nieuwelingen Senioren"
D_KLASSE_SENIOREN = "D-Klasse Senioren"
C_KLASSE_SENIOREN = "C-Klasse Senioren"
B_KLASSE_SENIOREN = "B-Klasse Senioren"
A_KLASSE_SENIOREN = "A-Klasse Senioren"
OPEN_KLASSE_SENIOREN = "Open Klasse Senioren"

SOND_CLASSES = [
    TEST,
    ASPIRANTEN_JUNIOREN,
    NIEUWELINGEN_JUNIOREN,
    D_KLASSE_JUNIOREN,
    C_KLASSE_JUNIOREN,
    B_KLASSE_JUNIOREN,
    A_KLASSE_JUNIOREN,
    OPEN_KLASSE_JUNIOREN,
    ASPIRANTEN_SENIOREN,
    NIEUWELINGEN_SENIOREN,
    D_KLASSE_SENIOREN,
    C_KLASSE_SENIOREN,
    B_KLASSE_SENIOREN,
    A_KLASSE_SENIOREN,
    OPEN_KLASSE_SENIOREN
]
SOND_JUNIOREN = [
    ASPIRANTEN_JUNIOREN,
    NIEUWELINGEN_JUNIOREN,
    D_KLASSE_JUNIOREN,
    C_KLASSE_JUNIOREN,
    B_KLASSE_JUNIOREN,
    A_KLASSE_JUNIOREN,
    OPEN_KLASSE_JUNIOREN
]
SOND_SENIOREN = [
    ASPIRANTEN_SENIOREN,
    NIEUWELINGEN_SENIOREN,
    D_KLASSE_SENIOREN,
    C_KLASSE_SENIOREN,
    B_KLASSE_SENIOREN,
    A_KLASSE_SENIOREN,
    OPEN_KLASSE_SENIOREN
]


# Short representations of base items
TAGS = {
    TEST: TEST,
    BEGINNERS: BEGINNERS[:3],
    BREITENSPORT_QUALIFICATION: f"{BREITENSPORT_QUALIFICATION[:2]}Q",
    AMATEURS: AMATEURS[:3],
    PROFESSIONALS: PROFESSIONALS[:4],
    MASTERS: MASTERS[:2],
    CHAMPIONS: CHAMPIONS[:2],
    CLOPEN_QUALIFICATION: f"{CLOPEN_QUALIFICATION[:2]}Q",
    CLOSED: CLOSED[:2],
    OPEN_CLASS: "OC",
    BALLROOM: BALLROOM[:2],
    STANDARD: STANDARD[:2],
    LATIN: LATIN[:2],
    BONUS: BONUS,
    SALSA: SALSA,
    BACHATA: DANCE_TAGS[BACHATA],
    MERENGUE: DANCE_TAGS[MERENGUE],
    POLKA: DANCE_TAGS[POLKA],
}
TAGS.update({dance["name"]: dance["tag"] for dance in DANCES})
TAGS.update({
    c: c.replace("Junioren", "J").replace("Senioren", "S").replace("-Klasse", "").replace("Aspiranten", "Asp")
        .replace("Nieuwelingen", "Nw").replace("Open Klasse", "OK") for c in SOND_CLASSES
})