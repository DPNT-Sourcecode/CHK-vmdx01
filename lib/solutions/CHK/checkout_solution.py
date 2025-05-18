
class CheckoutSolution:

    def is_valid_skus(skus):

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

        for item, count in counts.items():
            data = price_table.get(item)
            if not data:
                return -1

            if data["offer"]:
                offer_num, offer_price = data["offer"]
                total_offers_applied = count // offer_num
                remaining_items = count % offer_num
                total += total_offers_applied * offer_price + remaining_items * data["price"]
            else:
                total += data["price"] * count

        return total


