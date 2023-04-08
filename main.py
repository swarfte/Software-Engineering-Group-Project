import tkinter as tk
import models
import views
import controllers


def main() -> None:
    root = tk.Tk()
    model = models.BaseModel()
    view = views.BaseView(root)
    controller = controllers.BaseController(model, view)
    root.mainloop()


if __name__ == '__main__':
    main()
