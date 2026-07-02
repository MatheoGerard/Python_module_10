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
    return f"Launch a {element} sort and do {power} damage to {target}!"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, power=50, element="fire"),
        "freeze": partial(base_enchantment, power=50, element="freeze"),
        "poison": partial(base_enchantment, power=50, element="poison"),
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
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
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    print(memoized_fibonacci(0))
    print(memoized_fibonacci.cache_info())
    print(memoized_fibonacci(1))
    print(memoized_fibonacci.cache_info())
    print(memoized_fibonacci(10))
    print(memoized_fibonacci.cache_info())
    print(memoized_fibonacci(15))
    print(memoized_fibonacci.cache_info())
    print(memoized_fibonacci(15))
    print(memoized_fibonacci.cache_info())
