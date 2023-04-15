

import tkinter as tk
import ttkbootstrap as ttk
class AbstractView(object):

    def __init__(self, master):
        pass

    def create_button(self):
        pass

    def get_input(self):
        pass

    def set_answer_output(self, value):
        pass

    def set_expression_output(self, value):
        pass

class BaseView(AbstractView):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.root = master
        self.root.title("Calculator")

        # Create the entry field
        self.display = tk.Entry(self.root, width=30,
                                font=('Arial', 12))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    def create_button(self, text, row, column, rowspan=1, columnspan=1, command=None):
        button = tk.Button(self.root, text=text, width=5,
                           height=2, font=('Arial', 10), command=command)
        button.grid(row=row, column=column, rowspan=rowspan,
                    columnspan=columnspan, padx=5, pady=5)

    def get_input(self):
        return self.display.get()

    def set_answer_output(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(0, value)


class AdvanceView(AbstractView):
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.title("Science Calculator")

        entry_style = ttk.Style()
        entry_style.configure('Custom.TEntry', borderwidth=0, highlightthickness=0,bootstyle="dark")
        font_size = 37
        entry_width = 20
        self.expression_display = ttk.Entry(self.root, width=entry_width, font=('Arial', font_size), style ='Custom.TEntry')
        self.expression_display.config(state="readonly")
        self.expression_display.grid(row=0, column=0, columnspan=5, padx=0, pady=0)

        self.answer_display = ttk.Entry(self.root, width=entry_width, font=('Arial', font_size), style ='Custom.TEntry')
        self.answer_display.config(state="readonly")
        self.answer_display.grid(row=1, column=0, columnspan=5, padx=0, pady=0)

        self.symbol = [
            "sin",
            "cos",
            "tan",
            "sec",
            "csc",
            "cot",
            "\u03C0",     # pi 3.14
            "e",
            "C",
            "delete",
            "x\u00B2",  # x^2  #\u00B2係^2  #\u00B3係^3
            "1/x",
            "|x|",
            "exp",
            "mod",
            "\u221A",  # root 2
            "(",
            ")",
            "n!",
            "/",
            "x\u02B8",     # x^y   改完但x同y望落有啲奇怪   
            "7",
            "8",
            "9",
            "x",
            "10\u02E3",    #  10^x 
            "4",
            "5",
            "6",
            "-",
            "log",
            "1",
            "2",
            "3",
            "+",
            "ln",
            "+/-",
            "0",
            ".",
            "="
        ]


    def create_button(self, text, row, column, rowspan=1, columnspan=1, command=None , bootstyle=None) -> ttk.Button:
        button = ttk.Button(self.root, text=text, width=10,
                            command=command, bootstyle=bootstyle)
        button.grid(row=row, column=column, rowspan=rowspan,
                    columnspan=columnspan, padx=1, pady=1,sticky='w')

        return button
    def get_input(self) -> str:
        return self.expression_display.get()

    def set_answer_output(self, value) -> None:
        self.answer_display.config(state="normal")
        self.answer_display.delete(0, tk.END)
        self.answer_display.insert(0, value)
        self.answer_display.config(state="readonly")

    def set_expression_output(self, value:str) -> None:
        self.expression_display.config(state="normal")
        self.expression_display.delete(0, tk.END)
        self.expression_display.insert(0, value)
        self.expression_display.config(state="readonly")
