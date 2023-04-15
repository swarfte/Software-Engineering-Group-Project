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
    def __init__(self, model, view):
        self.model = model
        self.view = view

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
            self.generic_expression_output("delete_expression"),
            self.generic_symbol("^2"),
            self.generic_answer_output("get_reciprocal"),  # 1/x  => 倒數
            self.generic_answer_output("get_abs"),
            self.generic_symbol(".e+"),  # exp => 科學計數法
            self.generic_symbol("%"),
            self.generic_symbol("^0.5"),  # root 2 => **0.5
            self.generic_symbol("("),
            self.generic_symbol(")"),
            self.generic_answer_output("get_factorial"),  # 階乘 x!
            self.generic_symbol("/"),
            self.generic_symbol("^"),
            self.generic_symbol("7"),
            self.generic_symbol("8"),
            self.generic_symbol("9"),
            self.generic_symbol("x"),
            self.generic_answer_output("get_10power"),  # 10的N次方
            self.generic_symbol("4"),
            self.generic_symbol("5"),
            self.generic_symbol("6"),
            self.generic_symbol("-"),
            self.generic_answer_output("get_log10"),
            self.generic_symbol("1"),
            self.generic_symbol("2"),
            self.generic_symbol("3"),
            self.generic_symbol("+"),
            self.generic_answer_output("get_logln"),  # ln
            self.generic_expression_output("set_minus"),  # +/-
            self.generic_symbol("0"),
            self.generic_symbol("."),
            self.generic_refresh_output("calculate_expression")  # "=" => 計算結果
        ]

        self.setup()
        self.default_action()

    def default_action(self):
        self.view.set_expression_output("0")

    def setup(self):
        symbol = self.view.symbol
        column_size = 5
        remain_row = 2
        for row in range(remain_row, len(symbol) // column_size + remain_row):
            for column in range(column_size):
                print(self.command[(row - remain_row) * column_size + column].__name__)
                self.view.create_button(
                    symbol[(row - remain_row) * column_size + column],
                    row,
                    column,
                    command=self.command[(row - remain_row) * column_size + column],
                    bootstyle=self.set_button_color(self.command[(row - remain_row) * column_size + column].__name__)
                )

    def set_button_color(self,button_name:str) -> str:
        if button_name == "answer_action":
            return "info"
        elif button_name == "expression_action":
            return "success"
        elif button_name == "refresh_action":
            return "danger"
        else:
            return "dark"

    def update_expression(self, value: str) -> None:
        self.model.update_expression(value)
        self.view.set_expression_output(self.model.expression)

    def generic_answer_output(self, model_func: str):
        def answer_action():
            exec(f"self.model.{model_func}()")
            self.view.set_answer_output(self.model.answer)

        return answer_action

    def generic_expression_output(self, model_func: str):
        def expression_action():
            exec(f"self.model.{model_func}()")
            self.view.set_expression_output(self.model.expression)

        return expression_action

    def generic_symbol(self, symbol: str):
        def symbol_action():
            self.update_expression(symbol)

        return symbol_action

    def generic_refresh_output(self, model_func: str):
        def refresh_action():
            exec(f"self.model.{model_func}()")
            self.refresh()

        return refresh_action

    def refresh(self):
        self.view.set_expression_output(self.model.expression)
        self.view.set_answer_output(self.model.answer)
