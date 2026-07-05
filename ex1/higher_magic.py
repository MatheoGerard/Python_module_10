from collections.abc import Callable


def heal(target: str, power: int) -> str:
    if not isinstance(target, str):
        raise TypeError("Target must be a str")
    if not isinstance(power, int):
        raise TypeError("Power must be an int")
    return f"Heal restores {target} for {power} HP"


def fire(target: str, power: int) -> str:
    if not isinstance(target, str):
        raise TypeError("Target must be a str")
    if not isinstance(power, int):
        raise TypeError("Power must be an int")
    return f"Fire do {power} damage to {target}"


def freeze(target: str, power: int) -> str:
    if not isinstance(target, str):
        raise TypeError("Target must be a str")
    if not isinstance(power, int):
        raise TypeError("Power must be an int")
    return f"Freeze do {power} damage to {target}"


def lighting(target: str, power: int) -> str:
    if not isinstance(target, str):
        raise TypeError("Target must be a str")
    if not isinstance(power, int):
        raise TypeError("Power must be an int")
    return f"Lighting do {power} damage to {target}"


def poison(target: str, power: int) -> str:
    if not isinstance(target, str):
        raise TypeError("Target must be a str")
    if not isinstance(power, int):
        raise TypeError("Power must be an int")
    return f"Poison do {power} damage to {target}"


def spell_combiner(
    spell1: Callable[[str, int], str], spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Spell must be callable")

    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str], multiplier: int
) -> Callable[[str, int], str]:
    if not callable(base_spell):
        raise TypeError("Base_spell must be callable")
    if not isinstance(multiplier, int):
        raise TypeError("Multiplier must be an int")

    def amplified(target: str, power: int) -> str:
        if not isinstance(target, str):
            raise TypeError("Traget must be a str")
        if not isinstance(power, int):
            raise TypeError("Power must be an int")
        return base_spell(target, power * multiplier)

    return amplified


def condition_test(power: int) -> bool:
    if not isinstance(power, int):
        raise TypeError("Power must be an int")
    if power >= 5:
        return True
    return False


def conditional_caster(
    condition: Callable[[int], bool], spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    if not callable(condition):
        raise TypeError("Condition must be callable")
    if not callable(spell):
        raise TypeError("Spell must be callable")

    def casters(target: str, power: int) -> str:
        if condition(power):
            return spell(target, power)
        return "Spell fizzled"

    return casters


def spell_sequence(
    spells: list[Callable[[str, int], str]],
) -> Callable[[str, int], list[str]]:
    for spell in spells:
        if not callable(spell):
            raise TypeError("All spells must be callable")

    def sequence(target: str, power: int) -> list[str]:
        spell_list: list[str] = []
        for x in spells:
            spell_list.append(x(target, power))
        return spell_list

    return sequence


if __name__ == "__main__":
    print("Testing spell combiner...")
    try:
        combiner: Callable[[str, int], tuple[str, str]] = spell_combiner(
            poison, fire
        )
        combined_spell: tuple[str, str] = combiner("Dragon", 67)
        print(
            f"Combined spell result: > Callable{combined_spell[0]}, "
            f"{combined_spell[1]}"
        )
    except Exception as e:
        print(e)

    print("\nTesting power amplifier...")
    try:
        amplifier: Callable[[str, int], str] = power_amplifier(fire, 9)
        print(amplifier("goblin", 90))
    except Exception as e:
        print(e)

    print("\nTesting conditional caster...")
    try:
        caster: Callable[[str, int], str] = conditional_caster(
            condition_test, freeze
        )
        print(caster("goblin", 3))
    except Exception as e:
        print(e)

    print("\nTesting spell sequence...")
    try:
        spell_list: list[Callable[[str, int], str]] = [
            poison,
            fire,
            freeze,
            heal,
        ]
        sequencer: Callable[[str, int], list[str]] = spell_sequence(spell_list)
        sequence: list[str] = sequencer("zombies", 54)
        for x in sequence:
            print(x)
    except Exception as e:
        print(e)
