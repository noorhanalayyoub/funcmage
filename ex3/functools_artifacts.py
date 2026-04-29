import operator
from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable

def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        x = reduce(operator.add, spells)
        return x
    elif operation == "multiply":
        x = reduce(operator.mul, spells)
        return x
    elif operation == "max":
        x = reduce(max, spells)
        return x
    elif operation == "min":
        x = reduce(min, spells)
        return x
    else:
        raise ValueError("Unknown spell type")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    new_functions ={}
    ice = partial(base_enchantment, power = 50, element = "ice")
    fire = partial(base_enchatment, power = 50, element = "fire")
    lightening = partial(base_enchatment, power = 50, element = "lightening")
    new_functions ={"ice": ice, "fire": fire, "lightening": lightening}
    return new_functions

@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n<2:
        return 1
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def base_function(Any)

