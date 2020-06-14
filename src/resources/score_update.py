from flask import jsonify, make_response, request
from flask_restful import Resource
from sqlalchemy.exc import NoReferencedColumnError

from repositories import ScoreUpdateRepository


class ScoreUpdateResource(Resource):
    def get(self):
        result = [su.json for su in ScoreUpdateRepository.get_scores()]
        return make_response(jsonify(result), 200)

    def post(self):
        try:
            data = request.json
            score = ScoreUpdateRepository.create(
                data['study_area'], data['score'], data['student']
            )
        except NoReferencedColumnError:
            return make_response("Error while updating with this user", 500)
        return make_response(score.json, 200)
