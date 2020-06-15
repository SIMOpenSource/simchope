from datetime import datetime

from . import db
from .abc import BaseModel, MetaBaseModel


class ScoreUpdate(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The ScoreUpdate model """

    __tablename__ = "score_update"

    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.String(), db.ForeignKey('student.simconnect_id'), nullable=False)
    study_area = db.Column(db.Integer, db.ForeignKey('study_area.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, student, study_area, score):
        self.student = student
        self.study_area = study_area
        self.score = score
        self.timestamp = datetime.now()
