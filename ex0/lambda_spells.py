from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
    )


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell_name: f"* {spell_name} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, int | float]:
    stats_find: dict[str, int | float] = {}
    max_value = max(mages, key=lambda mage: mage["power"])["power"]
    stats_find.update({"max_power": max_value})
    min_value = min(mages, key=lambda mage: mage["power"])["power"]
    stats_find.update({"min_power": min_value})
    average: float = round((max_value + min_value) / 2, 2)
    stats_find.update({"avg_power": average})
    return stats_find


if __name__ == "__main__":
    artifacts: list[dict[str, Any]] = [
        {"name": "Fire Staff", "power": 92, "type": "accessory"},
        {"name": "Crystal Orb", "power": 85, "type": "armor"},
    ]
    mages: list[dict[str, Any]] = [
        {"name": "Riley", "power": 63, "element": "ice"},
        {"name": "Morgan", "power": 100, "element": "ice"},
        {"name": "Ember", "power": 54, "element": "water"},
        {"name": "Ash", "power": 95, "element": "ice"},
        {"name": "Storm", "power": 66, "element": "fire"},
    ]

    print("Testing artifact sorter...")
    spells: list[str] = ["shield", "blizzard", "freeze", "flash"]
    try:
        sorted_artifact: list[dict[str, Any]] = artifact_sorter(artifacts)
        for x in sorted_artifact:
            print(f"{x['name']} ({x['power']})", end="")
            if x != sorted_artifact[-1]:
                print(" comes before ", end="")
    except Exception as e:
        print(e)

    print("\n\nTesting power filter...")
    print("All mages:")
    try:
        for x in mages:
            print(f"{x['name']} ({x['power']})")
    except Exception as e:
        print(e)
    print("\nStrong mages:")
    try:
        strong_mage: list[dict[str, Any]] = power_filter(mages, 70)
        for x in strong_mage:
            print(f"{x['name']} ({x['power']})")
    except Exception as e:
        print(e)
    print("\nTesting spell transformer...")
    try:
        modif_list: list[str] = spell_transformer(spells)
        for y in modif_list:
            if y != modif_list[-1]:
                print(f"{y} ", end="")
            else:
                print(f"{y}", end="")
    except Exception as e:
        print(e)
    print("\n\nTesting mage stats...")
    try:
        stats: dict[str, int | float] = mage_stats(mages)
        print(f"Max power: {stats['max_power']}")
        print(f"Min power: {stats['min_power']}")
        print(f"Average power: {stats['avg_power']}")
    except Exception as e:
        print(e)
