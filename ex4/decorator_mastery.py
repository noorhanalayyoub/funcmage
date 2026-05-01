from typing import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        returned_value = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return returned_value

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) > 2:
                power = args[2]
            else:
                kwargs.get("power")
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i < max_attempts:
                        print("Spell failed, retrying... "
                              f"(attempt {i}/{max_attempts})")
                    if i == max_attempts:
                        return ("Spell casting failed after"
                                f"{max_attempts} attempts")

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            if all(c.isalpha() or c.isspace() for c in name):
                return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    @spell_timer
    def fireball() -> str:
        time.sleep(0.4)
        return "Fireball cast!"

    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise RuntimeError("Spell backfired!")

    print(unstable_spell())

    @retry_spell(max_attempts=3)
    def lucky_spell() -> str:
        return "Waaaaaaagh spelled !"

    print(lucky_spell())

    print("\nTesting MageGuild...")
    guild10 = MageGuild()
    print(guild10.validate_mage_name("ValidMage"))
    print(guild10.validate_mage_name("AB"))
    print(guild10.cast_spell("Lightning", 15))
    print(guild10.cast_spell("Fireball", 5))
