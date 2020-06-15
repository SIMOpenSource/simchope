from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from src import config
from src.models import db
from src.resources.routes import initialize_routes
from src.services import ScoreUpdateCoordinator

scheduler = BackgroundScheduler()
scheduler.add_job(ScoreUpdateCoordinator.run, config.SCHEDULER_TRIGGER, seconds=30)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)
db.app = app

CORS(app)
api = Api(app)
initialize_routes(api)

# Uncomment this to run scheduler - configure interval in seconds at line 12
# scheduler.start()


@app.route('/')
def api_health():
    return 'Server is running as expected!'


if __name__ == '__main__':
    app.run()
