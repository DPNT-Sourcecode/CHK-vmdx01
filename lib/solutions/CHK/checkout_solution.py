
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        price_table = {
            "A": {"price": 50, "offer": (3,130)},
            "B": {"price": 30, "offer": (2,45)},
            "C": {"price": 20, "offer": None},
            "D": {"price": 15, "offer": None}
        }

        total = 0
        from collections import Counter
        counts = Counter(skus)

        for item, count in counter.items():
            data = price_table.get("A")
            if data["offer"]:
                offer_num, offer_price = data["offer"]
                