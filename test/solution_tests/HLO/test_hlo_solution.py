from solutions.HLO.hello_solution import HelloSolution


class TestHLO():
    def test_hello(self):
        assert HelloSolution().hello("Dave") == "hello world"
