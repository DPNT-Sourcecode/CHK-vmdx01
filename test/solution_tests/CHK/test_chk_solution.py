from solutions.CHK.checkout_solution import CheckoutSolution


class TestCHK():
    def test_single_item_no_offer(self):
        assert CheckoutSolution().checkout("AAA") == 130
