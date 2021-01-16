from tkinter import *


def change_name():
    message = 'successful operation'
    i = 0
    while i < len(message):
        label2.config(text=message[i, END])
        i += 1
        return
    if i != len(message):
        change_name()



root = Tk()  # Add the Main Window
mainFrame = Frame(root, bg='lightblue', height=400, width=450, cursor="pirate", bd=35, relief='groove')  # Add frame with it's parameters
root.title("Personal Finances")  # Add title to the  Main Window
root.resizable(False, False)  # Allows or not to resize the Main Window
# root.iconbitmap("rutaImage") --> Allows to changes the icon on the Main Window
# root.geometry("500x500")  # Allows to change the Main Window initial size
root.config(bg='lightgreen')  # Allows to change the main window color
mainFrame.pack(side='left', anchor='s', padx=60, pady=60)  # Add the frame to the Main Window... Side = left, right, top, bottom to
# locate frame, using the method fill --> mainFrame.pack(fill='y', expand=True) using both instead y it expands to all
label1 = Label(mainFrame, text="hiiiii", font=("chill", 16))
label1.place(x=10, y=10)
label2 = Label(mainFrame, text="successful operation", fg="blue", justify="right")
label2.place(x=40, y=40)  # Using place() instead pack() allows to relocate the label
Label(mainFrame, text="newLabel").place(x=80, y=80)  # Another way to create labels
label2.after(1000, change_name)
root.mainloop()  # Allows the Window to Run. It most be at the end of the code.
