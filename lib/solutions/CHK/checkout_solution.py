
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
            "F": {"price": 10, "offers": []}, # apply 2F get one F free separately
            "G": {"price": 20, "offers": []},
            "H": {"price": 20, "offers": [(5,45), (10,80)]},
            "I": {"price": 20, "offers": []},
            "J": {"price": 20, "offers": []},
            "K": {"price": 20, "offers": [(2,150)]},
            "L": {"price": 20, "offers": []},
            "M": {"price": 20, "offers": []},
            "N": {"price": 20, "offers": []}, # apply 3N get one M free separately
            "O": {"price": 20, "offers": []},
            "P": {"price": 20, "offers": [(5,200)]},
            "Q": {"price": 20, "offers": [(3,80)]},
            "R": {"price": 20, "offers": []}, # apply 3R get one Q free separately
            "S": {"price": 20, "offers": []},
            "T": {"price": 20, "offers": []},
            "U": {"price": 20, "offers": []}, # apply 3U get one U separately
            "V": {"price": 20, "offers": [(2,90), (3,130)]},
            "W": {"price": 20, "offers": []},
            "X": {"price": 20, "offers": []},
            "Y": {"price": 20, "offers": []},
            "Z": {"price": 20, "offers": []},
        }

        total = 0
        from collections import Counter
        counts = Counter(skus)

        # Free F discount will not be affected by other discounts, so always apply
        def update_sku_multiple_sku_free_sku_offer(sku: str, counts: dict[str | int], ) -> int:
            total_sku = counts[sku]
            free_sku = total_sku // 


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


