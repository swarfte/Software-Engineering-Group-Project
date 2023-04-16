class AbstractController(object):
    def __init__(self, model, view):
        pass

    def update_expression(self, value: str):
        pass

    def calculate_expression(self):
        pass

    def clear_expression(self):
        pass


class BaseController(AbstractController):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.create_button("C", 4, 2, command=self.clear_expression)
        self.view.create_button(
            "=", 5, 0, 1, 4, command=self.calculate_expression)
        self.view.create_button(
            "+", 4, 3, command=lambda: self.update_expression("+"))
        self.view.create_button(
            "-", 3, 3, command=lambda: self.update_expression("-"))
        self.view.create_button(
            "*", 2, 3, command=lambda: self.update_expression("*"))
        self.view.create_button(
            "/", 1, 3, command=lambda: self.update_expression("/"))
        self.view.create_button(
            ".", 4, 1, command=lambda: self.update_expression("."))
        self.view.create_button(
            "0", 4, 0, command=lambda: self.update_expression("0"))
        self.view.create_button(
            "1", 3, 0, command=lambda: self.update_expression("1"))
        self.view.create_button(
            "2", 3, 1, command=lambda: self.update_expression("2"))
        self.view.create_button(
            "3", 3, 2, command=lambda: self.update_expression("3"))
        self.view.create_button(
            "4", 2, 0, command=lambda: self.update_expression("4"))
        self.view.create_button(
            "5", 2, 1, command=lambda: self.update_expression("5"))
        self.view.create_button(
            "6", 2, 2, command=lambda: self.update_expression("6"))
        self.view.create_button(
            "7", 1, 0, command=lambda: self.update_expression("7"))
        self.view.create_button(
            "8", 1, 1, command=lambda: self.update_expression("8"))
        self.view.create_button(
            "9", 1, 2, command=lambda: self.update_expression("9"))

    def update_expression(self, value: str) -> None:
        self.model.update_expression(value)
        self.view.set_output(self.model.expression)

    def calculate_expression(self) -> None:
        self.model.calculate_expression()
        self.view.set_output(self.model.expression)

    def clear_expression(self) -> None:
        self.model.clear_expression()
        self.view.set_output(self.model.expression)


class AdvanceController(AbstractController):
    """
    the modern calculator has a lot of function, so I use a list to store the function
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.button_list = []
        self.command = [
            self.generic_answer_output("get_sin"),
            self.generic_answer_output("get_cos"),
            self.generic_answer_output("get_tan"),
            self.generic_answer_output("get_sec"),
            self.generic_answer_output("get_csc"),
            self.generic_answer_output("get_cot"),
            self.generic_expression_output("get_pi"),  # pi
            self.generic_expression_output("get_e"),
            self.generic_refresh_output("clear_output"),  # C => 清除輸入
            self.generic_answer_output("delete_answer"),  # 改成刪減答案     #有更改
            self.generic_answer_output("get_sqrea"),
            self.generic_expression_output("get_reciprocal"),  # 1/x  => 倒數   #有更改
            self.generic_answer_output("get_abs"),
            self.generic_symbol(".e+"),  # exp => 科學計數法
            self.generic_symbol("%"),
            self.generic_answer_output("get_root"),  # root 2 => **0.5
            self.generic_symbol("("),
            self.generic_symbol(")"),
            self.generic_answer_output("get_factorial"),  # 階乘 x!
            self.generic_symbol("/"),
            self.generic_symbol("^"),
            self.generic_symbol_num("7"),       #有更改
            self.generic_symbol_num("8"),       #有更改
            self.generic_symbol_num("9"),       #有更改
            self.generic_symbol("x"),
            self.generic_expression_output("get_10power"),  # 10的N次方
            self.generic_symbol_num("4"),       #有更改
            self.generic_symbol_num("5"),       #有更改
            self.generic_symbol_num("6"),       #有更改
            self.generic_symbol("-"),
            self.generic_answer_output("get_log10"),
            self.generic_symbol_num("1"),       #有更改
            self.generic_symbol_num("2"),       #有更改
            self.generic_symbol_num("3"),       #有更改
            self.generic_symbol("+"),
            self.generic_answer_output("get_logln"),  # ln
            self.generic_expression_output("set_minus"),  # +/-
            self.generic_symbol_num("0"),       #有更改
            self.generic_symbol_num("."),       #有更改
            self.generic_answer_output("calculate_expression")  # "=" => 計算結果       #有更改
        ]

        self.setup()
        self.default_action()

    def default_action(self):
        """
        set what action should be done when the calculator is first opened
        """
        self.generic_symbol_num("0")()

    def setup(self):
        """
        to build the button and bind the command to the corresponding button
        """
        symbol = self.view.symbol
        # we split the button to 5 columns
        column_size = 5

        # we have 2 entries , so remap two row for the entries
        remain_row = 2
        for row in range(remain_row, len(symbol) // column_size + remain_row):
            for column in range(column_size):
                index = (row - remain_row) * column_size + column
                self.button_list.append(self.view.create_button(
                    symbol[index],
                    row,
                    column,
                    command=self.command[index],
                    bootstyle=self.set_button_color(self.command[index].__name__)
                ))

    def set_button_color(self, button_name: str) -> str:
        """
        based on the button name, set the button color
        """
        if button_name == "answer_action":
            return "info"
        elif button_name == "expression_action":
            return "success"
        elif button_name == "refresh_action":
            return "danger"
        else:
            return "dark"


    def update_expression(self, value: str) -> None:
        """
        update the expression entry
        """
        self.model.update_expression(value)
        self.view.set_expression_output(self.model.expression)
        self.view.set_answer_output(self.model.answer)

    def update_answer(self, value: str) -> None:
        """
        update the answer entry
        """
        self.model.update_answer(value)
        self.view.set_answer_output(self.model.answer)
        self.view.set_clear_button(self.button_list[8], self.model.clear_mode)

    def generic_answer_output(self, model_func: str):
        """
        a generic function to bind the model function to the button
        """
        def answer_action():
            exec(f"self.model.{model_func}()")
            self.view.set_answer_output(self.model.answer)
            self.view.set_expression_output(self.model.expression)

        return answer_action

    def generic_expression_output(self, model_func: str):
        """
        a generic function to bind the model function to the button
        """
        def expression_action():
            exec(f"self.model.{model_func}()")
            self.view.set_answer_output(self.model.answer)
            self.view.set_expression_output(self.model.expression)

        return expression_action

    def generic_symbol(self, symbol: str):
        """
        a generic function to bind the symbol to the button
        """
        def symbol_action():
            self.update_expression(symbol)

        return symbol_action

    def generic_symbol_num(self, symbol: str):
        """
        similar to generic_symbol, but for number is updated to the answer
        """
        def symbol_action():
            if self.model.symbolholder == "=":
                self.view.set_expression_output("")
            self.update_answer(symbol)

        return symbol_action

    def generic_refresh_output(self, model_func: str):
        """
        a generic function to bind the model function to the button, and it will update the expression and answer
        """
        def refresh_action():
            exec(f"self.model.{model_func}()")
            self.refresh()

        return refresh_action

    def refresh(self):
        """
        update the expression and answer
        """
        self.view.set_expression_output(self.model.expression)
        self.view.set_answer_output(self.model.answer)
        self.view.set_clear_button(self.button_list[8], self.model.clear_mode)