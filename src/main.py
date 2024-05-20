from typing import Union


class A:
    x = 1


class Calculator:
    def divide(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both parameters should be numeric")
        if y == 0:
            raise ZeroDivisionError("Division by zero")
        return x / y

    def add(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both parameters should be numeric")
        return x + y


if __name__ == '__main__':
    calculator = Calculator()
    print(calculator.divide(10, 2))
    print(calculator.add(10, 5))
