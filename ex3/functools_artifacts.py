import operator as op
from functools import partial, reduce, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    if operation == "add":
        return reduce(op.add, spells)
    elif operation == "multiply":
        return reduce(op.mul, spells)
    elif operation == "max":
        return max(spells)
    elif operation == "min":
        return min(spells)
    else:
        raise ValueError("operation is unknown")


def base(power: int, element: str, target: str) -> str:
    if not isinstance(power, int):
        raise TypeError("power must be an int")
    if not isinstance(element, str):
        raise TypeError("element must be a str")
    if not isinstance(target, str):
        raise TypeError("target must be a str")
    return f"Launch a {element} sort and do {power} damage to {target}!"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    if not callable(base_enchantment):
        raise TypeError("base_enchantment must be callable")
    return {
        "fire": partial(base_enchantment, power=50, element="fire"),
        "freeze": partial(base_enchantment, power=50, element="freeze"),
        "poison": partial(base_enchantment, power=50, element="poison"),
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return f"unknown spell type: {spell}"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells_pow: list[int] = [10, 5, 2, 3]
    try:
        print(f"Sum: {spell_reducer(spells_pow, 'add')}")
        print(f"Product: {spell_reducer(spells_pow, 'multiply')}")
        print(f"Max: {spell_reducer(spells_pow, 'max')}")
    except Exception as e:
        print(e)

    print("\nTesting partial enchanter...")
    try:
        magic_book: dict[str, Callable] = partial_enchanter(base)
        fire_spell: Callable = magic_book["fire"]
        freeze_spell: Callable = magic_book["freeze"]
        poison_spell: Callable = magic_book["poison"]

        print(fire_spell(target="goblin"))
        print(freeze_spell(target="dragon"))
        print(poison_spell(target="zombie"))
    except Exception as e:
        print(e)

    print("\nTesting memoized fibonacci...")
    try:
        print(f"Fib(0): {memoized_fibonacci(0)}")
        print(f"Fib(1): {memoized_fibonacci(1)}")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")
    except Exception as e:
        print(e)

    print("\nTesting spell dispatcher...")
    dispatcher: Callable = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    spells: list[str] = ["1", "2", "3"]
    print(dispatcher(spells))
    print(dispatcher({"key": "value"}))
