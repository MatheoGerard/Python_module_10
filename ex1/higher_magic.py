from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fire(target: str, power: int) -> str:
    return f"Fire do {power} damage to {target}"


def freeze(target: str, power: int) -> str:
    return f"Freeze do {power} damage to {target}"


def lighting(target: str, power: int) -> str:
    return f"Lighting do {power} damage to {target}"


def poison(target: str, power: int) -> str:
    return f"Poison do {power} damage to {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args) -> tuple[str, str]:
        return (spell1(*args), spell2(*args))

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def condition_test(state: bool) -> bool:
    if state:
        return True
    return False


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def casters(*args) -> str:
        if condition(*args):
            return spell(*args)
        return "Spell fizzled"


if __name__ == "__main__":
    function: Callable = spell_combiner(fire, freeze)
    print(function("chips", 4))

    function2: Callable = power_amplifier(lighting, 3)
    print(function2("chips", 6))
