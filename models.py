import math


class AbstractModel(object):
    """ Abstract Base classes """

    def __init__(self) -> None:
        pass

    def update_expression(self) -> None:
        pass

    def calculate_expression(self) -> None:
        pass

    def clear_expression(self) -> None:
        pass


class BaseModel(AbstractModel):
    """ base model class"""

    def __init__(self):
        self.expression = ""

    def update_expression(self, value: str) -> None:
        self.expression += value

    def calculate_expression(self) -> None:
        try:
            result = str(eval(self.expression))
            self.expression = result
        except:
            self.expression = "Error"

    def clear_expression(self) -> None:
        self.expression = ""


class AdvanceModel(AbstractModel):
    def __init__(self):
        self.expression = ""
        self.trigonometric_function = [
            "sin",
            "cos",
            "tan",
            "sec",
            "csc",
            "cot",
        ]

        self.trigonometric_function_setup()

    def trigonometric_function_setup(self):
        pass

    def update_expression(self, value: str) -> None:
        self.expression += value

    def calculate_expression(self) -> None:
        try:
            result = str(eval(self.expression))
            self.expression = result
        except:
            self.expression = "Error"

    def clear_expression(self) -> None:
        self.expression = ""

    def get_reciprocal(self) -> None:
        self.expression = "1/" + self.expression

    def delete_expression(self) -> None:
        self.expression = self.expression[0:len(self.expression)-1]

    def get_factorial(self) -> None:
        factorial = 1
        if int(self.expression) < 0:
            self.expression = "Error"
        elif int(self.expression) == 0:
            self.expression = "1"
        else:
            for i in range(1, int(self.expression) + 1):
                factorial = factorial*i
            self.expression = factorial

    # def sin_expression(self) -> None:
    #     angle_in_degrees = float(self.expression)
    #     angle_in_radians = math.radians(angle_in_degrees)
    #     sin_angle = math.sin(angle_in_radians)
    #     self.expression = str(sin_angle)
