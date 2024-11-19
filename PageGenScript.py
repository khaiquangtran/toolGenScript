import tkinter as tk
from tkinter import filedialog
from Page import *
import json
from Script import *

class PageGenScript(Page):
   LISTOPTION = ["LearnImage", "Kanji", "KanjiV2"]

   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.labelProgramFile = tk.LabelFrame(self, text = "Program file")
        self.labelProgramFile.grid(row = 0, column = 0, padx = 10,  pady = 10, ipadx = 2, ipady = 2)

        self.entry = tk.Entry(self.labelProgramFile,  width = 60)
        self.entry.grid(row = 0, column = 0, pady = 5, padx = 5)

        self.btnBrowse = tk.Button(self.labelProgramFile, text = "Browse...", width = 13, height = 1, command = self.openFile)
        self.btnBrowse.grid(row = 0, column = 1)

        self.btnStart = tk.Button(self.labelProgramFile, text = "Start", font=('calibre', 15, 'bold'), width = 30, height = 1, command = self.parseFile)
        self.btnStart.grid(row = 1, column = 0)

        self.clicked = tk.StringVar()
        self.clicked.set(self.LISTOPTION[0])

        self.optGen = tk.OptionMenu(self.labelProgramFile, self.clicked , *self.LISTOPTION)
        self.optGen.config(width=10)
        self.optGen.grid(row = 1, column = 1, sticky = "n")

        self.labelProgramLog = tk.LabelFrame(self, text="Log")
        self.labelProgramLog.grid(row = 1, column = 0, ipadx = 2, ipady = 2)

        self.logText = tk.Text(self.labelProgramLog, width = 59, height = 10, state = "normal")
        self.logText.grid(row = 0, column = 0, columnspan = 3,  padx = 5,  pady = 5)
        self.logText.tag_configure("green_text", foreground = "green", font = ("calibre", 11 ,"bold"))
        self.logText.tag_configure("red_text", foreground = "red", font = ("calibre", 11 ,"bold"))

        self.btnClear = tk.Button(self.labelProgramLog, text = "Clear", font = ('calibre', 10), width = 6, command = self.clearLog)
        self.btnClear.grid(row = 1, column = 0, sticky="w", padx = 3)

   def openFile(self):
      filePath = filedialog.askopenfilename(title = "Choose file",
                                           filetypes = (("Json", "*.json"),))
      if filePath:
         self.entry.delete(0, tk.END)
         self.entry.insert(0, filePath)
      else:
         self.logText.insert(tk.END, "No file selected!!!\n", "red_text")

   def clearLog(self):
      self.logText.delete("1.0", tk.END)

   def parseFile(self):
      pathFile = self.entry.get()
      if pathFile:
         self.logText.insert(tk.END, pathFile+"\n")
         if self.clicked.get() == self.LISTOPTION[0]:  # LearnImage
            self.genScriptForLeanImage(pathFile)
         elif self.clicked.get() == self.LISTOPTION[1]: #Kanji
            self.genScriptForKanji(pathFile)
         elif self.clicked.get() == self.LISTOPTION[2]: #KanjiV2
            self.genScriptForKanjiV2(pathFile)
         else:
            return
      else:
         self.logText.insert(tk.END, "File is not exit!!!\n", "red_text")
         return

   def genScriptForLeanImage(self, pathFile):
      dictSaveFile = pathFile.rsplit('/', 1)[0] + "/index.html"
      # Read data from JSON file
      try:
         with open(pathFile, 'r', encoding='utf-8') as file:
            data = json.load(file)

         title = data.get("title", "")
         vocabulary = data["vocabulary"]

         # Initialize script with title
         script = ScrtipLearnImage.header.replace("<title></title>", f"<title>{title}</title>")

         # Add flashcards from vocabulary
         for item in vocabulary:
            item_script = ScrtipLearnImage.bodyFlashcard

            if len(item["japan"]) >= 7 and len(item["japan"]) <= 9:
               item_script = item_script.replace(
                  '<p class="japan"></p>', f'<p class="japan8">{item["japan"]}</p>'
               )
            else:
               item_script = item_script.replace(
                  '<p class="japan"></p>', f'<p class="japan">{item["japan"]}</p>'
               )

            if len(item["romaji"]) >= 13 and len(item["romaji"]) <= 15:
               item_script = item_script.replace(
                  '<p class="romaji">//</p>', f'<p class="romaji2">/{item["romaji"]}/</p>'
               )
            else:
               item_script = item_script.replace(
                  '<p class="romaji">//</p>', f'<p class="romaji">/{item["romaji"]}/</p>'
               )

            item_script = item_script.replace(
               '<img src="Images/.png"/>', f'<img src="Images/{item["img"]}.png"/>'
            ).replace(
               '<p class="mean"></p>', f'<p class="mean">{item["mean"]}</p>'
            )
            script += item_script

         # End script
         script += ScrtipLearnImage.bodyEnd

         # Write the entire script to file
         with open(dictSaveFile, "w", encoding="utf-8") as index:
            index.write(script)

         # Log result
         self.logText.insert(tk.END, "Successful!!!\n", "green_text")
         self.logText.insert(tk.END, f"Save here: {dictSaveFile}\n")

      except KeyError as e:
          # Log error
          self.logText.insert(tk.END, f"KeyError: {str(e)}\n", "red_text")

   def genScriptForKanji(self, pathFile):
      dictSaveFile = pathFile.rsplit('/', 1)[0] + "/index.html"

      # Read data from json file
      try:
         with open(pathFile, 'r', encoding='utf-8') as file:
             data = json.load(file)

         # Initialize script with title
         title = data.get("title", "")
         script = ScriptKanji.header.replace("<title></title>", f"<title>{title}</title>")
         vocabulary = data["vocabulary"]

         # Add vocabulary parts to script
         for i, item in enumerate(vocabulary, start=1):
            item_script = ScriptKanji.bodyNewWord.replace(
               "START NEW WORD", f"START {i} NEW WORD"
            ).replace(
               "おん", item["on"]
            ).replace(
               '<img src="../../GIF/kanji/gif/150x150/.gif" class="border_all"/>',
               f'<img src="../../GIF/kanji/gif/150x150/{item["image"]}.gif" class="border_all"/>'
            ).replace(
               "contentVietnam", item["content"]
            ).replace(
               "くん", item["kun"]
            )
            item_script += ScriptKanji.bodyStartOnKun
            # Add onKanji flashcards to item_script
            for y, on in enumerate(item.get("onKanji", []), start=1):
               flashcard_script = ScriptKanji.bodyFlashCard

               if len(on["japan"]) == 4:
                  flashcard_script = flashcard_script.replace(
                     '<p class="japan">1</p>', f'<p class="japan1 japan">{on["japan"]}</p>'
                  )
               elif len(on["japan"]) == 5:
                  flashcard_script = flashcard_script.replace(
                     '<p class="japan">1</p>', f'<p class="japan2 japan">{on["japan"]}</p>'
                  )
               elif len(on["japan"]) >= 6 and len(on["japan"]) <= 7:
                  flashcard_script = flashcard_script.replace(
                     '<p class="japan">1</p>', f'<p class="japan3 japan">{on["japan"]}</p>'
                  )
               else:
                  flashcard_script = flashcard_script.replace(
                     '<p class="japan">1</p>', f'<p class="japan">{on["japan"]}</p>'
                  )

               if len(on["hiragana"]) >= 6 and len(on["hiragana"]) <= 9:
                  flashcard_script = flashcard_script.replace(
                     '<p class="japan">2</p>', f'<p class="japan1 japan">{on["hiragana"]}</p>'
                  )
               else:
                  flashcard_script = flashcard_script.replace(
                     '<p class="japan">2</p>', f'<p class="japan">{on["hiragana"]}</p>'
                  )

               flashcard_script = flashcard_script.replace(
                  "<!-- START WORD-->", f"<!-- START {y} WORD-->"
               ).replace(
                  '<p class="romaji"></p>', f'<p class="romaji">{on["romaji"]}</p>'
               ).replace(
                  '</div> <!-- END WORD-->' , f'</div> <!-- END {y} WORD-->'
               )
               item_script += flashcard_script
            item_script += ScriptKanji.bodyEndOn

            item_script += ScriptKanji.bodySatrtKun
            # Add onKanji flashcards to item_script
            if item.get("kun", ""):
               for y, kun in enumerate(item.get("kunKanji", []), start=1):
                  flashcard_script = ScriptKanji.bodyFlashCard

                  if len(kun["japan"]) == 4:
                     flashcard_script = flashcard_script.replace(
                        '<p class="japan">1</p>', f'<p class="japan1 japan">{kun["japan"]}</p>'
                     )
                  elif len(kun["japan"]) == 5:
                     flashcard_script = flashcard_script.replace(
                        '<p class="japan">1</p>', f'<p class="japan2 japan">{kun["japan"]}</p>'
                     )
                  elif len(kun["japan"]) >= 6 and len(on["japan"]) <= 7:
                     flashcard_script = flashcard_script.replace(
                        '<p class="japan">1</p>', f'<p class="japan3 japan">{kun["japan"]}</p>'
                     )
                  else:
                     flashcard_script = flashcard_script.replace(
                        '<p class="japan">1</p>', f'<p class="japan">{kun["japan"]}</p>'
                     )

                  if len(kun["hiragana"]) >= 6 and len(kun["hiragana"]) <= 9:
                     flashcard_script = flashcard_script.replace(
                        '<p class="japan">2</p>', f'<p class="japan1 japan">{kun["hiragana"]}</p>'
                     )
                  else:
                     flashcard_script = flashcard_script.replace(
                        '<p class="japan">2</p>', f'<p class="japan">{kun["hiragana"]}</p>'
                     )

                  flashcard_script = flashcard_script.replace(
                     "<!-- START WORD-->", f"<!-- START {y} WORD-->"
                  ).replace(
                     '<p class="romaji"></p>', f'<p class="romaji">{kun["romaji"]}</p>'
                  ).replace(
                     '</div> <!-- END WORD-->' , f'</div> <!-- END {y} WORD-->'
                  )
                  item_script += flashcard_script
            item_script += ScriptKanji.bodyEndOnKun
            item_script += ScriptKanji.bodyNewWordEnd.replace(
               'END NEW WORD', f'END {i} NEW WORD'
            )
            script += item_script

         script += ScriptKanji.bodyEnd
         # Write the entire script to file
         with open(dictSaveFile, "w", encoding="utf-8") as index:
             index.write(script)

         # Log result
         self.logText.insert(tk.END, "Successful!!!\n", "green_text")
         self.logText.insert(tk.END, f"Save here: {dictSaveFile}\n")

      except KeyError as e:
          # Log error
          self.logText.insert(tk.END, f"KeyError: {str(e)}\n", "red_text")

   def genScriptForKanjiV2(self, pathFile):
      dictSaveFile = pathFile.rsplit('/', 1)[0] + "/index.html"

      # Read data from json file
      try:
         with open(pathFile, 'r', encoding='utf-8') as file:
             data = json.load(file)

         # Initialize script with title
         title = data.get("title", "")
         script = ScriptKanjiV2.header.replace("<title></title>", f"<title>{title}</title>")

         vocabulary = data["vocabulary"]
         for y, item in enumerate(vocabulary, start=0):
            japan = list(item["japan"])
            item_script = None
            if len(japan) == 1:
               item_script = ScriptKanjiV2.bodySwipper1.replace(
                  '<img src="../../GIF/kanji/gif/150x150/.gif" class="border_all" />',
                  f'<img src="../../GIF/kanji/gif/150x150/{japan[0]}.gif" class="border_all" />'
               )
            elif len(japan) == 2:
               item_script = ScriptKanjiV2.bodySwipper2.replace(
                  'src="../../GIF/kanji/gif/150x150/1.gif"',
                  f'src="../../GIF/kanji/gif/150x150/{japan[0]}.gif"'
               ).replace (
                  'src="../../GIF/kanji/gif/150x150/2.gif"',
                  f'src="../../GIF/kanji/gif/150x150/{japan[1]}.gif"'
               )
            elif len(japan) == 3:
               item_script = ScriptKanjiV2.bodySwipper3.replace(
                  'src="../../GIF/kanji/gif/150x150/1.gif"',
                  f'src="../../GIF/kanji/gif/150x150/{japan[0]}.gif"'
               ).replace(
                  'src="../../GIF/kanji/gif/150x150/2.gif"',
                  f'src="../../GIF/kanji/gif/150x150/{japan[1]}.gif"'
               ).replace(
                  'src="../../GIF/kanji/gif/150x150/3.gif"',
                  f'src="../../GIF/kanji/gif/150x150/{japan[2]}.gif"'
               )
            else:
               self.logText.insert(tk.END, f"Japanese length in Json haven't supported")
               return

            if y != 0:
               item_script = item_script.replace(
                  '<div class="swiper-slide slide">',
                  f'<div class="swiper-slide slide{y}">'
               ).replace(
                  '<button class="open_button slide" type="button">Help</button>',
                  f'<button class="open_button slide{y}" type="button">Help</button>'
               )
            script += item_script

         script += ScriptKanjiV2.bodyEnd

         # Write the entire script to file
         with open(dictSaveFile, "w", encoding="utf-8") as index:
             index.write(script)

         # Log result
         self.logText.insert(tk.END, "Successful!!!\n", "green_text")
         self.logText.insert(tk.END, f"Save here: {dictSaveFile}\n")

      except KeyError as e:
         # Log error
         self.logText.insert(tk.END, f"KeyError: {str(e)}\n", "red_text")