from bs4 import BeautifulSoup
import requests
from tkinter import * 
import tkinter as tk

#gui
#window
def gui():
    def refresh():
        root.destroy()
        gui()
    def submit():
        if(entry.get()==answer):
            entry.delete(0,END)
            entry.insert(0,"Correct answer")
        else:
            entry.delete(0,END)
            entry.insert(0,"Incorrect answer")
    page = requests.get('http://www.subnettingquestions.com/')
    soup = BeautifulSoup(page.content, 'html.parser')
    question = (soup.find(class_='question')).getText()

    answer = soup.find(id='answerLayer').getText()
    answer = answer[9:]
    root = tk.Tk()
    canvas = tk.Canvas(root, height= 200, width = 600)
    canvas.pack()

    frame = tk.Frame(root, bg = '#80c1ff')
    frame.place(relx=.1, rely=.1, relwidth=.8,relheight=.8)

    label = tk.Label(frame, text = question, bg = 'white')
    label.pack(side = 'top')

    entry = tk.Entry(frame, bg = 'white', xscrollcommand = 1 )
    entry.pack()

    submit = tk.Button(frame, text= "Submit", command = submit)#button to refresh
    submit.pack(side = 'left')

    refresh = tk.Button(frame, text= "Refresh", command = refresh)#button to refresh
    refresh.pack(side = 'right')
    #end of application gui
    root.mainloop()
gui()
