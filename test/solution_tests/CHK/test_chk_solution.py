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
        assert CheckoutSolution().checkout("AAAAABB") == 245
        assert CheckoutSolution().checkout("AAAAABBEEFFF") == 200 + 30 + 80 + 20
        assert CheckoutSolution().checkout("AAAAABBEEFFFSSS") == 200 + 30 + 80 + 20 + 45
        assert CheckoutSolution().checkout("AAAAABBEEFFFSSSSTXYZ") == 200 + 30 + 80 + 20 + 127

    def test_invalid_input(self):
        assert CheckoutSolution().checkout(".") == -1
        assert CheckoutSolution().checkout(435) == -1
        assert CheckoutSolution().checkout("A435B") == -1
        assert CheckoutSolution().checkout(True) == -1

    def test_empty_input(self):
        assert CheckoutSolution().checkout("") == 0

    def test_2E_get_1B_free(self):
        assert CheckoutSolution().checkout("BEE") == 80
        assert CheckoutSolution().checkout("BBEEEEEE") == 240
        assert CheckoutSolution().checkout("BBEE") == 110 

    def test_pro_customer_offer(self):
        assert CheckoutSolution().checkout("AAAAA") == 200
        assert CheckoutSolution().checkout("AAAAAA") == 250
        assert CheckoutSolution().checkout("AAAAAAAA") == 330
        assert CheckoutSolution().checkout("AA") == 100
        assert CheckoutSolution().checkout("AAAAAAAAA") == 380

    def test_3F_get_1F_free(self):
        assert CheckoutSolution().checkout("FFF") == 20
        assert CheckoutSolution().checkout("FFFFF") == 40
        assert CheckoutSolution().checkout("FFFFFFFFFFFF") == 80
        assert CheckoutSolution().checkout("FFFABC") == 20 + 50 + 30 + 20

    def test_new_offers(self):
        assert CheckoutSolution().checkout("HHHHHHHHHH") == 80
        assert CheckoutSolution().checkout("KK") == 120
        assert CheckoutSolution().checkout("NNNMM") == 135
        assert CheckoutSolution().checkout("PPPPP") == 200
        assert CheckoutSolution().checkout("QQQ") == 80
        assert CheckoutSolution().checkout("RRRQQQ") == 210
        assert CheckoutSolution().checkout("RRRQQQQ") == 230
        assert CheckoutSolution().checkout("UUUU") == 120
        assert CheckoutSolution().checkout("UUU") == 120
        assert CheckoutSolution().checkout("VVV") == 130
        assert CheckoutSolution().checkout("VV") == 90

    def test_STXYZ_offer(self):
        assert CheckoutSolution().checkout("STXYZ") == 82 # ZTY should be removed for 45 + S and X = 45 + 17 + 20
        assert CheckoutSolution().checkout("SSSSTXYZ") == 127





