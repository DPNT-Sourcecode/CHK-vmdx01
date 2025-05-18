
class CheckoutSolution:

    def is_valid_skus(self, skus: str) -> bool:
        import re
        return bool(re.fullmatch(r"[A-Z]*", str(skus)))

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        if not self.is_valid_skus(skus):
            return -1

        price_table = {
            "A": {"price": 50, "offer": [(3,130), (5,200)]},
            "B": {"price": 30, "offer": [(2,45)]},
            "C": {"price": 20, "offer": []},
            "D": {"price": 15, "offer": []},
            "E": {"price": 40, "offer": []} # apply 2E for 1B separately
        }

        total = 0
        from collections import Counter
        counts = Counter(skus)
        
        free_b = counts["E"] // 2
        if counts.get("B"):
            counts["B"] = max(0, counts["B"] - free_b)

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