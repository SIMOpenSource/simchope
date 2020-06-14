from models import StudyArea


class StudyAreaRepository:

    @staticmethod
    def get_all():
        study_areas = StudyArea.query.all()
        return study_areas

    @staticmethod
    def get_by_id(id):
        return StudyArea.query.filter_by(id=id).one()

    @staticmethod
    def get_by_block(block):
        study_areas = StudyArea.query.filter_by(block=block).all()
        return study_areas

    def update_score(self, id, new_score):
        study_area = self.get_by_id(id)
        study_area.scores = new_score
        return study_area.save()
