#!/usr/bin/env python3

class GardenError (Exception):
    def __init__(self, e: str = "Unknown Garden Error") -> None:
        super().__init__(e)


class PlantError(GardenError):
    def __init__(self, e: str = "Unknown Plant Error") -> None:
        super().__init__(e)


class WaterError(GardenError):
    def __init__(self, e: str = "Unknown Water Error") -> None:
        super().__init__(e)


def checkplant() -> None:

    raise PlantError("The tomato plant is wilting!")


def checkwater() -> None:
    raise WaterError("Not enough water in the tank!")


def test_error_types() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        checkplant()
    except PlantError as e:
        print(f"Caught PlantError:{e}\n")
    try:
        print("Testing WaterError...")
        checkwater()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    try:
        print("Testing catching all garden errors...")
        checkplant()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        checkwater()
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    test_error_types()
    print()
    print("All error types tested successfully!")
