import tkinter as tk
import models
import views
import controllers
import ttkbootstrap as ttk


def original_calculator() -> None:
    style = ttk.Style(theme='darkly')
    root = style.master
    model = models.BaseModel()
    view = views.BaseView(root)
    controller = controllers.BaseController(model, view)
    root.mainloop()


def advance_calculator() -> None:
    #root = tk.Tk()
    root = ttk.Window(themename="darkly")
    root.geometry()
    model = models.AdvanceModel()
    view = views.AdvanceView(root)
    controller = controllers.AdvanceController(model, view)
    root.mainloop()


if __name__ == '__main__':
    # original_calculator()
    advance_calculator()
