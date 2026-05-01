import operator
from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable, Any


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
    new_functions = {}
    ice = partial(base_enchantment, power=50, element="ice")
    fire = partial(base_enchantment, power=50, element="fire")
    lightening = partial(base_enchantment, power=50, element="lightening")
    new_functions = {"ice": ice, "fire": fire, "lightening": lightening}
    return new_functions


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(var: Any):
        return "Unknown spell type"

    @dispatcher.register
    def _(var: int) -> str:
        return f"Damage spell: {var} damage"

    @dispatcher.register
    def _(var: str) -> str:
        return f"Enchantment: {var}"

    @dispatcher.register
    def _(var: list) -> str:
        return f"Multi-cast spell: {len(var)} spells cast"

    return dispatcher


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    try:
        print("Sum:", spell_reducer(spells, "add"))
        print("Product:", spell_reducer(spells, "mul"))
        print("Max:", spell_reducer(spells, "max"))
    except Exception as e:
        print(e)

    print("\nTesting memoized fibonacci...")

    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")

    dispatch = spell_dispatcher()

    print(dispatch(21))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch(3.14))
