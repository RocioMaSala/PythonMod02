
def garden_operations(operation_number: int):
    print(f"Testing operation {operation_number}...")
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        2/0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        len(5)
    else:
        print("Operation completed successfully")

def test_error_types(): ## Me quedo aquí
    for operation_number in range (0, 5):
        try:
            garden_operations(operation_number)
        except Exception as e:
            if operation_number == 0: 
                raise ValueError(f"Caught ValueError: {e}") from e
            elif operation_number == 1: 
                raise ZeroDivisionError(f"Caught ZeroDivisionError: {e}") from e
            elif operation_number == 2: 
                raise FileNotFoundError(f"Caught FileNotFoundError: {e}") from e
            elif operation_number == 3: 
                raise TypeError(f"Caught TypeError: {e}") from e


if __name__ == "__main__":
    test_error_types()