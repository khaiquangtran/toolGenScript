import tkinter as tk
from Page import *
from tkinter import filedialog
import os
import cv2

class PageResizeImage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.labelProgramFile = tk.LabelFrame(self, text="Program file")
        self.labelProgramFile.grid(row = 0, column = 0, padx=10,  pady=10, ipadx=2, ipady=2)

        self.entry = tk.Entry(self.labelProgramFile,  width=60)
        self.entry.grid(row = 0, column = 0, columnspan=3, pady = 5, padx = 5)

        self.btnBrowse = tk.Button(self.labelProgramFile, text = "Browse...", width=13, height=1, command = self.openFolder)
        self.btnBrowse.grid(row = 0, column = 3)

        self.btnRun = tk.Button(self.labelProgramFile, text = "RUN", font=('calibre', 15, 'bold'), width=25, height=1, command = self.run)
        self.btnRun.grid(row = 1, column = 0, columnspan = 2, rowspan = 2, padx = 5)

        self.labelWidth = tk.Label(self.labelProgramFile, text = "Width: ")
        self.labelWidth.grid(row = 1, column = 2, sticky = "e")

        self.entryWidth = tk.Entry(self.labelProgramFile, width=15,  justify='right')
        self.entryWidth.grid(row = 1, column = 3)
        self.entryWidth.insert(0, 300)

        self.labelHeight = tk.Label(self.labelProgramFile, text = "Height: ")
        self.labelHeight.grid(row = 2, column = 2, sticky = "e")

        self.entryHeight = tk.Entry(self.labelProgramFile, width=15, justify='right')
        self.entryHeight.grid(row = 2, column = 3)
        self.entryHeight.insert(0, 220)

        self.labelProgramLog = tk.LabelFrame(self, text="Log")
        self.labelProgramLog.grid(row = 1, column = 0, ipadx=2, ipady=2)

        self.logText = tk.Text(self.labelProgramLog, width=59, height=10, state="normal")
        self.logText.grid(row = 0, column = 0, columnspan = 3,  padx=5,  pady=5)
        self.logText.tag_configure("green_text", foreground="green", font=("calibre", 11 ,"bold"))

        self.btnClear = tk.Button(self.labelProgramLog, text = "Clear", font=('calibre', 10), width = 6)
        self.btnClear.grid(row = 1, column = 0, sticky="w", padx = 3)

    def openFolder(self):
        folderPath = filedialog.askdirectory(title="Choose folder")
        if folderPath:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, folderPath)
        else:
            self.logText.insert(tk.END, "Folder is not exit\n")

    def run(self):
        pathFolder = self.entry.get()
        height = self.entryHeight.get()
        width = self.entryWidth.get()

        listFile = self.scranFolder(pathFolder)
        for file in listFile:
            if self.isValidImageExtension(file):
                self.resize(file, width, height)
            else:
                self.logText.insert(tk.END, f"file {file} is not image")

    def scranFolder(self, path):
        listFilePath = []
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                listFilePath.append(file_path)
        return listFilePath

    def isValidImageExtension(self, fileName):
        validExtensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
        return any(fileName.lower().endswith(ext) for ext in validExtensions)

    def resize(self, filePath, width, height):
        image = cv2.imread(filePath)

        if image is None:
            self.logText.insert(tk.END, f"Error loading {filePath}")
            return

        if image.shape[0] == int(height) and image.shape[1] == int(width):
            self.logText.insert(tk.END, f"skip {filePath}\n")
        else:
            size = (int(width), int(height))
            resized_image = cv2.resize(image, size)
            cv2.imwrite(filePath, resized_image)
            self.logText.insert(tk.END, f"Done {filePath}\n")