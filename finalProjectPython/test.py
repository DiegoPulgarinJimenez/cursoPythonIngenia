from tkinter import *
from tkinter import scrolledtext

root = Tk()
root.title("acá")
root.geometry("800x400")
frame1 = Frame(root, bg='green', height=100, width=200, cursor='plus')
frame1.pack(side=LEFT)
scrollTextBox = scrolledtext.ScrolledText(frame1, wrap=WORD, width=8, height=4, bg='pink')
scrollTextBox.place(x=20, y=20)
scrollTextBox.insert(0.1, END, 'hello')
root.mainloop()
