# class_static_methods_demo.py

class Calculator:
    """
    A simple Calculator class to demonstrate the use of
    class methods and static methods in Python.
    """

    # Class attribute shared across all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method that adds two numbers.
        Does not depend on class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method that multiplies two numbers.
        Demonstrates access to the class attribute via 'cls'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
