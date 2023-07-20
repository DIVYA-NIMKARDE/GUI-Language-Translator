#importing modules
from tkinter import *
from translate import Translator
from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
from datetime import datetime
from datetime import date
from datetime import time
from tkinter import font as tkFont
from PIL import ImageTk, Image  
# initializing window
Screen = Tk()
Screen.title("Language Translator with GUI")
Screen.geometry("1000x800")
Screen.configure(bg = "")
img =Image.open('bk.jpg')
bg = ImageTk.PhotoImage(img)

label = Label(Screen, image=bg)
label.place(x = 0,y = 0)

InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()



#tuple for choosing languages
LanguageChoices = {'Hindi','English','French','German','Spanish'}
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Hindi')

f20 = tkFont.Font(family='Comic Sans MS', size=20)
f25 = tkFont.Font(family='Comic Sans MS', size=25)
f15 = tkFont.Font(family='Comic Sans MS', size=15)
def Translate():
    translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)
    
def Text_to_speech():
    Message = OutputVar.get()
    speech = gTTS(text = Message)
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    speech.save(filename)
    playsound(filename)


#choice for input language
InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)
InputLanguageChoiceMenu.config(font=f20)
Label(Screen,text="Choose a Language", font =f25).grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1, padx=50, pady=50)

#choice in which the language is to be translated
NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices)

Label(Screen,text="Translated Language", font =f25).grid(row=0,column=5)
NewLanguageChoiceMenu.grid(row=1,column=5)
NewLanguageChoiceMenu.config(font=f20)

Label(Screen,text="Enter Text", font =f15).grid(row=2,column =0)
TextVar = StringVar()
TextBox = Entry(Screen,textvariable=TextVar, font = f15).grid(row=2,column = 1, padx=50, pady=50)


Label(Screen,text="Output Text", font =f15).grid(row=2,column =4)
OutputVar = StringVar()
TextBox = Entry(Screen,textvariable=OutputVar, font =f15).grid(row=2,column = 5)

#Button for calling function
B = Button(Screen,text="Translate",command=Translate, font=f15).grid(row=7,column=1, padx=100, pady=100)

button_submit = Button(Screen, text ="Speech", command=Text_to_speech, font=f15).grid(row=7,column=5, padx=100, pady=100)

mainloop()
