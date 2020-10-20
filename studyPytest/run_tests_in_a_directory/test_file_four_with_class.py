class TestMyClass():
    def test_notrun_case_one_fail(self):
        assert 0

    def test_run_case_one_success(self):
        assert 1

    def test_run_case_two_success(self):
        assert 1

    def test_notrun_case_two_fail(self):
        assert 0

    def test_run_case_three_success(self):
        assert 1

    def test_notrun_case_three_fail(self):
        assert 0