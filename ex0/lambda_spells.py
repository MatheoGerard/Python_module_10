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


if __name__ == "__main__":
    artifacts: list[dict] = [
        {"name": "Fire Staff", "power": 92, "type": "accessory"},
        {"name": "Crystal Orb", "power": 85, "type": "armor"},
    ]
    mages: list[dict] = [
        {"name": "Riley", "power": 63, "element": "ice"},
        {"name": "Morgan", "power": 100, "element": "ice"},
        {"name": "Ember", "power": 54, "element": "water"},
        {"name": "Ash", "power": 95, "element": "ice"},
        {"name": "Storm", "power": 66, "element": "fire"},
    ]

    print("Testing artifact sorter...")
    spells: list[str] = ["shield", "blizzard", "freeze", "flash"]
    try:
        sorted_artifact: list[dict] = artifact_sorter(artifacts)
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
        strong_mage: list[dict] = power_filter(mages, 70)
        for x in strong_mage:
            print(f"{x['name']} ({x['power']})")
    except Exception as e:
        print(e)
    print("\nTesting spell transformer...")
    try:
        modif_list: list[str] = spell_transformer(spells)
        for x in modif_list:
            if x != modif_list[-1]:
                print(f"{x} ", end="")
            else:
                print(f"{x}", end="")
    except Exception as e:
        print(e)
    print("\n\nTesting mage stats...")
    try:
        stats: dict = mage_stats(mages)
        print(f"Max power: {stats['max_power']}")
        print(f"Min power: {stats['min_power']}")
        print(f"Average power: {stats['avg_power']}")
    except Exception as e:
        print(e)
