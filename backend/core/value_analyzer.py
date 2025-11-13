"""
Tippmester AI Fusion 1.0 – Value Analyzer 3.0
Két szálas (dual-stream) predikciós rendszer:
1️⃣ Saját Monte Carlo és ML predikció
2️⃣ AI Data Mining javaslatok beolvasása és kombinálása
"""

from core.montecarlo_engine import MonteCarloEngine
from fusion.mining_bridge import DataMiningBridge
from core.fusion_engine import FusionEngine


class ValueAnalyzer:
    def __init__(self):
        self.mc_engine = MonteCarloEngine()
        self.dm_bridge = DataMiningBridge()
        self.fusion = FusionEngine()

    def run_dual_stream(self, matches):
        """
        Fő belépési pont – két szál párhuzamos futtatása.
        1️⃣ Tippmester saját Monte Carlo szimulációk
        2️⃣ Data Mining AI tanácsok lekérése
        Ezután a FusionEngine egyesíti az eredményeket.
        """
        print("▶️ Monte Carlo predikciók futtatása...")
        tips_self = self.mc_engine.find_value_odds(matches)

        print("▶️ Data Mining ajánlások lekérése...")
        tips_dm = self.dm_bridge.get_advice_batch(matches)

        print("🔄 Fusion motor kombinálja az eredményeket...")
        final_tips = self.fusion.merge_predictions(tips_self, tips_dm)

        print(f"✅ Elemzés kész ({len(final_tips)} tipp jött létre)")
        return final_tips
