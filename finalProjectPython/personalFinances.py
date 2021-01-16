from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import pickle

# ---------- Calc Var ----------
n_1 = 0
operation = ""
# ---------- Results Var ----------
totalExpenses = 0
totalEarnings = 0
moneyAvailable = 0
moneyDeficit = 0
# ---------- permanence ----------
info_db_reading = open('per_earns_DB', 'rb')
earns_db_load = pickle.load(info_db_reading)
info_db_reading.close()
del info_db_reading

info_db_reading = open('per_expenses_DB', 'rb')
expenses_db_load = pickle.load(info_db_reading)
info_db_reading.close()
del info_db_reading
# ---------- Expenses DB ----------
transport_db = expenses_db_load.get('tExpenses')
food_db = expenses_db_load.get('fExpenses')
hobbies_db = expenses_db_load.get('hExpenses')
debts_db = expenses_db_load.get('dExpenses')
# ---------- Earnings DB ----------
salary_db = earns_db_load.get('sEarns')
consulting_earnings_db = earns_db_load.get('cEarns')
hobbies_earnings_db = earns_db_load.get('hEarns')
other_earnings_db = earns_db_load.get('oEarns')
# ---------- Notes DB ----------
readNotes = open('notes_DB', 'rb')
notes_load = pickle.load(readNotes)
readNotes.close()
del readNotes


def display_earns_data():
    global totalEarnings
    v1 = plus_db(salary_db)
    v2 = plus_db(consulting_earnings_db)
    v3 = plus_db(hobbies_earnings_db)
    v4 = plus_db(other_earnings_db)
    totalEarnings = v1 + v2 + v3 + v4
    return totalEarnings


def display_expenses_data():
    global totalExpenses
    v1 = plus_db(transport_db)
    v2 = plus_db(food_db)
    v3 = plus_db(hobbies_db)
    v4 = plus_db(debts_db)
    totalExpenses = v1 + v2 + v3 + v4
    return totalExpenses


def is_number(parameter_1):
    try:
        float(parameter_1)
        return True
    except ValueError:
        return False


def plus_db(parameter_2):
    res_t = 0
    for i in parameter_2:
        res_t += i
    return res_t


def calculator_window():
    def add():
        n1 = result_box.get()
        global n_1
        global operation
        operation = "add"
        n_1 = int(n1)
        result_box.delete(0, END)

    def subtract():
        n1 = result_box.get()
        global n_1
        global operation
        operation = "subtract"
        n_1 = int(n1)
        result_box.delete(0, END)

    def multiply():
        n1 = result_box.get()
        global n_1
        global operation
        operation = "multiply"
        n_1 = int(n1)
        result_box.delete(0, END)

    def divide():
        n1 = result_box.get()
        global n_1
        global operation
        operation = "divide"
        n_1 = int(n1)
        result_box.delete(0, END)

    def equals():
        n2 = result_box.get()
        result_box.delete(0, END)
        if operation == "add":
            res = n_1 + int(n2)
            result_box.insert(0, res)
        elif operation == "subtract":
            res = n_1 - int(n2)
            result_box.insert(0, res)
        elif operation == "multiply":
            res = n_1 * int(n2)
            result_box.insert(0, res)
        elif operation == "divide":
            res = n_1 / int(n2)
            result_box.insert(0, res)

    def dot():
        pass

    def delete():
        pass

    def clear():
        result_box.delete(0, END)

    def writing(entry):
        # result_box.config(text="".join(num))
        # op_label.config(text="".join(op_list))
        current = result_box.get()
        result_box.delete(0, END)
        result_box.insert(0, str(current) + str(entry))

    calc_window = Toplevel()
    calc_window.title('D Calculator')
    calc_window.geometry('420x400')
    calc_window.resizable(False, False)
    calc_window.config(bg='lightslategrey', cursor='dot')
    calc_window.iconbitmap('images/iconCalc.ico')
    result_frame = Frame(calc_window, bg='lightgrey', height=95, width=400, cursor='circle', bd=4, relief='sunken')
    result_frame.pack(side='top', padx=1, pady=10)
    calc_frame = Frame(calc_window, bg='lightsteelblue', height=255, width=400, cursor='dot', bd=3, relief='ridge')
    calc_frame.pack(side='bottom', padx=1, pady=10)
    op_label = Label(result_frame, text='write here', height=2, width=55, bg='lightgrey', anchor='w', bd=2,
                     relief='ridge')
    op_label.place(x=2, y=2)
    result_box = Entry(result_frame, bg='lightgrey', width=43, fg='blue', borderwidth=2, font=11, justify=RIGHT)
    result_box.place(x=2, y=45, height=40)
    # Operation Buttons
    clear_button = Button(calc_frame, text='C', width=12, height=2, command=clear).place(x=4, y=1)
    divide_button = Button(calc_frame, text='/', width=12, height=2, command=divide).place(x=101, y=1)
    product_button = Button(calc_frame, text='*', width=12, height=2, command=multiply).place(x=198, y=1)
    delete_button = Button(calc_frame, text='<--', width=12, height=2, command=delete).place(x=296, y=1)
    minus_button = Button(calc_frame, text='-', width=12, height=2, command=subtract).place(x=296, y=50)
    add_button = Button(calc_frame, text='+', width=12, height=2, command=add).place(x=296, y=100)
    equals_button = Button(calc_frame, text='=', width=12, height=5, command=equals).place(x=296, y=150)
    dot_button = Button(calc_frame, text='.', width=12, height=2, command=dot).place(x=198, y=200)
    # Numbers Buttons
    seven_button = Button(calc_frame, text='7', width=12, height=2, command=lambda: writing(7)).place(x=4, y=50)
    eight_button = Button(calc_frame, text='8', width=12, height=2, command=lambda: writing(8)).place(x=101, y=50)
    nine_button = Button(calc_frame, text='9', width=12, height=2, command=lambda: writing(9)).place(x=198, y=50)
    four_button = Button(calc_frame, text='4', width=12, height=2, command=lambda: writing(4)).place(x=4, y=100)
    five_button = Button(calc_frame, text='5', width=12, height=2, command=lambda: writing(5)).place(x=101, y=100)
    six_button = Button(calc_frame, text='6', width=12, height=2, command=lambda: writing(6)).place(x=198, y=100)
    one_button = Button(calc_frame, text='1', width=12, height=2, command=lambda: writing(1)).place(x=4, y=150)
    two_button = Button(calc_frame, text='2', width=12, height=2, command=lambda: writing(2)).place(x=101, y=150)
    three_button = Button(calc_frame, text='3', width=12, height=2, command=lambda: writing(3)).place(x=198, y=150)
    zero_button = Button(calc_frame, text='0', width=26, height=2, command=lambda: writing(0)).place(x=4, y=200)

    calc_window.mainloop()


def clean_notes_box():
    scrollTextBox.delete(1.0, END)


def undone_expenses_reset():
    transportResult.config(text='0')
    transport_db.clear()
    foodResult.config(text='0')
    food_db.clear()
    hobbies_db.clear()
    hobbiesResult.config(text='0')
    debts_db.clear()
    debtsResult.config(text='0')
    expenses_results.config(text='0')
    totalEMonth.config(text='0')


def undone_earns_reset():
    salary_db.clear()
    salary_result.config(text='0')
    consulting_earnings_db.clear()
    consulting_result.config(text='0')
    hobbies_earnings_db.clear()
    hobbies_earns_result.config(text='0')
    other_earnings_db.clear()
    other_result.config(text='0')
    earnings_results.config(text='0')
    totalRMonth.config(text='0')


def expenses_db(type_entry):
    global totalExpenses
    if type_entry == 'transport':
        new_entry = ExpensesBox.get()
        if is_number(new_entry):
            transport_db.append(int(new_entry))
            totalExpenses += int(new_entry)
            messagebox.showinfo(message='Transport expense entered correctly', title='Message')
            ExpensesBox.delete(0, END)
            transportResult.config(text=(str(plus_db(transport_db))))
        else:
            messagebox.showinfo(message='Only numerical figures allowed \n          try it again please.')
            ExpensesBox.delete(0, END)

    elif type_entry == 'food':
        new_entry = ExpensesBox.get()
        if is_number(new_entry):
            food_db.append(int(new_entry))
            totalExpenses += int(new_entry)
            messagebox.showinfo(message='Food expense entered correctly', title='Message')
            ExpensesBox.delete(0, END)
            foodResult.config(text=(str(plus_db(food_db))))
        else:
            messagebox.showinfo(message='Only numerical figures allowed \n          try it again please.')
            ExpensesBox.delete(0, END)
    elif type_entry == 'hobbies':
        new_entry = ExpensesBox.get()
        if is_number(new_entry):
            hobbies_db.append(int(new_entry))
            totalExpenses += int(new_entry)
            messagebox.showinfo(message='Hobbies expense entered correctly', title='Message')
            ExpensesBox.delete(0, END)
            hobbiesResult.config(text=(str(plus_db(hobbies_db))))
        else:
            messagebox.showinfo(message='Only numerical figures allowed \n          try it again please.')
            ExpensesBox.delete(0, END)
    elif type_entry == 'debts':
        new_entry = ExpensesBox.get()
        if is_number(new_entry):
            debts_db.append(int(new_entry))
            totalExpenses += int(new_entry)
            messagebox.showinfo(message='Debts expense entered correctly', title='Message')
            ExpensesBox.delete(0, END)
            debtsResult.config(text=(str(plus_db(debts_db))))
        else:
            messagebox.showinfo(message='Only numerical figures allowed \n          try it again please.')
            ExpensesBox.delete(0, END)
    expenses_results.config(text=(str(totalExpenses)))


def earnings_db(type_entry_2):
    global totalEarnings
    if type_entry_2 == 'salary':
        new_entry = EarningsBox.get()
        if is_number(new_entry):
            salary_db.append(int(new_entry))
            totalEarnings += int(new_entry)
            messagebox.showinfo(message='Salary entered correctly', title='Message')
            EarningsBox.delete(0, END)
            salary_result.config(text=(str(plus_db(salary_db))))
        else:
            messagebox.showinfo(message='Only numerical figures allowed \n          try it again please.')
            EarningsBox.delete(0, END)

    elif type_entry_2 == 'consulting':
        new_entry = EarningsBox.get()
        if is_number(new_entry):
            consulting_earnings_db.append(int(new_entry))
            totalEarnings += int(new_entry)
            messagebox.showinfo(message='Consulting Earnings entered correctly', title='Message')
            EarningsBox.delete(0, END)
            consulting_result.config(text=(str(plus_db(consulting_earnings_db))))
        else:
            messagebox.showinfo(message='Only numerical figures allowed \n          try it again please.')
            EarningsBox.delete(0, END)
    elif type_entry_2 == 'hobbies':
        new_entry = EarningsBox.get()
        if is_number(new_entry):
            hobbies_earnings_db.append(int(new_entry))
            totalEarnings += int(new_entry)
            messagebox.showinfo(message='Hobbies Earnings entered correctly', title='Message')
            EarningsBox.delete(0, END)
            hobbies_earns_result.config(text=(str(plus_db(hobbies_earnings_db))))
        else:
            messagebox.showinfo(message='Only numerical figures allowed \n          try it again please.')
            EarningsBox.delete(0, END)
    elif type_entry_2 == 'other':
        new_entry = EarningsBox.get()
        if is_number(new_entry):
            other_earnings_db.append(int(new_entry))
            totalEarnings += int(new_entry)
            messagebox.showinfo(message='Other Earnings entered correctly', title='Message')
            EarningsBox.delete(0, END)
            other_result.config(text=(str(plus_db(other_earnings_db))))
        else:
            messagebox.showinfo(message='Only numerical figures allowed \n          try it again please.')
            EarningsBox.delete(0, END)
    earnings_results.config(text=(str(totalEarnings)))


def calculate_balance():
    global moneyAvailable
    moneyAvailable = totalEarnings
    moneyAvailable -= totalExpenses
    totalEMonth.config(text=str(totalExpenses))
    totalRMonth.config(text=str(moneyAvailable))
    if moneyAvailable == 0:
        messagebox.showinfo(message='You do not have money saved \nbe careful with your expenses')
        totalRMonth.config(fg='orange')
    elif moneyAvailable < 0:
        messagebox.showinfo(message='                Negative balance \nReconsider your investments and expenses')
        totalRMonth.config(fg='red')
    elif moneyAvailable > 0:
        totalRMonth.config(fg='green')


def save_db():
    expenses_info = {'tExpenses': transport_db, 'fExpenses': food_db, 'hExpenses': hobbies_db, 'dExpenses': debts_db}
    info_db = open('per_expenses_DB', 'wb')
    pickle.dump(expenses_info, info_db)
    info_db.close()
    del info_db
    earnings_info = {'sEarns': salary_db, 'cEarns': consulting_earnings_db, 'hEarns': hobbies_earnings_db,
                     'oEarns': other_earnings_db}
    info_db = open('per_earns_DB', 'wb')
    pickle.dump(earnings_info, info_db)
    info_db.close()
    del info_db
    notes_box_save = open('notes_DB', 'wb')
    pickle.dump(scrollTextBox.get(0.1, END), notes_box_save)


def reset_db():
    reset = messagebox.askquestion('Warning', 'Are you sure to reset the data base?. This process can not be undone.')
    if reset == 'yes':
        clean_notes_box()
        undone_expenses_reset()
        undone_earns_reset()
        save_db()


# -------------------Main Window-------------------

mainWindow = Tk()
mainWindow.title('D Personal Finances')
mainWindow.geometry('1000x700')
mainWindow.resizable(False, False)
mainWindow.config(bg='whitesmoke', cursor='pirate')
mainWindow.iconbitmap('images/iconDollar.ico')
# --------------------Frames-----------------------
leftFrame = Frame(mainWindow, bg='lightgrey', height=700, width=500, cursor='plus')
leftFrame.pack(side='left', padx=5, pady=5)
rightFrame = Frame(mainWindow, bg='lightgrey', height=700, width=500, cursor='plus')
rightFrame.pack(side='right', padx=5, pady=5)
# --------------------Labels------------------------
Label(leftFrame, text='Inputs: ', fg='green', bg='lightgrey').place(x=220, y=5)
Label(leftFrame, text='Monthly expenses', fg='red', bg='lightgrey', font=14).place(x=200, y=40)
Label(leftFrame, text='Monthly Earns', fg='green', bg='lightgrey', font=14).place(x=200, y=200)
Label(rightFrame, text='Registry: ', fg='green', bg='lightgrey').place(x=220, y=5)
Label(rightFrame, text='Remember to save changes before exiting.', fg='red', bg='lightgrey', font=12).place(x=170,
                                                                                                            y=650)
# ---------- Expenses ----------
Label(rightFrame, text='Expenses', fg='red', bg='lightgrey', font=12).place(x=10, y=40)
transport_registry = Label(rightFrame, text='Transport Expenses: ', fg='black', bg='lightgrey').place(x=10, y=70)
transportResult = Label(rightFrame, text='0', fg='red', bg='lightgrey')
transportResult.place(x=135, y=70)
#
food_registry = Label(rightFrame, text='Food Expenses: ', fg='black', bg='lightgrey').place(x=10, y=90)
foodResult = Label(rightFrame, text='0', fg='red', bg='lightgrey')
foodResult.place(x=135, y=90)
#
hobbies_registry = Label(rightFrame, text='Hobbies Expenses: ', fg='black', bg='lightgrey').place(x=10, y=110)
hobbiesResult = Label(rightFrame, text='0', fg='red', bg='lightgrey')
hobbiesResult.place(x=135, y=110)
#
debts_registry = Label(rightFrame, text='Debts Expenses: ', fg='black', bg='lightgrey').place(x=10, y=130)
debtsResult = Label(rightFrame, text='0', fg='red', bg='lightgrey')
debtsResult.place(x=135, y=130)
#
total_expenses = Label(rightFrame, text='Total Expenses: ', fg='purple', bg='lightgrey').place(x=10, y=150)
expenses_results = Label(rightFrame, text='0', fg='red', bg='lightgrey')
expenses_results.place(x=135, y=150)
# ---------- Earnings ----------
Label(rightFrame, text='Earnings', fg='green', bg='lightgrey', font=12).place(x=10, y=180)
salary_registry = Label(rightFrame, text='Earned Salary: ', fg='black', bg='lightgrey').place(x=10, y=210)
salary_result = Label(rightFrame, text='0', fg='green', bg='lightgrey')
salary_result.place(x=135, y=210)
#
consulting_registry = Label(rightFrame, text='Consulting Earnings: ', fg='black', bg='lightgrey').place(x=10, y=230)
consulting_result = Label(rightFrame, text='0', fg='green', bg='lightgrey')
consulting_result.place(x=135, y=230)
#
hobbies_earns_registry = Label(rightFrame, text='Hobbies Earnings: ', fg='black', bg='lightgrey').place(x=10, y=250)
hobbies_earns_result = Label(rightFrame, text='0', fg='green', bg='lightgrey')
hobbies_earns_result.place(x=135, y=250)
#
other_registry = Label(rightFrame, text='Other Earnings: ', fg='black', bg='lightgrey').place(x=10, y=270)
other_result = Label(rightFrame, text='0', fg='green', bg='lightgrey')
other_result.place(x=135, y=270)
#
total_earnings = Label(rightFrame, text='Total Earnings: ', fg='purple', bg='lightgrey').place(x=10, y=290)
earnings_results = Label(rightFrame, text='0', fg='green', bg='lightgrey')
earnings_results.place(x=135, y=290)
# ---------- Final results ----------
Label(rightFrame, text='Total Revenue Month: ', fg='blue', bg='lightgrey').place(x=10, y=330)
totalRMonth = Label(rightFrame, text='0', fg='green', bg='lightgrey')
totalRMonth.place(x=145, y=330)
Label(rightFrame, text='Total Expenses Month: ', fg='blue', bg='lightgrey').place(x=10, y=360)
totalEMonth = Label(rightFrame, text='0', fg='red', bg='lightgrey')
totalEMonth.place(x=145, y=360)

# ---------- Input Fields ----------
expenses = Label(leftFrame, text='Enter Expenses: ', bg='lightgrey', fg='brown', font=12).place(x=10, y=70)
earnings = Label(leftFrame, text='Enter Earnings: ', bg='lightgrey', fg='brown', font=12).place(x=10, y=240)
notes = Label(leftFrame, text='Notes: ', bg='lightgrey', fg='brown', font=12).place(x=10, y=380)
# ---------- Text Box ----------
ExpensesBox = Entry(leftFrame, width=34, fg='red', borderwidth=2, font=11, justify=RIGHT)
ExpensesBox.place(x=145, y=70)
EarningsBox = Entry(leftFrame, width=34, fg='darkgreen', borderwidth=2, font=11, justify=RIGHT)
EarningsBox.place(x=145, y=240)
scrollTextBox = scrolledtext.ScrolledText(leftFrame, wrap=WORD, width=42, height=17)
scrollTextBox.place(x=80, y=380)
scrollTextBox.insert(0.1, notes_load)
# ---------------------Buttons----------------------
# Expenses Buttons
transportExButton = Button(leftFrame, text='Save In \ntransport expenses', height=2,
                           command=lambda: expenses_db('transport')).place(x=10, y=110)
foodExButton = Button(leftFrame, text='Save In \nfood expenses', height=2,
                      command=lambda: expenses_db('food')).place(x=135, y=110)
hobbiesExButton = Button(leftFrame, text='Save In \nhobbies expenses', height=2,
                         command=lambda: expenses_db('hobbies')).place(x=235, y=110)
debtsExButton = Button(leftFrame, text='Save In \ndebts expenses', height=2,
                       command=lambda: expenses_db('debts')).place(x=354, y=110)
# Earnings Buttons
salaryEarnsButton = Button(leftFrame, text='Save In \nsalary earnings', height=2,
                           command=lambda: earnings_db('salary')).place(x=10, y=280)
consultingEarnsButton = Button(leftFrame, text='Save In \nconsulting earnings', height=2,
                               command=lambda: earnings_db('consulting')).place(x=111, y=280)
hobbiesEarnsButton = Button(leftFrame, text='Save In \nhobbies earnings', height=2,
                            command=lambda: earnings_db('hobbies')).place(x=236, y=280)
othersEarnsButton = Button(leftFrame, text='Save In \nother earnings', height=2,
                           command=lambda: earnings_db('other'), width=14).place(x=350, y=280)
balanceButton = Button(rightFrame, text='Calculate Balance', command=calculate_balance).place(x=30, y=390)

notesButton = Button(leftFrame, text='Clean', command=clean_notes_box).place(x=20, y=642)
calcButton = Button(leftFrame, text='D Basic Calculator', command=calculator_window)
calcButton.place(x=380, y=5, height=30)
saveButton = Button(rightFrame, text='Save DB ', bg='green', command=save_db).place(x=20, y=650)
resetButton = Button(rightFrame, text='Reset DB', bg='red', fg='white', command=reset_db).place(x=100, y=650)

transportResult.config(text=str(plus_db(transport_db)))
foodResult.config(text=str(plus_db(food_db)))
hobbiesResult.config(text=str(plus_db(hobbies_db)))
debtsResult.config(text=str(plus_db(debts_db)))
display_expenses_data()
expenses_results.config(text=(str(totalExpenses)))

salary_result.config(text=str(plus_db(salary_db)))
consulting_result.config(text=str(plus_db(consulting_earnings_db)))
hobbies_earns_result.config(text=str(plus_db(hobbies_earnings_db)))
other_result.config(text=str(plus_db(other_earnings_db)))
display_earns_data()
earnings_results.config(text=str(totalEarnings))

mainWindow.mainloop()
