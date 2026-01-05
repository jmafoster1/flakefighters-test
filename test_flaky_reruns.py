from flaky_reruns import FlakyReruns
import uuid


class TestFlakyRuns:

    def test_pass(self):
        assert True

    def test_create_or_delete(self):
        flaky = FlakyReruns(f"{uuid.uuid4()}.txt")
        result = flaky.create_or_delete()
        assert not result
