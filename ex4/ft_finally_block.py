class GardenError (Exception):
    def __init__(self, e: str = "Unknown Garden Error") -> None:
        super().__init__(e)


class PlantError(GardenError):
    def __init__(self, e: str = "Unknown Plant Error") -> None:
        super().__init__(e)


def water_plant(plant_name: str) -> None:
    if plant_name[0].isupper():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("... ending tests and returning to main")
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("... ending tests and returning to main")
    finally:
        print("Closing watering system\n")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
