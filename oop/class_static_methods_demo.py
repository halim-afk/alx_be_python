class Calculator:
    """
    A class demonstrating the use of static and class methods in Python.
    It includes a static method for addition and a class method for multiplication
    that accesses a class attribute.
    """

    # Class attribute accessible by class methods
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method to perform addition.
        Static methods do not receive a reference to the class or instance.
        They are just functions conceptually belonging to the class's namespace.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method to perform multiplication.
        Class methods receive the class itself as the first argument (conventionally 'cls').
        This allows them to access or modify class-level attributes.

        Args:
            cls (type): The class itself (e.g., Calculator).
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The product of a and b.
        """
        # Accessing the class attribute 'calculation_type' using 'cls'
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

