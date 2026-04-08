def input_temperature(temp_str: str) -> int:
    return int(temp_str)

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
    print("All tests completed - program didn't crash!")