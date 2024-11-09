import tkinter as tk
import ctypes
from PageGenScript import *
from PageResizeImage import *

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.p1 = PageGenScript(self)
        p2 = PageResizeImage(self)

        # Create frames for buttons and page container
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        # Place pages in container frame
        self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # Buttons to switch pages
        self.b1 = tk.Button(buttonframe, text=" Gen Script ", command=self.p1.show)
        b2 = tk.Button(buttonframe, text="Resize Image", command=p2.show)

        self.b1.pack(side="left")
        b2.pack(side="left")

        # Show the first page by default
        self.p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.wm_geometry("510x370")  # Set fixed window size
    root.title("Generate script")
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    try:
        root.iconbitmap("./icon.ico")
    except:
        print("Icon file not found.")
    root.resizable(False, False)
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)

    root.mainloop()