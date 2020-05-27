from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .score_update import ScoreUpdate
from .student import Student
from .study_area import StudyArea
