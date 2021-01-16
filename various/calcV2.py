from tkinter import *

first_value = .0
operation = ''
operation_equals = ''
result = .0


def d_calc_v2():
    calc_v2_window = Toplevel()
    calc_v2_window.title('D Calc V2')
    calc_v2_window.config(bg='snow')
    calc_frame = Frame(calc_v2_window, bg='snow')
    calc_frame.pack(padx=5, pady=5)
    # ---------- Display ----------
    display_data = StringVar()
    display = Entry(calc_frame, textvariable=display_data)
    display.grid(row=1, column=1, padx=5, pady=5, columnspan=4, ipady=6)
    display.config(bg='darkgrey', fg='black', justify=RIGHT, width=45, borderwidth=2)
    display.insert(0, '0')

    # ----------Display Print ----------

    def print_display(parameter):
        global operation
        if display_data.get() == '0':
            display.delete(0, END)
        if operation != '':
            display_data.set(parameter)
            operation = ''
        else:
            display_data.set(display_data.get() + parameter)

    def add(value_display):
        global operation_equals
        global result
        global operation
        result += float(value_display)
        operation = '+'
        operation_equals = '+'
        display_data.set(result)

    def subtraction(value_display):
        global operation_equals
        global result
        global operation
        result -= float(value_display)
        operation = '-'
        operation_equals = '-'
        display_data.set(result)

    def division():
        global first_value
        global operation
        operation = '/'
        first_value = float(display_data.get())
        display.delete(0, END)

    def multi():
        global first_value
        global operation
        operation = '*'
        first_value = float(display_data.get())
        display.delete(0, END)

    def clean():
        if display_data.get() == '0':
            return
        else:
            global first_value
            display.delete(0, END)
            first_value = .0
            display.insert(0, '0')

    def module():
        global first_value
        global operation
        operation = '%'
        first_value = float(display_data.get())
        display.delete(0, END)

    def power():
        global first_value
        global operation
        operation = '^'
        first_value = float(display_data.get())
        display.delete(0, END)

    def sign():
        sign_change = float(display_data.get()) * -1
        display.delete(0, END)
        display.insert(0, str(sign_change))

    def equals():
        global result
        second_value = float(display_data.get())
        # display.delete(0, END)
        if operation_equals == '+':
            display_data.set(result + float(display_data.get()))
            result = .0

            # res = first_value + second_value
            # display.insert(0, str(res))
        elif operation == '-':
            res = first_value - second_value
            display.insert(0, str(res))
        elif operation == '*':
            res = first_value * second_value
            display.insert(0, str(res))
        elif operation == '/':
            if second_value != 0:
                res = first_value / second_value
                display.insert(0, str(res))
            else:
                display.insert(0, 'ERROR: Division/0 is undetermined')
        elif operation == '%':
            res = first_value % second_value
            display.insert(0, str(res))
        elif operation == '^':
            res = first_value ** second_value
            display.insert(0, str(res))

        # ---------- Buttons ----------

    button7 = Button(calc_frame, text='7', width=10, height=2, command=lambda: print_display('7'))
    button7.grid(row=2, column=1)
    button8 = Button(calc_frame, text='8', width=10, height=2, command=lambda: print_display('8'))
    button8.grid(row=2, column=2)
    button9 = Button(calc_frame, text='9', width=10, height=2, command=lambda: print_display('9'))
    button9.grid(row=2, column=3)
    button_cos = Button(calc_frame, text='/', width=10, height=2, command=division)
    button_cos.grid(row=2, column=4)

    button4 = Button(calc_frame, text='4', width=10, height=2, command=lambda: print_display('4'))
    button4.grid(row=3, column=1)
    button5 = Button(calc_frame, text='5', width=10, height=2, command=lambda: print_display('5'))
    button5.grid(row=3, column=2)
    button6 = Button(calc_frame, text='6', width=10, height=2, command=lambda: print_display('6'))
    button6.grid(row=3, column=3)
    button_multi = Button(calc_frame, text='*', width=10, height=2, command=multi)
    button_multi.grid(row=3, column=4)

    button1 = Button(calc_frame, text='1', width=10, height=2, command=lambda: print_display('1'))
    button1.grid(row=4, column=1)
    button2 = Button(calc_frame, text='2', width=10, height=2, command=lambda: print_display('2'))
    button2.grid(row=4, column=2)
    button3 = Button(calc_frame, text='3', width=10, height=2, command=lambda: print_display('3'))
    button3.grid(row=4, column=3)
    button_minus = Button(calc_frame, text='-', width=10, height=2, command=lambda: subtraction(display_data.get()))
    button_minus.grid(row=4, column=4)

    button0 = Button(calc_frame, text='0', width=10, height=2, command=lambda: print_display('0'))
    button0.grid(row=5, column=1)
    button_dot = Button(calc_frame, text='.', width=10, height=2, command=lambda: print_display('.'))
    button_dot.grid(row=5, column=2)
    button_power = Button(calc_frame, text='^', width=10, height=2, command=power)
    button_power.grid(row=5, column=3)
    button_plus = Button(calc_frame, text='+', width=10, height=2, command=lambda: add(display_data.get()))
    button_plus.grid(row=5, column=4)

    button_clean_display = Button(calc_frame, text='C', width=10, height=2, command=clean)
    button_clean_display.grid(row=6, column=1)
    button_module = Button(calc_frame, text='%', width=10, height=2, command=module)
    button_module.grid(row=6, column=2)
    button_equals = Button(calc_frame, text='=', width=10, height=2, command=lambda: equals())
    button_equals.grid(row=6, column=3)
    button_sign = Button(calc_frame, text='+/-', width=10, height=2, command=sign)
    button_sign.grid(row=6, column=4)

    calc_v2_window.mainloop()


root = Tk()
root.geometry('500x500')
root.title('Main App')
root.resizable(False, False)
root.config(bg='lightgreen')
mainFrame = Frame(root, bg='brown', height=500, width=500)
mainFrame.pack(padx=10, pady=10)
calcButton = Button(mainFrame, bg='green', text='Calc V 2.0', command=d_calc_v2).place(x=200, y=200)

root.mainloop()
