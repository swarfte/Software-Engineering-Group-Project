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
            self.clean_output,  # C => 清除輸入
            self.generic_expression_output("delete_expression"),
            "^2",
            self.generic_answer_output("get_reciprocal"),  # 1/x  => 倒數
            self.generic_answer_output("get_abs"),
            ".e+",  # exp => 科學計數法
            "%",
            "^0.5",  # root 2 => **0.5
            "(",
            ")",
            self.generic_answer_output("get_factorial"),  # 階乘 x!
            "/",
            "^",
            "7",
            "8",
            "9",
            "x",
            self.generic_answer_output("get_10power"),  # 10的N次方
            "4",
            "5",
            "6",
            "-",
            self.generic_answer_output("get_log10"),
            "1",
            "2",
            "3",
            "+",
            self.generic_answer_output("get_logln"),  # ln
            self.generic_answer_output("set_minus"),  # +/-
            "0",
            ".",
            self.generic_answer_output("calculate_expression")  # "=" => 計算結果
        ]

        self.setup()

    def setup(self):
        symbol = self.view.symbol
        column_size = 5
        remain_row = 2
        for row in range(remain_row, len(symbol) // column_size + remain_row):
            for column in range(column_size):
                if type(self.command[(row - remain_row) * column_size + column]) == str:
                    self.view.create_button(
                        symbol[(row - remain_row) * column_size + column],
                        row,
                        column,
                        command=lambda symbol=self.command[(row - remain_row) * column_size + column]: self.update_expression(symbol)
                    )
                else:
                    self.view.create_button(
                        symbol[(row - remain_row) * column_size + column],
                        row,
                        column,
                        command=self.command[(row - remain_row) * column_size + column]
                    )

    def generic_answer_output(self, model_func: str):
        def action():
            exec(f"self.model.{model_func}()")
            self.view.set_answer_output(self.model.answer)

        return action

    def generic_expression_output(self, model_func: str):
        def action():
            exec(f"self.model.{model_func}()")
            self.view.set_expression_output(self.model.expression)

        return action

    def clean_output(self):
        self.model.clear_output()
        self.refresh()

    def refresh(self):
        self.view.set_expression_output(self.model.expression)
        self.view.set_answer_output(self.model.expression)

    def update_expression(self, value: str) -> None:
        self.model.update_expression(value)
        self.view.set_expression_output(self.model.expression)
