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


def condition_test(power: int) -> bool:
    if power >= 5:
        return True
    return False


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def casters(*args) -> str:
        if condition(args[1]):
            return spell(*args)
        return "Spell fizzled"

    return casters


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args) -> list[str]:
        spell_list: list[str] = []
        for x in spells:
            spell_list.append(x(*args))
        return spell_list

    return sequence
