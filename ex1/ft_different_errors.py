def garden_operations() -> None:
    """
    """
    try:
        print("Testing ValueError...")
        int("abc")
    except (ValueError):
        print("Caught ValueError: invalid literal for int()")
    try:
        print("\nTesting ValueError...")
        10/0
    except (ZeroDivisionError):
        print("Caught ZeroDivisionError: division by zero")
    try:
        print("\nTesting ValueError...")
        open("file.txt", "r")
    except (FileNotFoundError):
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    try:
        print("\nTesting ValueError...")
        fruit = {"name": "apple", "color": "red"}
        print(fruit["apple"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")


def test_error_types() -> None:
    """
    """
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("\nTesting multiple errors together...")
    try:
        10/0
    except (ValueError, ZeroDivisionError,
            FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
