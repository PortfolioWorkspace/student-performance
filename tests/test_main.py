from main import main


class TestMain:
    def test_returns_none(self):
        assert main() is None
