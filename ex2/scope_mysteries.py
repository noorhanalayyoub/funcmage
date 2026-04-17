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


