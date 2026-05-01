from typing import Callable


def mage_counter() -> Callable:
    count = 1 #RECHECK IT 

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power
    
    def accumulate_power(initial_power: int) -> int:
        nonlocal total_power
        total_power+=initial_power
        return total_power

    return accumulate_power


def enchantment_factory(enchantment_type: str) -> Callable:
    
    def enchanted(enchantment_type: str, item_name: str) -> str:
        return enchantment_type+' '+item_name

    return enchanted


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: int) -> None:
        print(f"Store {key} = {value}")
        vault[key] = value

    
    def recall(key: str) -> None:
        if key in vault:
            print(f"Recall {key} = {vault[key]}")
            return vault[key]
        else:
            print(f"Recall {key} : Memory not found")
            return "Memory not found"

    return({"Store": store, "Recall": recall})


if __name__ == "__main__":

    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)

    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    fire = enchantment_factory("flamming")
    ice = enchantment_factory("frozen")

    print(fire("flamming", "Sword"))
    print(ice("frozen", "Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()

    vault["Store"]("secret", 42)
    print(f"Recall ’secret’: {vault['Recall']('secret')}")
    print(f"Recall ’unknown’: {vault['Recall']('unknown')}")
