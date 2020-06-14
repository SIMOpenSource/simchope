from flask import request, jsonify, make_response
from flask_restful import Resource

from repositories import StudyAreaRepository


class StudyAreasResource(Resource):
    def get(self):
        if 'block' in request.args:
            result = [sa.json for sa in StudyAreaRepository.get_by_block(request.args.get('block'))]
        else:
            result = [sa.json for sa in StudyAreaRepository.get_all()]
        return make_response(jsonify(result), 200)


class StudyAreaResource(Resource):
    def get(self, study_area_id):
        study_area = StudyAreaRepository.get_by_id(study_area_id)
        return make_response(jsonify(study_area.json), 200)