import logging
import os

DEBUG = os.getenv("ENVIRONMENT") == "DEV"
APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "/application")
HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))

DB_CONTAINER = os.getenv("APPLICATION_DB_CONTAINER", "localhost")
POSTGRES = {
    "user": os.getenv("APPLICATION_POSTGRES_USER", "simchope"),
    "pw": os.getenv("APPLICATION_POSTGRES_PW", "simchope"),
    "host": os.getenv("APPLICATION_POSTGRES_HOST", DB_CONTAINER),
    "port": os.getenv("APPLICATION_POSTGRES_PORT", 5432),
    "db": os.getenv("APPLICATION_POSTGRES_DB", "simchope"),
}
DB_URI = os.getenv("DATABASE_URL", "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES)
SQLALCHEMY_TRACK_MODIFICATIONS = False

SCHEDULER_TRIGGER = os.getenv("SCHEDULER_TRIGGER", "interval")
SCHEDULER_INTERVAL = {
    "seconds"
}


# logging.basicConfig(
#     filename=os.getenv("SERVICE_LOG", "server.log"),
#     level=logging.DEBUG,
#     format="%(levelname)s: %(asctime)s \
#         pid:%(process)s module:%(module)s %(message)s",
#     datefmt="%d/%m/%y %H:%M:%S",
# )