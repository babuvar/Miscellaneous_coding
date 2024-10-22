from Tkinter import *
import json
import random


with open('full_dic2.json') as json_file:
    full_dic2 = json.load(json_file)
 
alphabets = ['any', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

root = Tk()

root.geometry("800x400")

#Dropdown list
var_start = StringVar(root)
var_start.set(alphabets[0])
w = OptionMenu(root, var_start, *alphabets)
w.grid(row=1, column=0)

#Display word
answerLabel1 = Label(root, text="")
answerLabel1.grid(row=0, column=1)
#Display meaning
answerLabel2 = Label(root, text="", wraplength=500)
answerLabel2.grid(row=1, column=1)
#Display difficulty
answerLabel3 = Label(root, text="")
answerLabel3.grid(row=0, column=2)

#Search word
search_str = Entry(root, width = 20)
search_str.grid(row=2, column=0)

def onButtonClick():

    full_dic = full_dic2[var_start.get()]
    word, properties = random.choice(list(full_dic.items()))
    answerLabel1.configure(text=word)
    answerLabel2.configure(text=properties[0])
    answerLabel3.configure(text='(difficulty = %s)'%properties[1])


def searchClick():

    full_dic = full_dic2['any']
    try:
        word = search_str.get()
        properties = full_dic[word]
        answerLabel1.configure(text=word)
        answerLabel2.configure(text=properties[0])
        answerLabel3.configure(text='(difficulty = %s)'%properties[1])
    except:
        answerLabel1.configure(text='?')
        answerLabel2.configure(text='word not found')
        answerLabel3.configure(text='(difficulty = ?)')


enterButton = Button(root, text="New Word", command=onButtonClick)
enterButton.grid(row=0, column=0)

searchButton = Button(root, text="Search Word", command=searchClick)
searchButton.grid(row=3, column=0)



root.mainloop()






