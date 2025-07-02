import tkinter as tk
from tkinter import Canvas, PhotoImage, ttk, Label, Text, Message, LabelFrame, Scrollbar, Listbox
from tkinter import *
from PIL import Image, ImageTk
from functools import partial
import random
import winsound
import sys

##################################
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
###################################

root = tk.Tk()
root.geometry("800x600")
root.title("AppleClicker")

canvas = Canvas(root, width=800, height=600,)
canvas.pack(anchor="center")

#canvas displays the background
#canvas1 displays the apple button and click the apple thingy
#canvas2 displays the apple counter, achievement button and special apple display. The special apple display is called mylist
#canvas3 is the achievement screen
#canvas4 is the Altar
#canvas5 is the Setting Screen
#Canvas6 is the How to Play the Game Screen
#Canvas7 is the Credit Screen

#resizing image of apple
'''
def resize_by_percentage(image, outfile, percentage):
    with Image.open (image) as im:
        width, height = im.size
        resized_dimensions = (int(width * percentage), int(height * percentage))
        resized = im.resize(resized_dimensions)
        resized.save(outfile)
resize_by_percentage('apple.png', 'newapple.png', .2)
'''

#Displaying images
# my_image = PhotoImage(file='newapple.png')
resizeBackImage = ImageTk.PhotoImage(Image.open(resource_path('sunset.png')).resize((800,600)))
canvas.create_image(0, 0, anchor='nw', image=resizeBackImage)

#Canvas for apple counter
canvas1 = Canvas(root, width=350, height=100)
canvas1.place(x=460, y=35)
canvas1.config(width=320, height=50, state= "disabled")

#Canvas to display apple typle
canvas2=Canvas(root, width=320, height=400)
canvas2.place(x=460, y=89)
# scroll_bar = Scrollbar(canvas2) 
# scroll_bar.place(width=20, height=200)
mylist = Text(canvas2, state = "disabled") 
mylist.config(borderwidth=5, relief="solid", font=("Courier", 10), width=39, height=6)
mylist.pack(fill = BOTH, expand = True)
# scroll_bar.config( command = mylist.yview )

#Canvas for the Altar
canvas4=Canvas(root, width=320, height=250)
canvas4.config(highlightthickness=2, highlightbackground='black', bg='#ffad33')
canvas4.place(x=460, y=280)
canvas4.pack_propagate(0)

#Button that contains transparency
'''quitImage = ImageTk.PhotoImage(Image.open("newapple.png"))
quitButton = canvas.create_image(200, 250, image=quitImage)
canvas.tag_bind(quitButton, "<Button-1>", bruh)
quitButton = tk.Button()
'''

#function for apple counter------------------------------------------
def bruh():
    global counter
    counter += 1
    label1.config(text="Apples " + str(counter))

#displays number of special apples------------------------------------------
def update_label(applesList):

    mylist.config(state = "normal")
    mylist.delete('1.0', END)

    previous_value = None
    current_value = applesList[3]  # Replace with your method of getting the current value

    if previous_value is not None and current_value > previous_value:
        applesList[5] += 1
    elif previous_value is not None and current_value == previous_value:
        applesList[5] = 0

    previous_value = current_value


    mylist.insert('end', str(applesList[0]) + " Bad" + "\n")
    mylist.insert('end', str(applesList[1]) + " Commons" + "\n")
    mylist.insert('end', str(applesList[2]) + " Rares" + "\n")
    mylist.insert('end', str(applesList[3]) + " Epics" + "\n")
    mylist.insert('end',  str(applesList[4]) + " Legendaries" + "\n")

    mylist.config(state = "disabled")

#Apple Button---------------------------------------------------------
resizephoto = ImageTk.PhotoImage(Image.open(resource_path('FreeApple2.png')).resize((400,400)))
Button = tk.Button(canvas, image = resizephoto, bd=10, activebackground='orange',background='#993333', command=lambda:[bruh(), fileWrite(Apples), achieveCalc(Apples, themcommons, Rank)])
Button.place(x=35,y=35)
Button.config(width=350, height=450)

# Click me label below Image. Is Tranparent.----------------------------------
text = canvas.create_text((220,540),text="Hello", fill='white', font=("Comic Sans MS", 32))
res = "Click The Apple!"
canvas.itemconfig(text, text = res)

#display for apple counter--------------------------------
counter = 0
label1 = Label(canvas1, text="Apples " + str(counter))
label1.config(borderwidth=5, relief="solid", font=("Courier", 33))
label1.place(width=325, height=54)

#Where apple types are stored----------------------------------------
Apples = [0, 0, 0, 0, 0, 0]

#gives player special apples. Based on %-------------------------
def fileWrite(applesList):

    if counter % 10 == 0 and counter>5:

        chance = random.randint(1,100)
        
        if chance <= 1:
            applesList[4] += 1
        elif chance <= 10:
            applesList[3] += 1 
        elif chance <= 25:
            applesList[2] += 1
        elif chance <= 50:
            applesList[1] += 1
        else:
            applesList[0] += 1

    update_label(applesList)

#Photos for the achievements----------------------------
photo1 = PhotoImage(file = resource_path('preAchievement1.png'))
photo2 = PhotoImage(file = resource_path('preAchievement3.png'))
photo3 = PhotoImage(file = resource_path('preAchievement2.png'))
photo4 = PhotoImage(file = resource_path('preAchievement4.png'))
photo5 = PhotoImage(file = resource_path('preAchievement5.png'))

photo10 = PhotoImage(file = resource_path('Achievement1.png'))
photo20 = PhotoImage(file = resource_path('Achievement3.png'))
photo30 = PhotoImage(file = resource_path('Achievement2.png'))
photo40 = PhotoImage(file = resource_path('Achievement4.png'))
photo50 = PhotoImage(file = resource_path('Achievement5.png'))
themcommons = 0

#When hovoring over a button, it changes color--------------------------------
def changeOnHover(button1, colorOnHover, colorOnLeave):
 
    # adjusting backgroung of the widget
    # background on entering widget
    button1.bind("<Enter>", func=lambda e: button1.config(
        background=colorOnHover))
 
    # background color on leving widget
    button1.bind("<Leave>", func=lambda e: button1.config(
        background=colorOnLeave))

# #Achievement Button
canvas3 = tk.Canvas(root, background="pink", width=700, height=500, borderwidth=3)
Button1 = tk.Button(canvas2, bd=5, text='Achievements', fg='white', activebackground='#993333', background='#993333', command= lambda: show_achive(Apples))
Button1.config(width=5, height=2, font=("Comic Sans MS", 15))
Button1.pack(fill = BOTH, expand = True, side = TOP)
changeOnHover(Button1, "#ff4d4d", "#993333")

#This creates the achievemnt Screen---------------------------
def show_achive(applesList):
    canvas3.place(x=50,y=50)
    Button2 = tk.Button(canvas3, activebackground='orange', background='red', text = "×", fg = "white", command=lambda: canvas3.place_forget())
    Button2.config(width=3, height=1, font=("Comic Sans MS", 15))
    Button2.place(x = 665, y = 0)

    Achive_Label=Label(canvas3, text="Achievements")
    Achive_Label.config(borderwidth=5, relief="solid", font=("Courier", 33))
    Achive_Label.place(width=664, height=60)

    achieveCalc(applesList, themcommons, Rank)

achive10 = Label(canvas3, image=photo1)
achive10.config(width = 496, height=56)
achive10.place(x=100,y=70)

achive20 = Label(canvas3, image=photo2)
achive20.config(width = 496, height=56)
achive20.place(x=100,y=155) 

achive30 = Label(canvas3, image=photo3)
achive30.config(width = 496, height=56)
achive30.place(x=100,y=240)

achive40 = Label(canvas3, image=photo5)
achive40.config(width = 496, height=56)
achive40.place(x=100,y=320)  

achive50 = Label(canvas3, image=photo4)
achive50.config(width = 496, height=56)
achive50.place(x=100,y=400)

achievemnt=[0,0,0,0,0]
#This calculates when you recieve an achievement--------------------
def achieveCalc(applesList, themcommons, Rank):

    if counter >= 10000:
        achievemnt[0]+=1
        achive10.config(image=photo10)
        if achievemnt[0] == 1:
                if sound[0] %2 == 0:
                    winsound.PlaySound(resource_path("AchievementSound.wav"), winsound.SND_ASYNC)
    if applesList[0] >= 1000:
        achievemnt[1]+=1
        achive20.config(image=photo20)
        if achievemnt[1] == 1:
                if sound[0] %2 == 0:
                    winsound.PlaySound(resource_path("AchievementSound.wav"), winsound.SND_ASYNC)
    if applesList[4] >= 10:
        achievemnt[2]+=1
        achive30.config(image=photo30)
        if achievemnt[2] == 1:
                if sound[0] %2 == 0:
                    winsound.PlaySound(resource_path("AchievementSound.wav"), winsound.SND_ASYNC)
    if applesList[5] <= 10:
        themcommons += 1

    if themcommons >= 10:
        achievemnt[3]+=1
        achive40.config(image=photo50)
        if achievemnt[3] == 1:
                if sound[0] %2 == 0:
                    winsound.PlaySound(resource_path("AchievementSound.wav"), winsound.SND_ASYNC)
    if Rank[0] > 5:
        achievemnt[4]+=1
        achive50.config(image=photo40)
        if achievemnt[4] == 1:
                if sound[0] %2 == 0:
                    winsound.PlaySound(resource_path("AchievementSound.wav"), winsound.SND_ASYNC)
#The Alter Label----------------------------------------------------------------
Thealter = Label(canvas4, text='The Altar', fg='white', bg='red')
Thealter.config(font =("Comic Sans MS", 15), highlightthickness=5, highlightbackground='black', width=300)
Thealter.pack(padx=0,pady=0)

#Declaration and initial value of Ranks and EXP------------------------
Rank=[1]
Maxexp=[100]
CurrentXp=[0]
WHYRANK="Farmer"

#Updates the labels for Rank and EXP-----------------------------------------------
def UpdateXpRank(CurrentXp, Maxexp, Rank, WHYRANK):
    canvas4.itemconfig(text2, text="EXP: "+ str(CurrentXp[0]) + " / " + str(Maxexp[0]), font=('Comic Sans MS', 10))
    canvas4.itemconfig(text3, text="Rank "+ str(Rank[0]) + " / 5", fill="black", font=('Comic Sans MS', 10))
    WhatRank.config(text=WHYRANK)

#Calculates how much EXP to give when sacrificing special apples. It sends info to Ranking to level up and then displays them-----------
def text_updation(idx, applesList, CurrentXp, Rank, Maxexp, WHYRANK): 
    if idx == 0 and applesList[0] > 0:
        CurrentXp[0] += 1
        applesList[0] -= 1
    elif  idx == 1 and applesList[1] > 0:
        CurrentXp[0] += 10
        applesList[1] -= 1
    elif  idx == 2 and applesList[2] > 0:
        CurrentXp[0] += 25
        applesList[2] -= 1
    elif  idx == 3 and applesList[3] > 0:
        CurrentXp[0] += 50
        applesList[3] -= 1
    elif  idx == 4 and applesList[4] > 0:
        CurrentXp[0] += 100
        applesList[4] -= 1
    elif  idx == 5:
        addvalues = (applesList[0] * 1) + (applesList[1] * 10) + (applesList[2] * 25) + (applesList[3] * 50) + (applesList[4] * 100)
        CurrentXp[0] += addvalues
        for i in range(len(applesList)):
            applesList[i]=0
    if CurrentXp[0] >= Maxexp[0]:
        CurrentXp[0] = 0
        Rank[0] += 1
    if sound[0] %2 == 0:
        winsound.PlaySound(resource_path("AchievementSound.wav"), winsound.SND_ASYNC)
    update_label(applesList)
    Ranking(Maxexp, Rank, WHYRANK)

# The for loop that contains all the sacrifice buttons
ButtonName = ["Sacrifice Bad", "Sacrifice Common", "Sacrifice Rare", "Sacrifice Epic", "Sacrifice Legendary", "Sacrifice All"]
button_dict = [] 
for i in range(6): 
    # pass each button's text to a function 
    # def action(x = lang):  
    #     return text_updation(x, Apples, CurrentXp, Rank) 
        
    # create the buttons  
    newButton = tk.Button(canvas4, bd=4, fg='white',text=ButtonName[i], activebackground='#993333', background='#993333', command= lambda i = i: text_updation(i, Apples, CurrentXp, Rank, Maxexp, WHYRANK))
    newButton.config(font=("Comic Sans MS", 8))
    newButton.pack(padx=(0,180), pady=2)
    button_dict.append(newButton)
    changeOnHover(newButton, "#ff4d4d", "#993333")

#Initial display for the Rank and EXP
text3 = canvas4.create_text(230, 80, text="Rank "+ str(Rank[0]) + " / 5", fill="black", font=('Comic Sans MS', 10))
text2 = canvas4.create_text(230, 205, text="EXP: "+ str(CurrentXp[0]) + " / " + str(Maxexp[0]), fill="black", font=('Comic Sans MS', 10))
#Images for the Rank Photo
Rank1image = PhotoImage(file = resource_path('Farmer1.png'))
Rank2image = PhotoImage(file = resource_path('FactoryWorker.png'))
Rank3image = PhotoImage(file = resource_path('UpperClass.png'))
Rank4image = PhotoImage(file = resource_path('Tycoon.png'))
Rank5image = PhotoImage(file = resource_path('Demon.png'))
#What Rank is the display for the Ranking you in
WhatRank = Label(canvas4, text=WHYRANK, fg='black')
WhatRank.config(font =("Comic Sans MS", 14), highlightthickness=1, highlightbackground='black')
WhatRank.place(x=181,y=170,  width=100, height=20)
#Intial Rank image display
RankImage = Label(canvas4, image=Rank1image)
RankImage.place(x=195,y=90)
#Calculates Ranking
def Ranking(Maxexp, Rank, WHYRANK):
    Maxexp
    WHYRANK
    if Rank[0] == 1:
        Maxexp[0]=100
        WHYRANK = "Farmer"
    if Rank[0] == 2:
        Maxexp[0]=1000
        RankImage = Label(canvas4, image=Rank2image)
        RankImage.place(x=195,y=90)
        WHYRANK = "Worker"
    if Rank[0] == 3:
        Maxexp[0]=10000
        RankImage = Label(canvas4, image=Rank3image)
        RankImage.place(x=195,y=90)
        WHYRANK = "UpperClass"
    if Rank[0] == 4:
        Maxexp[0]=100000
        RankImage = Label(canvas4, image=Rank4image)
        RankImage.place(x=195,y=90)
        WHYRANK = "Tycoon"
    if Rank[0] == 5:
        Maxexp[0]= "∞"
        RankImage = Label(canvas4, image=Rank5image)
        RankImage.place(x=195,y=90)
        WHYRANK = "Demon"
    winsound.PlaySound(resource_path("AchievementSound.wav"), winsound.SND_ASYNC)
    UpdateXpRank(CurrentXp, Maxexp, Rank, WHYRANK)

# p = multiprocessing.Process(target=playsound, args="Goldberg Variations, BWV 988 - 22 - Variatio 21 Canone alla Settima.mp3")
# p.join()
# if mus[0] % 2 == 0:
    
    
# else:
#     p.join()
#     p.terminate()
photo100 = ImageTk.PhotoImage(Image.open(resource_path('NoMusicImage.png')).resize((40,40)))
photo1000 = ImageTk.PhotoImage(Image.open(resource_path('BackfroundMusicImage.png')).resize((40,40)))
photo1001 = ImageTk.PhotoImage(Image.open(resource_path('NoSoundImage.png')).resize((40,40)))
photo10001 = ImageTk.PhotoImage(Image.open(resource_path('SoundImage.png')).resize((40,40)))
mus=[0]
sound=[0]

def MUSIC(mus):
    if mus[0] %2 == 0:
        MusicBtn.config(image=photo1000)
        winsound.PlaySound(resource_path("Goldberg Variations, BWV 988 - 22 - Variatio 21 Canone alla Settima.wav"), winsound.SND_ASYNC)
    else:
        winsound.PlaySound(None, winsound.SND_PURGE)
        MusicBtn.config(image=photo100)
    mus[0]+=1

def SOUND(sound):
    sound[0]+=1
    if sound[0] %2 == 0:
        SoundBtn.config(image=photo10001)
    else:
        SoundBtn.config(image=photo1001)

#All the photos for bottom right buttons
# setting = PhotoImage(file=resource_path("Setting.png"))
resizeSetting = ImageTk.PhotoImage(Image.open(resource_path('settingsButton.png')).resize((50,50)))
question = PhotoImage(file=resource_path("Question.png"))
# credits = PhotoImage(file=resource_path('Credits.png'))
resizeCredits = ImageTk.PhotoImage(Image.open(resource_path('Credits.png')).resize((50,50)))

#Bro, it shows the setting screen and all its components
canvas5 = tk.Canvas(root, background="#cc8800", width=300, height=300, borderwidth=3)
    
settinglabel = Label(canvas5, background='#802b00', text='Setting', fg='white')
settinglabel.config(width=40, height=3, highlightcolor='#000000')
settinglabel.place(x=2,y=2)

SettingBtn = tk.Button(canvas5, activebackground='brown', background='black', text = "×", fg = "white", command=lambda: canvas5.place_forget())
SettingBtn.config(width=3, height=1, font=("Comic Sans MS", 15))
SettingBtn.place(x = 262, y = 2)

MusicBack = Label(canvas5, background='#996633')
MusicBack.config(highlightthickness=2, highlightbackground='black')
MusicBack.place(x = 70, y = 90, width=140, height=55)

MusicLabel = Label(canvas5, activebackground='brown', background='black', text = "Music", fg = "white")
MusicLabel.config(font=("Comic Sans MS", 12), highlightthickness=2, highlightbackground='brown')
MusicLabel.place(x = 80, y = 100)

MusicBtn = tk.Button(canvas5, activebackground='brown', image=photo100, background="black", command=lambda: MUSIC(mus))
MusicBtn.place(x = 155, y = 94)

SoundBack = Label(canvas5, background='#996633')
SoundBack.config(highlightthickness=2, highlightbackground='black')
SoundBack.place(x = 70, y = 190, width=140, height=55)

SoundLabel = Label(canvas5, activebackground='brown', background='black', text = "Sound", fg = "white")
SoundLabel.config(font=("Comic Sans MS", 12), highlightthickness=2, highlightbackground='brown')
SoundLabel.place(x = 80, y = 200)

SoundBtn = tk.Button(canvas5, activebackground='brown', image=photo10001, background="black", command=lambda: SOUND(sound))
SoundBtn.place(x = 155, y = 195)

def show_setting():
    canvas5.place(x=250,y=150)
#Shows the How To screen and alll its components
def show_HowTo():
    canvas6 = tk.Canvas(root, background="#cc8800", width=600, height=500, borderwidth=3)
    canvas6.place(x=100,y=50)
    canvas6.propagate(0)

    HowTolabel = Label(canvas6, background='#802b00', text='How to Play the Game', fg='white')
    HowTolabel.config(width=79, height=3, highlightcolor='#000000')
    HowTolabel.pack(side=TOP, padx=(2,48), pady=(2,38))

    HowToBtn = tk.Button(canvas6, activebackground='brown', background='black', text = "×", fg = "white", command=lambda: canvas6.destroy())
    HowToBtn.config(width=3, height=1, font=("Comic Sans MS", 15))
    HowToBtn.place(x = 562, y = 2)

    StepBack = Label(canvas6, background='#802b00')
    StepBack.config(width=75, height=27, highlightcolor='#000000')
    StepBack.place(x=40, y=80)

    Step1 = Label(canvas6, background='#ffa366', text='1. Click the apples to Gain -Apples-. \n Every 10 apples grants you a -SPECIAL- Apple. \n Chances of type of -SPECIAL- Apples vary.', fg='white')
    Step1.config(width=70, height=4, highlightcolor='#000000')
    Step1.place(x=60, y=100)

    Step2 = Label(canvas6, background='#ffa366', text='2. Sacrifice your -SPECIAL Apples to the Altar and gain EXP. \n Each type of -SPECIAL- Apple gives a diffrent amount of EXP', fg='white')
    Step2.config(width=70, height=4, highlightcolor='#000000')
    Step2.place(x=60, y=170)

    Step3 = Label(canvas6, background='#ffa366', text="3. Getting enough EXP will level up your Rank. \n The EXP required for each rank gets much harder the higher the rank.\n They're are also achivements that are pretty hard to get.", fg='white')
    Step3.config(width=70, height=4, highlightcolor='#000000')
    Step3.place(x=60, y=240)

    Step4 = Label(canvas6, background='#ffa366', text="Chance of -SPECIAL- Apples: \n \n Bad:(If you don't get the others) \n Common: 50% \n Rare: 25% \n Epic: 10% \n Legendary: 1%", fg='white')
    Step4.config(width=34, height=10, highlightcolor='#000000')
    Step4.place(x=60, y=310)

    Step5 = Label(canvas6, background='#ffa366', text="EXP given by -SPECIAL- Apples: \n \n Bad:1 EXP \n Common: 10 EXP \n Rare: 25 EXP \n Epic: 50 EXP \n Legendary: 100 EXP", fg='white')
    Step5.config(width=34, height=10, highlightcolor='#000000')
    Step5.place(x=312, y=310)
#Shows the credit screen and all its components
def show_Credits():
    canvas7 = tk.Canvas(root, background="#cc8800", width=500, height=400, borderwidth=3)
    canvas7.place(x=150,y=80)
    canvas7.propagate(0)
    
    Creditlabel = Label(canvas7, background='#802b00', text='CREDITS', fg='white')
    Creditlabel.config(width=79, height=3, highlightcolor='#000000')
    Creditlabel.pack(side=TOP, padx=(2,48), pady=(2,38))

    CreditBtn = tk.Button(canvas7, activebackground='brown', background='black', text = "×", fg = "white", command=lambda: canvas7.destroy())
    CreditBtn.config(width=3, height=1, font=("Comic Sans MS", 15))
    CreditBtn.place(x = 462, y = 2)

    Programers = Label(canvas7, background="#993333", text = "Lead Programer: Alan Nguyen \n Lead Debugger: Carl Nguyen", fg="white", borderwidth=2, relief="solid")
    Programers.config(width=50, height=3)
    Programers.place(x=80, y=65)

    GraphicDesign = Label(canvas7, background="#993333", text = "Lead Graphic Designer: Alan Nguyen \n Co Graphic Designer: Carl Nguyen", fg="white", borderwidth=2, relief="solid")
    GraphicDesign.config(width=50, height=3)
    GraphicDesign.place(x=80, y=125)

    Support = Label(canvas7, background="#993333", text = "Special Thanks To: \nKen Nguyen \nDon Nguyen", fg="white", borderwidth=2, relief="solid")
    Support.config(width=50, height=4)
    Support.place(x=80, y=185)

    AllImages = Label(canvas7, background="#993333", text = "Background Image and the Apple Image comes from perchance.org. \n Music: Goldberg Variations, BWV 988 - 22 - Variatio 21 Canone alla Settima \n Music from musopen.org \n Sound made by Carl Nguyen and recorded on 123apps ", fg="white", borderwidth=2, relief="solid")
    AllImages.config(width=67, height=5)
    AllImages.place(x=20, y=260)

    OnlineHelp = Label(canvas7, background="#993333", text = "A huge thanks to Stack Overflow and Geeks for Geeks for the knowledge to fix code\n and teaching me the basics of the tkinter Libary and Python", fg="white", borderwidth=2, relief="solid")
    OnlineHelp.config(width=67, height=3)
    OnlineHelp.place(x=20, y=350)

#The bottom right buttons
Setting = tk.Button(canvas, activebackground='grey', background='black', image=resizeSetting, fg = "white", command=lambda: show_setting())
Setting.config(width=45, height=45, font=("Comic Sans MS", 15))
Setting.place(x = 747, y = 547)
Question = tk.Button(canvas, activebackground='grey', background='black', image=question, fg = "white", command=lambda: show_HowTo())
Question.config(width=45, height=45, font=("Comic Sans MS", 15))
Question.place(x = 695, y = 547)
Credits = tk.Button(canvas, activebackground='grey', background='black', image=resizeCredits, fg = "white", command=lambda: show_Credits())
Credits.config(width=45, height=45, font=("Comic Sans MS", 15))
Credits.place(x = 643, y = 547)

root.mainloop()