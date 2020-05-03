from . import db
from .abc import BaseModel, MetaBaseModel


class Student(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Student model """

    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True)
    simconnect_id = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    ranking = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, simconnect_id, email, password):
        self.simconnect_id = simconnect_id
        self.email = email
        self.password = password
        self.ranking = 0
