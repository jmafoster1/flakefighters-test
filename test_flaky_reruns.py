from flaky_reruns import FlakyReruns


class TestFlakyRuns:

    def test_create_or_delete(self):
        flaky = FlakyReruns("test.txt")
        result = flaky.create_or_delete()
        assert result
