import tkinter as tk


cal = tk.Tk()
cal.title("Calculatrice")

def click(number):
    global operator
    operator = operator + str(number)
    variable.set(operator)

def clear():
    global operator
    operator = ""
    variable.set(operator)

def sum():
    global operator
    operator = str(eval(operator))
    variable.set(operator)


operator=""
variable = tk.StringVar()
display = tk.Entry(cal, textvariable=variable, justify = "right")
display.grid(columnspan=5)

button7 = tk.Button(cal,text="7", pady=6, padx=12, command = lambda : click(7))
button7.grid(row=1,column=0)

button8 = tk.Button(cal,text="8", pady=6, padx=12, command = lambda : click(8))
button8.grid(row=1,column=1)

button9 = tk.Button(cal,text="9", pady=6, padx=12, command = lambda : click(9))
button9.grid(row=1,column=2)

button4 = tk.Button(cal,text="4", pady=6, padx=12, command = lambda : click(4))
button4.grid(row=2,column=0)

button5 = tk.Button(cal,text="5", pady=6, padx=12, command = lambda : click(5))
button5.grid(row=2,column=1)

button6 = tk.Button(cal,text="6", pady=6, padx=12, command = lambda : click(6))
button6.grid(row=2,column=2)

button1 = tk.Button(cal,text="1", pady=6, padx=12, command = lambda : click(1))
button1.grid(row=3,column=0)

button2 = tk.Button(cal,text="2", pady=6, padx=12, command = lambda : click(2))
button2.grid(row=3,column=1)

button3 = tk.Button(cal,text="3", pady=6, padx=12, command = lambda : click(3))
button3.grid(row=3,column=2)

button0 = tk.Button(cal,text="0", pady=6, padx=12, command = lambda : click(0))
button0.grid(row=4,column=0)

buttonclear = tk.Button(cal,text="C", pady=5, padx=11, command = clear)
buttonclear.grid(row=4,column=2)

buttonpoint = tk.Button(cal,text=".", pady=6, padx=14, command = lambda : click("."))
buttonpoint.grid(row=4,column=1)

buttondivi = tk.Button(cal,text="/", pady=6, padx=13, command = lambda : click("/"))
buttondivi.grid(row=1,column=3)

buttonmulti = tk.Button(cal,text="*", pady=6, padx=12, command = lambda : click("*"))
buttonmulti.grid(row=2,column=3)

buttonminus = tk.Button(cal,text="-", pady=6, padx=12, command = lambda : click("-"))
buttonminus.grid(row=3, column=3)

buttonplus = tk.Button(cal,text="+",pady=21, padx=11, command = lambda : click("+"))
buttonplus.grid(row=4, column=3, rowspan=2)

buttonequal = tk.Button(cal,text="=", pady=6, padx=60, command = sum)
buttonequal.grid(row=5, column=0, columnspan=3)


cal.mainloop()
