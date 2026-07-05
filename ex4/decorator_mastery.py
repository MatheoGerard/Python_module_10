from collections.abc import Callable
from functools import wraps
import time
from typing import TypeVar, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")


def spell_timer(func: Callable[P, R]) -> Callable[P, R]:
    if not callable(func):
        raise TypeError("func must be callable")

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Casting {func.__name__}...")
        start: float = time.time()
        res: R = func(*args, **kwargs)
        end: float = time.time()
        print(f"Spell completed in {round(end - start, 3)} seconds")
        return res

    return wrapper


@spell_timer
def fire() -> str:
    time.sleep(0.1)
    return "Fireball cast"


def power_validator(
    min_power: int,
) -> Callable[[Callable[P, R]], Callable[P, R | str]]:
    if not isinstance(min_power, int):
        raise TypeError("min_power must be an int")

    def deco(func: Callable[P, R]) -> Callable[P, R | str]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R | str:
            power: int | None = None

            if len(args) > 2:
                if isinstance(args[2], int):
                    power = args[2]
                else:
                    raise TypeError("power must be a int")

            if power is None:
                raise ValueError("power not found")

            if power < min_power:
                return "Insufficient power for this spell"
            else:
                return func(*args, **kwargs)

        return wrapper

    return deco


def retry_spell(
    max_attempts: int,
) -> Callable[[Callable[P, R]], Callable[P, R | str]]:
    def deco(func: Callable[P, R]) -> Callable[P, R | str]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R | str:
            for x in range(0, max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {x + 1}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return deco


def make_test() -> Callable[[], str]:
    n: int = 0

    @retry_spell(3)
    def test() -> str:
        nonlocal n
        n += 1

        if n != 3:
            raise ValueError("RATER")
        else:
            return f"Pass in {n} try"

    return test


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("mane must be a str")
        if len(name) < 3:
            return False
        for char in name:
            if not char.isalpha() and not char == " ":
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        if not isinstance(spell_name, str):
            raise TypeError("spell_name must be a str")
        if not isinstance(power, int):
            raise TypeError("power must be an int")

        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")
    try:
        wrap: Callable[[], str] = spell_timer(fire)
        return_str: str = wrap()
        print(f"Result: {return_str}!")
    except Exception as e:
        print(e)

    print("\nTesting retrying spell...")
    try:
        tester: Callable[[], str] = make_test()
        print(tester())
    except Exception as e:
        print(e)

    print("\nTesting MageGuild...")
    try:
        guild: MageGuild = MageGuild()
        print(guild.validate_mage_name("Arthur guild"))
        print(guild.validate_mage_name("Arthur guild 42"))
        print(guild.cast_spell("FireBall", 15))
        print(guild.cast_spell("FireBall", 8))
    except Exception as e:
        print(e)
