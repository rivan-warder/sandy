# main.py
# This is the main entry point for the sandy application.
# It imports the math module and uses its functions.
from my_math import subtract
from core import SimpleClass


def main():
    print("Hello from sandy!")

    simple_instance = SimpleClass(name="Sandy", value=10, email="jack@famous.com")
    print(simple_instance.greet())
    print(f"Initial value: {simple_instance.value}")
    print(f"Incremented value: {simple_instance.increment_value()}")
    print(f"Value after adding 5: {simple_instance.add_to_value(5)}")
    print(f"Value after subtracting 3: {subtract(simple_instance.value, 3)}")


if __name__ == "__main__":
    main()
