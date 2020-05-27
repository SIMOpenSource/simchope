from datetime import datetime

from . import db
from .abc import BaseModel, MetaBaseModel


class StudyArea(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The StudyArea model """

    __tablename__ = "study_area"

    id = db.Column(db.Integer, primary_key=True)
    area_name = db.Column(db.String(), nullable=False)
    block = db.Column(db.String(), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Numeric, nullable=False)
    table_count = db.Column(db.Integer, nullable=True)
    capacity = db.Column(db.Integer, nullable=True)
    last_updated = db.Column(db.DateTime, nullable=False)

    def __init__(self, area_name, block, level, score, table_count, capacity):
        self.area_name = area_name
        self.block = block
        self.level = level
        self.score = score
        self.table_count = table_count
        self.capacity = capacity
        self.last_updated = datetime.utcnow()
