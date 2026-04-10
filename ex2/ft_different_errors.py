def garden_operations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        2/0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "hello" + 5
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    for operation_number in range(0, 5):
        try:
            garden_operations(operation_number)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")


if __name__ == "__main__":
    test_error_types()
    print()
    print("All error types tested successfully!")
