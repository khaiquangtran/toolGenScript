import tkinter as tk
from Page import *

listOption = ["LearnImage", "Kanji", "KanjiV2"]

class PageGenScript(Page):
   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        labelProgramFile = tk.LabelFrame(self, text="Program file")
        labelProgramFile.grid(row = 0, column = 0, padx=10,  pady=10, ipadx=2, ipady=2)

        entry = tk.Entry(labelProgramFile,  width=60)
        entry.grid(row = 0, column = 0, pady = 5, padx = 5)

        btnBrowse = tk.Button(labelProgramFile, text = "Browse...", width=13, height=1)
        btnBrowse.grid(row = 0, column = 1)

        btnStart = tk.Button(labelProgramFile, text = "Start", font=('calibre', 15, 'bold'), width=20, height=1)
        btnStart.grid(row = 1, column = 0)

        clicked = tk.StringVar()
        clicked.set(listOption[0])

        optGen = tk.OptionMenu(labelProgramFile, clicked , *listOption)
        optGen.config(width=10)
        optGen.grid(row = 1, column = 1, sticky = "n")

        labelProgramLog = tk.LabelFrame(self, text="Log")
        labelProgramLog.grid(row = 1, column = 0, ipadx=2, ipady=2)

        logText = tk.Text(labelProgramLog, width=59, height=10, state="normal")
        logText.grid(row = 0, column = 0, columnspan = 3,  padx=5,  pady=5)
        logText.tag_configure("green_text", foreground="green", font=("calibre", 11 ,"bold"))

        btnClear = tk.Button(labelProgramLog, text = "Clear", font=('calibre', 10), width = 6)
        btnClear.grid(row = 1, column = 0, sticky="w", padx = 3)