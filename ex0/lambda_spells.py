def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell_name: f"* {spell_name} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    stats_find: dict = {}
    max_value = max(mages, key=lambda mage: mage["power"])["power"]
    stats_find.update({"max_power": max_value})
    min_value = min(mages, key=lambda mage: mage["power"])["power"]
    stats_find.update({"min_power": min_value})
    average: float = round((max_value + min_value) / 2, 2)
    stats_find.update({"avg_power": average})
    return stats_find
