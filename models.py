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
        self.answer = ""
        self.trigonometric_function = [
            "sin",
            "cos",
            "tan",
            "sec",
            "csc",
            "cot",
        ]

        self.replace_map = {
            "^": "**",
            "x": "*"
        }

        self.trigonometric_function_setup()



    def update_expression(self, value: str) -> None:
        if str(self.expression) == "Error":
            self.expression = value
        else:
            self.expression = str(self.expression) + value

    def pre_replace_expression(func):
        """ if the method include the eval() method, it must use this decorator"""
        def wrapper(self):
            # replace the symbol so that python eval() can process
            temp_expression = self.expression[:]
            for key, value in self.replace_map.items():
                if key in self.expression:
                    self.expression = self.expression.replace(key, value)

            # execute the method
            func(self)

            # replace the symbol back to the human-readable symbol
            self.expression = temp_expression
        return wrapper
    def trigonometric_function_setup(self):
        for index in range(len(self.trigonometric_function)):

            def make_dynamic_function(i):
                def dynamic_function():
                    temp_expression = self.expression[:]
                    for key, value in self.replace_map.items():
                        if key in self.expression:
                            self.expression = self.expression.replace(key, value)

                    degrees = eval(self.expression)
                    radians = math.radians(degrees)
                    if i < 3:
                        angle = eval(f"math.{self.trigonometric_function[i]}(radians)")
                    else:
                        angle = eval(f"1/math.{self.trigonometric_function[i - 3]}(radians)")
                    self.answer = str(angle)
                    self.expression = temp_expression

                return dynamic_function

            setattr(self, f"get_{self.trigonometric_function[index]}", make_dynamic_function(index))

    @pre_replace_expression
    def calculate_expression(self) -> None:
        try:
            result = str(eval(str(self.expression)))
            self.answer = result
        except Exception as e:
            self.answer = "Error"

    def clear_output(self) -> None:
        self.expression = "0"
        self.answer = ""

    def get_reciprocal(self) -> None:
        self.expression = "1/" + str(self.expression)
        #self.answer = float(eval(self.expression))

            # replace the symbol so that python eval() can process
        temp_expression = self.expression[:]
        for key, value in self.replace_map.items():
            if key in self.expression:
                self.expression = self.expression.replace(key, value)

        # replace the symbol back to the human-readable symbol
        self.answer = float(eval(temp_expression))
        

    @pre_replace_expression
    def get_10power(self) -> None:
        self.answer = 10 ** float(eval(self.expression))

    def delete_expression(self) -> None:
        self.expression = self.expression[0:len(str(self.expression)) - 1]

    @pre_replace_expression
    def get_factorial(self) -> None:  # 階乘
        factorial = 1
        expression = eval(self.expression)
        if int(expression) < 0:
            self.answer = "Error"
        elif int(expression) == 0:
            self.answer = "1"
        else:
            for i in range(1, int(expression) + 1):
                factorial = factorial * i
            self.answer = factorial

    def get_pi(self) -> None:
        self.expression = math.pi

    def get_e(self) -> None:
        self.expression = math.e

    @pre_replace_expression
    def get_log10(self) -> None:
        self.answer = math.log10(float(eval(self.expression)))

    @pre_replace_expression
    def get_logln(self) -> None:
        self.answer = math.log(float(eval(self.expression)))



    def set_minus(self) -> None:
        expression = float(self.expression)
        if expression > 0:
            self.expression = "-" + str(expression)
        else:
            self.expression = str(abs(expression))

    @pre_replace_expression
    def get_abs(self) -> None:
        self.answer = abs(float(eval(self.expression)))
