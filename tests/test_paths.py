from pathlib import Path


class TestPaths:
    def test_raw_dataset_exists(self):
        assert Path("data/raw/student_performance.csv").exists()
