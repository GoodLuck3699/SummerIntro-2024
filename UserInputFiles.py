from tkinter import filedialog, Label, PhotoImage
import fileinput
import os
import playsound
import tkinter as tk
from PIL import Image

#playsound.playsound('Testinglol1.mp3')

filewha = filedialog.askopenfilename()

ext = os.path.splitext(filewha)[-1].lower()

def textfunc():
       for line in fileinput.input(files=filewha):
            print(line, end='')

def musfunc(music):
       print("Music:" , music)
       playsound.playsound(os.path.basename(music))

def imagefunc():
        if ext == ".jfif":
               img = Image.open(filewha.jfif)
               img.save(filewha.gif)

               img = Image.open(filewha.gif)
               img.save(filewha.gif)
        else:
                root = tk.Tk()
                root.geometry("800x600")
                image = PhotoImage(file=filewha)
                original_image = Label(root, image=image)
                original_image.image = image
                original_image.pack(anchor="center", fill=tk.BOTH, expand=True)
                root.mainloop()



if ext == ".txt":
        textfunc()

elif ext == ".mp3":
        musfunc(filewha)
elif ext == ".png" or ".jfif":
        imagefunc()
else:
        print(filewha, "is an unknown file format.")