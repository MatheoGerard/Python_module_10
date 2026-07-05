from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    if not isinstance(initial_power, int):
        raise TypeError("Initial_power must be an int")
    power: int = initial_power

    def accumulator(boost: int) -> int:
        if not isinstance(boost, int):
            raise TypeError("boost must be an int")
        nonlocal power
        power += boost
        return power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    if not isinstance(enchantment_type, str):
        raise TypeError("enchantment_type must be a str")
    type_to_apply: str = enchantment_type

    def enchantment(item_name: str) -> str:
        if not isinstance(item_name, str):
            raise TypeError("item_name must be a str")
        return f"{type_to_apply} {item_name}"

    return enchantment


def memory_vault() -> (
    dict[str, Callable[[str, Any], None] | Callable[[str], Any]]
):
    storage: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        if not isinstance(key, str):
            raise TypeError("key must be a str")
        storage.update({key: value})

    def recall(key: str) -> Any:
        if not isinstance(key, str):
            raise TypeError("key must be a str")
        if key in storage.keys():
            return storage[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter: Callable[[], int] = mage_counter()
    print(f"counter_a call 1: {counter()}")
    print(f"counter_a call 2: {counter()}")
    print(f"counter_a call 3: {counter()}")
    print(f"counter_a call 4: {counter()}")

    print("\nTesting spell accumulator...")
    try:
        base_value: int = 100
        accumulator: Callable[[int], int] = spell_accumulator(base_value)
        print(f"Base {base_value}, add 20: {accumulator(20)}")
        print(f"Base {base_value}, add 30: {accumulator(30)}")
    except Exception as e:
        print(e)

    print("\nTesting enchantment factory...")
    try:
        factory_fire: Callable[[str], str] = enchantment_factory("Fire")
        print(factory_fire("sword"))
        factory_freeze: Callable[[str], str] = enchantment_factory("freeze")
        print(factory_freeze("shield"))
    except Exception as e:
        print(e)

    print("\nTesting memory vault...")
    try:
        vault: dict[str, Any] = memory_vault()
        print("Store 'secret' = 42")
        vault["store"]("secret", 42)
        print("Recall 'secret':", vault["recall"]("secret"))
        print("Recall 'unknown':", vault["recall"]("unknown"))
    except Exception as e:
        print(e)
