

import tkinter as tk


class AbstractView(object):

    def __init__(self, master):
        pass

    def create_button(self):
        pass

    def get_input(self):
        pass

    def set_output(self):
        pass


class BaseView(AbstractView):
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Create the entry field
        self.display = tk.Entry(self.master, width=30, font=('Arial', 12))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create the buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)
        self.create_button("=", 5, 0, 1, 4)

    def create_button(self, text, row, column, rowspan=1, columnspan=1, command=None):
        button = tk.Button(self.master, text=text, width=7,
                           height=2, font=('Arial', 12), command=command)
        button.grid(row=row, column=column, rowspan=rowspan,
                    columnspan=columnspan, padx=5, pady=5)

    def get_input(self):
        return self.display.get()

    def set_output(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(0, value)
