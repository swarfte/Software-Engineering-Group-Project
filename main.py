import tkinter as tk
import models
import views
import controllers


def original_calculator() -> None:
    root = tk.Tk()
    model = models.BaseModel()
    view = views.BaseView(root)
    controller = controllers.BaseController(model, view)
    root.mainloop()


def advance_calculator() -> None:
    root = tk.Tk()
    root.geometry("450x550")
    model = models.AdvanceModel()
    view = views.AdvanceView(root)
    controller = controllers.AdvanceController(model, view)
    root.mainloop()


if __name__ == '__main__':
    # original_calculator()
    advance_calculator()
