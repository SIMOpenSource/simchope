from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

import config
from src.models import db, Student, ScoreUpdate, StudyArea
from src.repositories import StudentRepository, StudyAreaRepository, ScoreUpdateRepository
from src.services import ScoreUpdateCoordinator

scheduler = BackgroundScheduler()
scheduler.add_job(ScoreUpdateCoordinator.run, config.SCHEDULER_TRIGGER, seconds=30)
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
# scheduler.start()
db.init_app(app)
db.app = app


@app.route('/')
def api_base():
    return 'API Base Reached!'


# @app.route('/students', methods=['GET'])
# def get_current_user(simconnect_id):
#     student = StudentRepository.get_student(simconnect_id)
#     return jsonify({
#         "simconnectId": student.simconnect_id,
#         "ranking": student.ranking
#     })


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


@app.route('/study-areas', methods=['GET', 'POST'])
def handle_locations():
    if request.method == "GET":
        if 'block' in request.args:
            result = [sa.json for sa in StudyAreaRepository.get_by_block(request.args.get('block'))]
        else:
            result = [sa.json for sa in StudyAreaRepository.get_all()]
        return jsonify(result)

    if request.method == 'POST':
        data = request.json
        existing = StudyArea.query.filter(StudyArea.area_name == data['area_name']).first()
        if existing:
            return make_response(f'{data.area_name} already created!')
        new_study_area = StudyArea(
            area_name=data['area_name'],
            block=data['block'],
            level=data['level'],
            scores=data['scores'],
            table_count=data['table_count'],
            capacity=data['capacity']
        )
        db.session.add(new_study_area)
        db.session.commit()
        return make_response(f"{new_study_area} successfully created")


@app.route('/study-areas/<id>', methods=['GET'])
def get_study_area(id):
    return jsonify(StudyAreaRepository.get_by_id(id).json)


# TODO: Remove after testing
@app.route('/scores', methods=['GET'])
def get_scores():
    return jsonify([su.json for su in ScoreUpdateRepository.get_scores()])


# end-point to create score updates, to be polled by scheduler later
@app.route('/score/update', methods=['POST'])
def create_score():
    data = request.json
    score = ScoreUpdateRepository.create(
        data['study_area'], data['score'], data['student']
    )
    return jsonify(score.json)


if __name__ == '__main__':
    app.run()
