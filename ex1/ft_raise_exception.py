def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if 0 <= temp <= 40:
        return temp
    elif temp > 40:
        raise ValueError(f"{temp}ºC is too hot for plants (max 40ºC)")
    else:
        raise ValueError(f"{temp}ºC is too cold for plants (min 0ºC)")


def test_temperature(test) -> None:
    print(f"Input data is '{test}'")
    try:
        input_temperature(test)
        print(f"Temperature is now {input_temperature(test)}ºC")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":

    print("=== Garden Temperature ===\n")
    test_temperature("25")
    print()
    test_temperature("abc")
    print()
    test_temperature("100")
    print()
    test_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")
