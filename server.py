from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_restful import Api

from src import config
from src.models import db, Student
from src.resources.routes import initialize_routes
from src.services import ScoreUpdateCoordinator

scheduler = BackgroundScheduler()
scheduler.add_job(ScoreUpdateCoordinator.run, config.SCHEDULER_TRIGGER, seconds=30)

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

# scheduler.start()

db.init_app(app)
db.app = app

initialize_routes(api)


@app.route('/')
def api_base():
    return 'API Base Reached!'


@app.route('/students', methods=['GET'])
def show_users():
    data = Student.query.order_by(Student.simconnect_id).all()
    result = \
        [
            {
                "id": student.simconnect_id,
                "ranking": student.ranking
            } for student in data
        ]
    return jsonify(result)


@app.route('/student', methods=['POST'])
def create_user():
    simconnect_id = request.args.get('simconnectId')
    email = str(simconnect_id) + '@mymail.sim.edu.sg'
    password = simconnect_id
    existing = Student.query.filter(Student.simconnect_id == simconnect_id).first()
    if existing:
        return make_response(f'{simconnect_id} already created!')
    new_student = Student(
        simconnect_id=simconnect_id,
        email=email,
        password=password
    )
    db.session.add(new_student)
    db.session.commit()
    return make_response(f"{new_student} successfully created")


if __name__ == '__main__':
    app.run()
