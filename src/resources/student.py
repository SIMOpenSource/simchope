from flask import request, make_response
from flask_restful import Resource

from src.repositories import StudentRepository


class StudentResource(Resource):
    def post(self):
        simconnect_id = request.args.get('simconnectId')
        existing = StudentRepository.find_if_existing(simconnect_id)
        if existing:
            return make_response(f"User with id:{simconnect_id} already exists!", 400)
        StudentRepository.create(simconnect_id)
        return make_response(f"New user with id:{simconnect_id} is created", 200)
