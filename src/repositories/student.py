from flask import jsonify

from models import Student


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
