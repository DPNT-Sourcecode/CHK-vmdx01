
class CheckoutSolution:

    def is_valid_skus(self, skus: str) -> bool:
        import re
        return bool(re.fullmatch(r"[A-Z]*", str(skus)))

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        if not self.is_valid_skus(skus):
            return -1

        price_table = {
            "A": {"price": 50, "offers": [(3,130), (5,200)]},
            "B": {"price": 30, "offers": [(2,45)]},
            "C": {"price": 20, "offers": []},
            "D": {"price": 15, "offers": []},
            "E": {"price": 40, "offers": []}, # apply 2E for 1B separately
            "F": {"price": 10, "offers": []} # apply 2F get one F free separately
        }

        total = 0
        from collections import Counter
        counts = Counter(skus)

        # Free F discount will not be affected by other discounts, so always apply
        if "F" in counts:
            total_f = counts["F"]
            free_f = total_f // 3
            counts["F"] = total_f - free_f

        # Free B discount is always better than 50% of a B if you buy two, so always apply
        free_b = counts["E"] // 2
        if counts.get("B"):
            counts["B"] = max(0, counts["B"] - free_b)

        for item, count in counts.items():
            data = price_table.get(item)
            if not data:
                return -1

            # This assumes that offers are highest offer_num will be the best offer
            offers = sorted(data["offers"], reverse=True)

            for offer_num, offer_price in offers:
                offers_applied = count // offer_num
                count = count % offer_num
                total += offers_applied * offer_price 

            total += data["price"] * count

        return total