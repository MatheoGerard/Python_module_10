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


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Spell must be callable")

    def combined(*args) -> tuple[str, str]:
        return (spell1(*args), spell2(*args))

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
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


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition):
        raise TypeError("Condition must be callable")
    if not callable(spell):
        raise TypeError("Spell must be callable")

    def casters(*args) -> str:
        if condition(args[1]):
            return spell(*args)
        return "Spell fizzled"

    return casters


def spell_sequence(spells: list[Callable]) -> Callable:
    for spell in spells:
        if not callable(spell):
            raise TypeError("All spells must be callable")

    def sequence(*args) -> list[str]:
        spell_list: list[str] = []
        for x in spells:
            spell_list.append(x(*args))
        return spell_list

    return sequence


if __name__ == "__main__":
    print("Testing spell combiner...")
    try:
        combiner: Callable = spell_combiner(poison, fire)
        combined_spell: tuple[str, str] = combiner("Dragon", 67)
        print(
            f"Combined spell result: {combined_spell[0]}, {combined_spell[1]}"
        )
    except Exception as e:
        print(e)

    print("\nTesting power amplifier...")
    try:
        amplifier: Callable = power_amplifier(fire, 9)
        print(amplifier("goblin", 90))
    except Exception as e:
        print(e)

    print("\nTesting conditional caster...")
    try:
        caster: Callable = conditional_caster(condition_test, freeze)
        print(caster("goblin", 3))
    except Exception as e:
        print(e)

    print("\nTesting spell sequence...")
    try:
        spell_list: list[Callable] = [poison, fire, freeze, heal]
        sequencer: Callable = spell_sequence(spell_list)
        sequence: list[str] = sequencer("zombies", 54)
        for x in sequence:
            print(x)
    except Exception as e:
        print(e)
