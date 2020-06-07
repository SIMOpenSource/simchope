from statistics import mean
import itertools
import operator

from repositories import StudyAreaRepository, ScoreUpdateRepository


class ScoreEngine:
    scores = []

    def __init__(self):
        self.scores = ScoreUpdateRepository.get_last_fifty_scores()

    def execute(self, block):
        print(f"Job Running for block {block}")
        score_updates = self.get_scores(block)
        print(f"Retrieved the following score updates {score_updates} for block {block}")
        self.calculate_and_update_scores(score_updates)

    def get_scores(self, block):
        study_area_ids = self.derive_study_area_ids(block)
        scores = list(filter(lambda x: x.study_area in study_area_ids, self.scores))
        return scores

    @staticmethod
    def derive_study_area_ids(block):
        study_areas = set(map(lambda x: x.id, StudyAreaRepository.get_by_block(block)))
        return study_areas

    @staticmethod
    def calculate_and_update_scores(score_updates):
        get_attr = operator.attrgetter('study_area')
        grouped_list = [{'study_area': k, 'scores': list(map(lambda x: x.score, g))} for k, g in
                        itertools.groupby(sorted(score_updates, key=get_attr), get_attr)]
        for g in grouped_list:
            current_id, current_scores, total_count = g['study_area'], g['scores'], len(g['scores'])
            grouped_scores = [{'score': k, 'count': list(g).count(k)} for k, g in itertools.groupby(current_scores)]
            score_mean = mean(map(lambda x: x.score, current_scores))
            print(f"Score mean for {current_id}: {score_mean}")
            current_score = StudyAreaRepository.get_by_id(current_id).score
            print(f"Current score for {current_id}: {current_score}")
            updated = StudyAreaRepository().update_score(current_id, current_score + score_mean / 2)
            print(f"Updated study area: {updated.json}")
