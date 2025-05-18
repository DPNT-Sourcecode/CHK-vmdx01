
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
            "H": {"price": 10, "offers": [(5,45), (10,80)]},
            "I": {"price": 35, "offers": []},
            "J": {"price": 60, "offers": []},
            "K": {"price": 70, "offers": [(2,120)]},
            "L": {"price": 90, "offers": []},
            "M": {"price": 15, "offers": []},
            "N": {"price": 40, "offers": []}, # 3N get one M free
            "O": {"price": 10, "offers": []},
            "P": {"price": 50, "offers": [(5,200)]},
            "Q": {"price": 30, "offers": [(3,80)]},
            "R": {"price": 50, "offers": []}, # 3R get one Q free
            "S": {"price": 20, "offers": []}, # buy any 3 of (S,T,X,Y,Z) for 45
            "T": {"price": 20, "offers": []}, # buy any 3 of (S,T,X,Y,Z) for 45
            "U": {"price": 40, "offers": []}, # 3U get one U
            "V": {"price": 50, "offers": [(2,90), (3,130)]},
            "W": {"price": 20, "offers": []},
            "X": {"price": 17, "offers": []}, # buy any 3 of (S,T,X,Y,Z) for 45
            "Y": {"price": 20, "offers": []}, # buy any 3 of (S,T,X,Y,Z) for 45
            "Z": {"price": 21, "offers": []}, # buy any 3 of (S,T,X,Y,Z) for 45
        }

        group_items = set("S", "T", "X", "Y", "Z")
        group_price = 45
        group_size = 3

        


        total = 0
        from collections import Counter
        counts = Counter(skus)

        counts["F"] = counts["F"] - (counts["F"] // 3)
        counts["U"] = counts["U"] - (counts["U"] // 4) 
        counts["B"] =  max(0, counts["B"] - (counts["E"] // 2))
        counts["M"] =  max(0, counts["M"] - (counts["N"] // 3))
        counts["Q"] =  max(0, counts["Q"] - (counts["R"] // 3))

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




