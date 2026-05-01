def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter((lambda x: x['power'] >= min_power), mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '*'+x+'*', spells))


def mage_stats(mages: list[dict]) -> dict:
    final_dict = {'min_power': (min(mages, key=lambda m: m['power'])['power']),
                  'max_power': (max(mages, key=lambda m: m['power'])['power']),
                  'avg_power': round(sum(i['power'] for i in mages)
                                     / len(mages), 2)
                  }
    return final_dict


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [
        {'name': 'Fire Staff', 'power': 81, 'type': 'relic'},
        {'name': 'Shadow Blade', 'power': 112, 'type': 'relic'},
        {'name': 'Light Prism', 'power': 60, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 96, 'type': 'weapon'}
    ]

    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']}"
          f"power comes before {sorted_artifacts[1]['name']}"
          f"({sorted_artifacts[1]['power']} power)")

    print("\nTesting power filter...")
    mages = [
        {'name': 'Casey', 'power': 65, 'element': 'ice'},
        {'name': 'Sage', 'power': 98, 'element': 'wind'},
        {'name': 'Kai', 'power': 92, 'element': 'water'},
        {'name': 'Casey', 'power': 87, 'element': 'light'},
        {'name': 'Sage', 'power': 87, 'element': 'water'}
    ]
    print(power_filter(mages, 92))

    print("\nTesting mage stats...")
    print(mage_stats(mages))

    print("\nTesting spell transformer...")
    spells = ['earthquake', 'darkness', 'freeze', 'tsunami']
    print(" ".join(spell_transformer(spells)))


if __name__ == "__main__":
    print("Testing artifact sorter...")
    a = artifact_sorter([{'name': 'Kai', 'power': 94, 'element': 'wind'},
                        {'name': 'Phoenix', 'power': 56, 'element': 'light'}])
    print(f"{a[0]['name']} ({a[0]['power']} power) comes before{
        a[1]["name"]} ({a[1]['power']} power)")
    print("\nTesting spell transformer...")
    s = spell_transformer(['freeze', 'flash', 'blizzard', 'earthquake'])
    for i in s:
        print(i, end=" ")
    print("\n\n Testing power filter")
    mages = [
        {'name': 'Casey', 'power': 74, 'element': 'earth'},
        {'name': 'Ember', 'power': 57, 'element': 'wind'},
        {'name': 'Zara', 'power': 82, 'element': 'light'},
        {'name': 'Ash', 'power': 51, 'element': 'lightning'},
        {'name': 'Alex', 'power': 98, 'element': 'light'}
    ]
    p = power_filter(mages, 70)
    mage: dict[str, object]
    for mage in p:
        print(mage, end=" ")
    m = mage_stats(mages)

    print("\n\nTesting mage stats")
    print(f"max power: {m['max_power']}")
    print(f"min power: {m['min_power']}")
    print(f"avg power: {m['avg_power']}")
