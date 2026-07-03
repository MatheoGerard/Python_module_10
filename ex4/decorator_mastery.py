from collections.abc import Callable
from functools import wraps
import time


def fire() -> str:
    time.sleep(0.1)
    return "Fireball cast"


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        print(f"Casting {func.__name__}...")
        start: float = time.time()
        res: str = func(*args, **kwargs)
        end: float = time.time()
        print(f"Spell completed in {round(end - start, 3)} seconds")
        return res

    return wrapper


if __name__ == "__main__":
    print("Testing spell timer...")
    wrap: Callable = spell_timer(fire)
    return_str: str = wrap()
    print(f"Result: {return_str}!")
