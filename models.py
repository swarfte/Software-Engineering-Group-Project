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
        for i in range(len(self.trigonometric_function)):
            def make_dynamic_function(func, index):
                def dynamic_function():
                    exec(f"""
angle_in_degrees = float({self.expression})
angle_in_radians = math.radians(angle_in_degrees)
if "{func[index]}" == "sin" or "{func[index]}" == "cos" or "{func[index]}" == "tan":
    {func[index]}_angle = math.{func[index]}(angle_in_radians)
else:
    {func[index]}_angle = 1/math.{func[index-3]}(angle_in_radians)
self.expression = str({func[index]}_angle)""")
                return dynamic_function
            setattr(self, f"{self.trigonometric_function[i]}_expression", make_dynamic_function(
                self.trigonometric_function, i))

    def update_expression(self, value: str) -> None:
        if str(self.expression) == "Error":
            self.expression = value
        else:
            self.expression = str(self.expression) + value

    def calculate_expression(self) -> None:
        try:
            result = str(eval(str(self.expression)))
            self.expression = result
        except:
            self.expression = "Error"

    def clear_expression(self) -> None:
        self.expression = ""

    def get_reciprocal(self) -> None:
        self.expression = "1/" + str(self.expression)

    def get_10power(self) -> None:
        self.expression = "10**" + str(self.expression)

    def delete_expression(self) -> None:
        self.expression = self.expression[0:len(str(self.expression))-1]

    def get_factorial(self) -> None:  # 階乘
        factorial = 1
        if int(self.expression) < 0:
            self.expression = "Error"
        elif int(self.expression) == 0:
            self.expression = "1"
        else:
            for i in range(1, int(self.expression) + 1):
                factorial = factorial*i
            self.expression = factorial

    def get_pi(self) -> None:
        self.expression = math.pi

    def get_e(self) -> None:
        self.expression = math.e

    def get_log10(self) -> None:
        self.expression = math.log10(int(self.expression))

    def get_logln(self) -> None:
        self.expression = math.log(int(self.expression))

    def set_minus(self) -> None:
        if int(self.expression) > 0:
            self.expression = "-" + str(self.expression)
        else:
            self.expression = abs(int(self.expression))

    def get_abs(self) -> None:
        self.expression = abs(int(self.expression))
