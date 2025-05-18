
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
            "E": {"price": 40, "offers": []}, # 2E get one B free
            "F": {"price": 10, "offers": []}, # 2F get one F free 
            "G": {"price": 20, "offers": []},
            "H": {"price": 20, "offers": [(5,45), (10,80)]},
            "I": {"price": 20, "offers": []},
            "J": {"price": 20, "offers": []},
            "K": {"price": 20, "offers": [(2,150)]},
            "L": {"price": 20, "offers": []},
            "M": {"price": 20, "offers": []},
            "N": {"price": 20, "offers": []}, # 3N get one M free
            "O": {"price": 20, "offers": []},
            "P": {"price": 20, "offers": [(5,200)]},
            "Q": {"price": 20, "offers": [(3,80)]},
            "R": {"price": 20, "offers": []}, # 3R get one Q free
            "S": {"price": 20, "offers": []},
            "T": {"price": 20, "offers": []},
            "U": {"price": 20, "offers": []}, # 3U get one U
            "V": {"price": 20, "offers": [(2,90), (3,130)]},
            "W": {"price": 20, "offers": []},
            "X": {"price": 20, "offers": []},
            "Y": {"price": 20, "offers": []},
            "Z": {"price": 20, "offers": []},
        }

        total = 0
        from collections import Counter
        counts = Counter(skus)

        def update_counts_multi_sku_same(sku: str, current_total: int, amount_needed: int) -> int:
            free_sku = current_total // amount_needed
            return current_total - free_sku

        counts["F"] = update_counts_multi_sku_same("F", counts["F"], 3)
        counts["U"] = 
        if "U" in counts:
            counts = update_counts_multi_sku_same("U", counts, 3)

        def update_counts_multi_sku_different(sku: str, discounted_sku: str, counts: dict[str | int], amount_needed: int) -> int:
            free_sku = sku // amount_needed
            if counts.get(discounted_sku):
                counts[discounted_sku] = max(0, counts[discounted_sku] - free_sku)

        if "B"

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





