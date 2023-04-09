import decorator


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
            self.sin_expression,
            self.cos_expression,
            self.tan_expression,
            self.sec_expression,
            self.csc_expression,
            self.cot_expression,
            self.get_pi,  # pi
            self.get_e,
            self.clear_expression,  # C => 清除輸入
            self.delete_expression,
            "**2",
            self.get_reciprocal,  # 1/x  => 倒數
            self.get_abs,
            ".e+",  # exp => 科學計數法
            "%",
            "** 0.5",  # root 2 => **0.5
            "(",
            ")",
            self.get_factorial,  # 階乘 x!
            "/",
            "**",
            "7",
            "8",
            "9",
            "*",
            "10 **",  # 10的N次方
            "4",
            "5",
            "6",
            "-",
            self.get_log10,
            "1",
            "2",
            "3",
            "+",
            self.get_logln,    # ln
            self.set_minus,    # +/-
            "0",
            ".",
            self.calculate_expression  # "=" => 計算結果
        ]

        self.setup()

    def setup(self):
        symbol = self.view.symbol
        column_size = 5
        for y in range(1, len(symbol) // column_size + 1):
            for x in range(column_size):
                if type(self.command[(y-1) * column_size + x]) == str:
                    self.view.create_button(
                        symbol[(y-1) * column_size + x],
                        y,
                        x,
                        command=lambda symbol=self.command[(
                            y-1) * column_size + x]: self.update_expression(symbol)
                    )
                else:
                    self.view.create_button(
                        symbol[(y-1) * column_size + x],
                        y,
                        x,
                        command=self.command[(y-1) * column_size + x]
                    )

    def update_expression(self, value: str) -> None:
        self.model.update_expression(value)
        self.view.set_output(self.model.expression)

    def calculate_expression(self) -> None:
        self.model.calculate_expression()
        self.view.set_output(self.model.expression)

    def clear_expression(self) -> None:
        self.model.clear_expression()
        self.view.set_output(self.model.expression)

    def get_reciprocal(self) -> None:
        self.model.get_reciprocal()
        self.calculate_expression()

    def get_10power(self) -> None:
        self.model.get_10power()
        self.view.set_output(self.model.expression)

    def delete_expression(self) -> None:
        self.model.delete_expression()
        self.view.set_output(self.model.expression)

    def get_factorial(self) -> None:  # 階乘
        self.model.get_factorial()
        self.view.set_output(self.model.expression)

    def sin_expression(self) -> None:
        self.model.sin_expression()
        self.view.set_output(self.model.expression)

    def cos_expression(self) -> None:
        self.model.cos_expression()
        self.view.set_output(self.model.expression)

    def tan_expression(self) -> None:
        self.model.tan_expression()
        self.view.set_output(self.model.expression)

    def sec_expression(self) -> None:
        self.model.sec_expression()
        self.view.set_output(self.model.expression)

    def csc_expression(self) -> None:
        self.model.csc_expression()
        self.view.set_output(self.model.expression)

    def cot_expression(self) -> None:
        self.model.cot_expression()
        self.view.set_output(self.model.expression)

    def get_pi(self) -> None:
        self.model.get_pi()
        self.view.set_output(self.model.expression)

    def get_e(self) -> None:
        self.model.get_e()
        self.view.set_output(self.model.expression)

    def get_log10(self) -> None:
        self.model.get_log10()
        self.view.set_output(self.model.expression)

    def get_logln(self) -> None:
        self.model.get_logln()
        self.view.set_output(self.model.expression)

    def set_minus(self) -> None:
        self.model.set_minus()
        self.view.set_output(self.model.expression)

    def get_abs(self) -> None:
        self.model.get_abs()
        self.view.set_output(self.model.expression)
