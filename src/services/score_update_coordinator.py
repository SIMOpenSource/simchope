from .score_engine import ScoreEngine


class ScoreUpdateCoordinator:
    blocks = ['A', 'B', 'C']

    @staticmethod
    def run():
        print("Scheduler started")
        score_engine = ScoreEngine()
        for block in ScoreUpdateCoordinator.blocks:
            score_engine.execute(block)
        print("Score Update Completed")
