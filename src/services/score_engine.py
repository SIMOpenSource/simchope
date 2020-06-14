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

    def calculate_and_update_scores(self, score_updates):
        grouped_list = self._convert_group('study_area', 'scores', score_updates,
                                           lambda x: list(map(lambda y: y.score, x)), True)

        for g in grouped_list:
            current_id, current_scores, total_count = g['study_area'], g['scores'], len(g['scores'])
            grouped_scores = self._convert_group('score', 'percent', current_scores,
                                                 lambda x, y: (list(x).count(y) / total_count) * 100.0, False)
            score_list = list(map(lambda x: x['percent'], grouped_scores))
            score_list.extend([0 for i in range(0, 4 - len(grouped_scores))])
            updated = StudyAreaRepository().update_score(current_id, score_list)
            print(f"Updated study area: {updated.json}")

    @staticmethod
    def _convert_group(key1, key2, grouped_list, custom_lambda, use_attr):
        get_attr = operator.attrgetter(key1)
        return \
            [{key1: k, key2: custom_lambda(g)} for k, g in
             itertools.groupby(sorted(grouped_list, key=get_attr), get_attr)] if use_attr else \
                [{key1: k, key2: custom_lambda(g, k)} for k, g in
                 itertools.groupby(sorted(grouped_list))]
