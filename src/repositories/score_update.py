from models import ScoreUpdate


class ScoreUpdateRepository:

    @staticmethod
    def get_scores():
        return ScoreUpdate.query.all()

    @staticmethod
    def get_last_fifty_scores():
        return ScoreUpdate.query.order_by(ScoreUpdate.id.desc()).limit(50).all()

    @staticmethod
    def create(study_area, score, student):
        score = ScoreUpdate(student, study_area, score)
        return score.save()