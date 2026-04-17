from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spells(target: str, power: int) -> tuple[str, str]:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return tuple([result1, result2])

    return combined_spells


def power_amplifier(base_spell: Callable, multiplier: int) ->Callable:
    def small_amplify(target: str, power: int) -> str:
        return base_spell(target, power*multiplier)
    return small_amplify


def conditional_caster(condition: Callable, spell: Callable) ->Callable:
    def new_spell(target: str, power: int) -> str:
        if condition:
            return spell(target, power)
        else:
            return "Spell fizzled"
    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def meow(target, power) -> list[str]:
        mylist = []
        for i in spells:
            mylist.append(i(target,power)) 
        return mylist
    return meow


if __name__ == '__main__':
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals restores {target} for {power} HP"

    def shield(target: str, power: int) -> str:
        return f"Increase {target}'s defense by {power}"

    print("Testing spell combiner...")
    result = spell_combiner(fireball, heal)("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

# ---------------------------------------------------
    # fireball_power returns power value to verify multiplication
    def fireball_power(target: str, power: int) -> int:
        return power
    print("\nTesting power amplifier...")
    original = fireball_power("Dragon", 10)
    amplified = power_amplifier(fireball_power, 3)("Dragon", 10)
    print(f"Original: {original}, Amplified: {amplified}")

# --------------------------------------------------
    print("\nTesting conditional caster...")

    def is_enemy(target: str, power: int) -> bool:
        return target in ("Dragon", "Orc")

    guarded_fireball = conditional_caster(is_enemy, fireball)
    # v3 change: spells now take (target, power) - pass power arg too
    print(guarded_fireball("Dragon", 10))  # → works
    print(guarded_fireball("Ally", 10)) 
    print("\nTesting spell sequences...")
    spell_list = [fireball, heal, shield]
    seq = spell_sequence(spell_list)
    res_seq = seq("dragon", 10)
    print(f"Spell Sequence: {res_seq}")
