from flask import jsonify

from src.models import Student


class StudentRepository:

    @staticmethod
    def get_all():
        students = Student.query.order_by(Student.simconnect_id).all()
        result = \
            [
                {
                    "id": student.simconnect_id,
                    "ranking": student.ranking
                } for student in students
            ]
        return jsonify(result)

    @staticmethod
    def get_student(simconnect_id):
        student = Student.query.filter_by(simconnect_id=simconnect_id).one()
        return student

    @staticmethod
    def find_if_existing(simconnect_id):
        return Student.query.filter_by(simconnect_id=simconnect_id).first()

    @staticmethod
    def create(simconnect_id):
        email = str(simconnect_id) + '@mymail.sim.edu.sg'
        password = simconnect_id
        student = Student(simconnect_id, email, password)
        return student.save()
