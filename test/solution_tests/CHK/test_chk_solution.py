from solutions.CHK.checkout_solution import CheckoutSolution


class TestCHK():
    def test_single_item_no_offer(self):
        assert CheckoutSolution().checkout("A") == 50
        assert CheckoutSolution().checkout("B") == 30
        assert CheckoutSolution().checkout("C") == 20
        assert CheckoutSolution().checkout("D") == 15

    def test_single_sku_with_no_offer(self):
        assert CheckoutSolution().checkout("CCC") == 60

    def test_single_sku_with_offer(self):
        assert CheckoutSolution().checkout("AAA") == 130

    def test_multi_sku_with_offer(self):
        assert CheckoutSolution().checkout("AAAAABB") == 275


