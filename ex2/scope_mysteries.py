from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power: int = initial_power

    def accumulator(boost: int) -> int:
        nonlocal power
        power += boost
        return power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    type_to_apply: str = enchantment_type

    def enchantment(item_name: str) -> str:
        return f"{type_to_apply} {item_name}"

    return enchantment


def memory_vault() -> dict[str, Callable]:
    storage: dict[str, Callable] = {}

    def store(key: str, value: Any):
        storage.update({key: value})

    def recall(key: str):
        if key in storage.keys():
            return storage[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}
