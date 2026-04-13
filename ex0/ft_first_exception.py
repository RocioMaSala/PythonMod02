def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    for test in ["25", "abc"]:
        print(f"Input data is '{test}'")
        try:
            input_temperature(test)
            print(f"Temperature is now {input_temperature(test)}ºC\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")


if __name__ == "__main__":

    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
