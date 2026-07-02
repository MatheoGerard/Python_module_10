import operator as op
import functools as ft
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    if operation == "add":
        return ft.reduce(op.add, spells)
    elif operation == "multiply":
        return ft.reduce(op.mul, spells)
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
        "fire": ft.partial(base_enchantment, power=50, element="fire"),
        "freeze": ft.partial(base_enchantment, power=50, element="freeze"),
        "poison": ft.partial(base_enchantment, power=50, element="poison"),
    }


if __name__ == "__main__":
    try:
        spells: list[int] = [20, 5, 8, 2]
        print(spell_reducer(spells, "min"))
    except Exception as e:
        print(e)
