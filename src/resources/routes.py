from .score_update import ScoreUpdateResource
from .study_area import StudyAreaResource, StudyAreasResource
from .student import StudentResource


def initialize_routes(api):
    # StudyArea end-points
    api.add_resource(StudyAreaResource, '/api/study-area/<study_area_id>')
    api.add_resource(StudyAreasResource, '/api/study-areas')

    # Score end-points
    api.add_resource(ScoreUpdateResource, '/api/score')

    # Student end-points
    api.add_resource(StudentResource, '/api/student')
