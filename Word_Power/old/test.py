from Tkinter import *

root = Tk()
root.geometry("400x600")


def newWord():
	myLabel = Label(root, text="Hello varbu")
	myLabel.pack()

myButton = Button(root, text="Load new word", command=newWord)
myButton.pack()

root.mainloop()



