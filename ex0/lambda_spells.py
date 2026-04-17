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
