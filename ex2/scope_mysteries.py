from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count+=1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = 0
    
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


