from datetime import datetime
from enum import Enum

from sqlalchemy import inspect

from . import db
from .abc import BaseModel, MetaBaseModel


class StudyArea(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The StudyArea model """

    __tablename__ = "study_area"

    id = db.Column(db.Integer, primary_key=True)
    area_name = db.Column(db.String(), nullable=False)
    block = db.Column(db.String(), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    _scores = db.Column(db.String(), nullable=False)
    table_count = db.Column(db.Integer, nullable=True)
    capacity = db.Column(db.Integer, nullable=True)
    _facilities = db.Column(db.String(), nullable=True)
    last_updated = db.Column(db.DateTime, nullable=False)

    def __init__(self, area_name, block, level, scores, table_count, capacity, facilities):
        self.area_name = area_name
        self.block = block
        self.level = level
        self.scores = scores
        self.table_count = table_count
        self.capacity = capacity
        self.facilities = facilities
        self.last_updated = datetime.utcnow()

    @property
    def scores(self):
        return list(map(lambda x: float(x), str(self._scores).split(";")))

    @scores.setter
    def scores(self, scores):
        self._scores = ";".join(scores)

    @property
    def facilities(self):
        return list(str(self._facilities).split(","))

    @facilities.setter
    def facilities(self, facilities):
        self._facilities = ",".join(facilities)

    @property
    def json(self):
        attr_dict = self._to_dict()
        attr_dict.update({'facilities': self.facilities})
        attr_dict.update({'scores': self.scores})
        return {
            column: value
            if not isinstance(value, datetime)
            else value.strftime("%Y-%m-%d")
            for column, value in attr_dict.items()
            if column not in self.to_json_filter
            if column not in ["_facilities", "_scores"]
        }


class Facility(Enum):
    COMPUTERS = "COMPUTERS"
    OUTDOOR_SEATS = "OUTDOOR_SEATS"
    PRINTING = "PRINTING"
    REFRESHMENTS = "REFRESHMENTS"
    SOCKETS = "SOCKETS"
    TOILETS = "TOILETS"
