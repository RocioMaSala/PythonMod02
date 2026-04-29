#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if 0 <= temp <= 40:
        return temp
    elif temp > 40:
        raise ValueError(f"{temp}ºC is too hot for plants (max 40ºC)")
    else:
        raise ValueError(f"{temp}ºC is too cold for plants (min 0ºC)")


def test_temperature() -> None:
    for test in ["25", "abc", "100", "-50"]:
        print(f"Input data is '{test}'")
        try:
            temp = input_temperature(test)
            print(f"Temperature is now {temp}ºC\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")


if __name__ == "__main__":

    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
