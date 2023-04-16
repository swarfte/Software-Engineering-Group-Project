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
    """
    the modern calculator can calculate the trigonometric function
    """
    def __init__(self):
        self.expression = ""
        self.answer = ""
        self.isreplace = False  # 可替身狀態 new
        self.symbolholder = ""  # 儲存上一個輸入的symbol
        self.clear_mode= True
        self.left_bracket_count = 0

        # the trigonometric function that will dynamically generate by the trigonometric_function_setup() method
        self.trigonometric_function = [
            "sin",
            "cos",
            "tan",
            "sec",
            "csc",
            "cot",
        ]

        # the symbol that will replace the human-readable symbol when the eval() method is executed
        self.replace_map = {
            "^": "**",
            "x": "*"
        }

        self.trigonometric_function_setup()

    def update_expression(self, value: str) -> None:
        """
        the method is used to update the expression
        """
        self.clear_mode = False
        self.symbolholder = value
        self.replaceSymbol(True)
        if value == ".e+":
            self.answer = str(self.answer) + value + "0"
            self.isreplace = True
        elif str(self.expression) == "0" or self.isreplace:
            self.expression = str(self.answer) + value
            self.isreplace = False
        elif value == "(":
            self.expression = str(self.answer) + "x("
            self.left_bracket_count += 1
            self.isreplace = False
        else:
            self.expression = self.expression + str(self.answer) + value

        def calculate_expression(self) -> None:
            try:
                if self.symbolholder in {".e+", "("}:
                    result = self.answer
                else:
                    result = str(eval(str(self.expression[:-1])))
                return result
            except Exception:
                return "Error"
        
        self.replaceSymbol(True)
        self.answer = calculate_expression(self)
        self.replaceSymbol(False)
        self.isreplace = True

    def update_answer(self, value: str) -> None:
        """
        the method is used to update the answer
        """
        self.clear_mode = False
        if self.symbolholder == ".e+" and self.isreplace:
            self.answer = str(self.answer[:-1]) + value
        elif self.symbolholder == "=" and self.isreplace:
            self.answer = value
        elif str(self.answer) == "Error" or str(self.answer) == "0" or self.isreplace and value != ".":
            self.answer = value
        else:
            self.answer = str(self.answer) + value
        self.isreplace = False

    def pre_replace_expression(func):
        """ if the method include the eval() method, it must use this decorator"""

        def wrapper(self):
            # replace the symbol so that python eval() can process
            temp_expression = self.expression[:]
            self.replaceSymbol(True)

            # execute the method
            func(self)

            # replace the symbol back to the human-readable symbol
            self.expression = temp_expression

        return wrapper

    def trigonometric_function_setup(self):
        """
        the method is used to dynamically generate the trigonometric function
        """
        for index in range(len(self.trigonometric_function)):

            def make_dynamic_function(i):
                """
                according to the index to build the different trigonometric function
                """
                def dynamic_function():
                    """
                    the content of the instance of the trigonometric function
                    """
                    temp_expression = self.answer[:]
                    for key, value in self.replace_map.items():
                        if key in self.expression:
                            self.expression = self.expression.replace(key, value)

                    degrees = float(eval(str(self.answer)))
                    radians = math.radians(degrees)
                    if i < 3:
                        angle = eval(f"math.{self.trigonometric_function[i]}(radians)")
                    else:
                        angle = eval(f"1/math.{self.trigonometric_function[i - 3]}(radians)")
                    self.answer = str(angle)
                    self.expression = temp_expression

                return dynamic_function

            setattr(self, f"get_{self.trigonometric_function[index]}", make_dynamic_function(index))

    def calculate_expression(self) -> None:
        """
        this method is used to calculate the expression from the view
        """
        self.replaceSymbol(True)
        try:
            if self.expression and str(self.expression[-1]) in {"+", "-", "*", "/", "%"}:
                self.expression = str(self.expression) + str(self.answer)
            elif not self.expression and self.symbolholder == "=":
                self.expression = self.answer
            else:
                last = 0
                for symbol in {"+", "-", "*", "/", "%"}:
                    if str(self.expression).rfind(symbol) > last:
                        last = str(self.expression).rfind(symbol)
                self.expression = str(self.answer) + str(self.expression[last:])

            def calculate_expression(self) -> None:
                try:
                    result = str(eval(str(self.expression)))
                    return result
                except Exception:
                    return "Error"
            
            self.answer = calculate_expression(self)
            self.replaceSymbol(False)
            if self.symbolholder == ".e+":
                self.expression = self.answer
            
            self.symbolholder = "="
            self.isreplace = True

        except Exception as e:
            self.answer = "Error"

    def clear_output(self) -> None:
        """
        this method is used to clear the output
        """
        if not self.clear_mode:
            self.expression = ""
        self.answer = "0"
        self.clear_mode = True

    def get_reciprocal(self) -> None:
        """
        this method is used to get the reciprocal of the answer
        """
        if self.expression:
            self.expression = "1/" + "(" + str(self.expression) + ")"
        else:
            self.expression = "1/" + "(" + str(self.answer) + ")"

        # replace the symbol so that python eval() can process
        temp_expression = self.expression[:]
        for key, value in self.replace_map.items():
            if key in self.expression:
                self.expression = self.expression.replace(key, value)

        # replace the symbol back to the human-readable symbol
        self.answer = float(eval(temp_expression))
        self.isreplace = True

    @pre_replace_expression
    def get_10power(self) -> None:
        """
        this method is used to get the 10 power of the answer
        """
        self.answer = 10 ** float(eval(str(self.answer)))

    def delete_answer(self) -> None:
        """
        this method is used to delete the last digit of the answer
        """
        self.answer = self.answer[0:len(str(self.expression)) - 1]

    @pre_replace_expression
    def get_factorial(self) -> None:  # 階乘
        """
        this method is used to get the factorial of the answer
        """
        factorial = 1
        expression = eval(str(self.answer))
        if int(expression) < 0:
            self.answer = "Error"
        elif int(expression) == 0:
            self.answer = "1"
        else:
            for i in range(1, int(expression) + 1):
                factorial = factorial * i
            self.answer = factorial

    def get_pi(self) -> None:
        """
        this method is used to get the pi
        """
        self.answer = math.pi

    def get_e(self) -> None:
        """
        this method is used to get the e
        """
        self.answer = math.e

    @pre_replace_expression
    def get_log10(self) -> None:
        """
        this method is used to get the log base 10 of the answer
        """
        self.answer = math.log10(float(eval(str(self.answer))))

    @pre_replace_expression
    def get_logln(self) -> None:
        """
        this method is used to get the log base e of the answer
        """
        self.answer = math.log(float(eval(str(self.answer))))

    def set_minus(self) -> None:  # 有更改
        """
        this method is used to set the minus
        """
        expression = float(self.answer)
        if expression > 0:
            self.answer = "-" + str(expression)
        else:
            self.answer = str(abs(expression))

    @pre_replace_expression
    def get_abs(self) -> None:
        """
        this method is used to get the absolute value of the answer
        """
        self.answer = abs(int(eval(self.answer)))

    @pre_replace_expression
    def get_sqrea(self) -> None:
        self.answer = str(math.pow(float(eval(self.answer)), 2))
        self.isreplace = True

    @pre_replace_expression
    def get_root(self) -> None:
        self.answer = str(math.sqrt(float(eval(self.answer))))
        self.isreplace = False

    def replaceSymbol(self, state:bool) -> None:
        """
        this method is used to replace the Symbols
        True is for ccalculate
        False is for human readable
        """
        for key, value in self.replace_map.items():
            #if key in self.expression:
                if state:
                    self.expression = self.expression.replace(key, value)
                else:
                    self.expression = self.expression.replace(value, key)
    
        