class FusionEngine:
    """
    Összefésüli a Tippmester és a Data Mining AI javaslatait.
    Ha ugyanazt a tippet adják → az bekerül.
    Ha különböznek → súlyozott döntés.
    """

    def merge_predictions(self, tips_self, tips_dm):
        merged = []
        for match in set(tips_self.keys()) | set(tips_dm.keys()):
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
        """Két tipp kombinálása"""
        if t2 and force:
            avg_prob = (t1["probability"] + t2["probability"]) / 2
            return {
                "match": t1["match"],
                "tip": t1["tip"],
                "odds": max(t1["odds"], t2["odds"]),
                "probability": avg_prob,
                "source": "Fusion"
            }
        else:
            t = t1 or t2
            return {**t, "source": t.get("source", "Single")}
