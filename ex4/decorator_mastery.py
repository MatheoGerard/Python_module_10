from collections.abc import Callable
from functools import wraps
import time


def fire() -> str:
    time.sleep(0.1)
    return "Fireball cast"


def spell_timer(func: Callable) -> Callable:
    if not callable(func):
        raise TypeError("func must be callable")

    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        print(f"Casting {func.__name__}...")
        start: float = time.time()
        res: str = func(*args, **kwargs)
        end: float = time.time()
        print(f"Spell completed in {round(end - start, 3)} seconds")
        return res

    return wrapper


def power_validator(min_power: int) -> Callable:
    if not isinstance(min_power, int):
        raise TypeError("min_power must be an int")

    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            power: int = args[0]
            if power < min_power:
                return "Insufficient power for this spell"
            else:
                return func(*args, **kwargs)

        return wrapper

    return deco


def test(n: int) -> str:
    if n != 2:
        raise ValueError("RATER")
    else:
        return f"Pass in {n} try"


def retry_spell(max_attempts: int) -> Callable:
    def deco(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            for x in range(0, max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... (attempt {x + 1}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return deco


class MageGuild:
    @staticmethod
    def validate_mage_name(name) -> bool:
        # TODO: Check if the conditions for the name is respected
        pass


if __name__ == "__main__":
    print("Testing spell timer...")
    try:
        wrap: Callable = spell_timer(fire)
        return_str: str = wrap()
        print(f"Result: {return_str}!")
    except Exception as e:
        print(e)
