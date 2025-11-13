"""
Fusion Engine – Tippmester és Data Mining AI összekapcsolása.
Feladata: két független predikciós forrás (saját + Data Mining) összevetése.
"""

class FusionEngine:
    def merge_predictions(self, tips_self, tips_dm):
        """
        Két forrás eredményeit egyesíti.
        Ha ugyanazt a mérkőzést javasolják → bekerül automatikusan.
        Ha eltérnek → súlyozott döntéssel választ.
        """
        merged = []

        all_matches = set(tips_self.keys()) | set(tips_dm.keys())

        for match in all_matches:
            t1 = tips_self.get(match)
            t2 = tips_dm.get(match)

            if t1 and t2:
                merged.append(self._combine(t1, t2, force=True))
            elif t1:
                merged.append(self._combine(t1))
            elif t2:
                merged.append(self._combine(t2))
        return merged

    def _combine(self, t1, t2=None, force=False):
        """Két tipp adatainak intelligens kombinálása."""
        if t2 and force:
            avg_prob = (t1.get("probability", 0.5) + t2.get("probability", 0.5)) / 2
            return {
                "match": t1["match"],
                "tip": t1["tip"],
                "odds": max(t1.get("odds", 1.0), t2.get("odds", 1.0)),
                "probability": avg_prob,
                "source": "Fusion"
            }
        else:
            t = t1 or t2
            return {**t, "source": t.get("source", "Single")}
