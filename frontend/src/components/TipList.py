# frontend/src/components/TipList.py
from typing import List, Dict

def render_tips(tips: List[Dict]):
    """
    Egyszerű lista-renderelő funkció tipp adatokhoz.
    Tippek: [{ "match": "TeamA - TeamB", "odds": 2.3, "ev": 0.12 }]
    """
    if not tips:
        return "Nincsenek tippek jelenleg."

    lines = ["Aktuális tippek:\n"]
    for tip in tips:
        line = f"- {tip.get('match', 'Ismeretlen')} | Odds: {tip.get('odds', '?')} | EV: {tip.get('ev', '?')}"
        lines.append(line)
    return "\n".join(lines)


if __name__ == "__main__":
    sample = [
        {"match": "Barcelona - Real Madrid", "odds": 1.95, "ev": 0.07},
        {"match": "Juventus - Milan", "odds": 2.4, "ev": 0.11},
    ]
    print(render_tips(sample))
