from tkinter import*
import math

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
    
    def display(self, value):
        display.delete(0, END)
        display.insert(0, value)
    
    def num_enter(self, num):
        self.result = False
        first_num = display.get()
        sec_num = str(num)
        # if a new number is entered
        if self.input_value:
            self.current = sec_num
            self.input_value = False
        else:
            #if a decimal point is enetered to make a decimal value
            if sec_num == '.':
                if sec_num in first_num:
                    return
            self.current = first_num + sec_num
        self.display(self.current)
    
    def total_sum(self):
        self.result = True
        self.current = float(self.current) #to display result in float(decimal)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(display.get())

    def valid_function(self):
        if self.op == 'add':
            self.total += self.current
        if self.op == 'sub':
            self.total -= self.current
        if self.op == 'mul':
            self.total *= self.current
        if self.op == 'div':
            self.total /= self.current

        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True
    
    def clear_all(self):
        self.clear_entry()
        self.total = 0

    def plusminus(self):
        self.result = False
        self.current = -(float(display.get()))
        self.display(self.current)
    
    def sqrt(self):
        self.result = False
        self.current = math.sqrt(float(display.get()))
        self.display(self.current)



val_entered = Calc()
root = Tk()
root.title("Calculator") #setting the title to be displayed
root.resizable(width=False, height=False) #it will not allow the user to resize the calculator window
calc = Frame(root) #making a frame and setting it to calc
calc.grid() #to display the main frame of calculator

#ROW0
display = Entry(calc, font=('arial', 13, 'bold'), bg="#87CEFA", bd=30, width=28, justify = RIGHT)
display.grid(row=0, column=0, columnspan=4, pady=1) #making the display at row & column 0 and columnspan will make the display cover 4 rows, pady will give padding to yaxis
display.insert(0, "0")

#ROW1
#displaying the buttons by adding the color,size,font and other attributes and the button will be displayed at location given in .grid() row and column
btn_ce = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='CE', bg="white", command = val_entered.clear_entry).grid(row=1, column=0)
btn_c = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='C', bg="white", command = val_entered.clear_all).grid(row=1, column=1)
btn_sqrt = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='√', bg="white", command = val_entered.sqrt).grid(row=1, column=2)
btn_div = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='/', bg="white", command = lambda: val_entered.operation('div')).grid(row=1, column=3)

#ROW2
btn_7 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='7', bg="white", command = lambda: val_entered.num_enter(7)).grid(row=2, column=0)
btn_8 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='8', bg="white", command = lambda: val_entered.num_enter(8)).grid(row=2, column=1)
btn_9 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='9', bg="white", command = lambda: val_entered.num_enter(9)).grid(row=2, column=2)
btn_mul = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='*', bg="white", command = lambda: val_entered.operation('mul')).grid(row=2, column=3)

#ROW3
btn_4 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='4', bg="white", command = lambda: val_entered.num_enter(4)).grid(row=3, column=0)
btn_5 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='5', bg="white", command = lambda: val_entered.num_enter(5)).grid(row=3, column=1)
btn_6 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='6', bg="white", command = lambda: val_entered.num_enter(6)).grid(row=3, column=2)
btn_sub = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='-', bg="white", command = lambda: val_entered.operation('sub')).grid(row=3, column=3)

#ROW4
btn_1 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='1', bg="white", command = lambda: val_entered.num_enter(1)).grid(row=4, column=0)
btn_2 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='2', bg="white", command = lambda: val_entered.num_enter(2)).grid(row=4, column=1)
btn_3 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='3', bg="white", command = lambda: val_entered.num_enter(3)).grid(row=4, column=2)
btn_add = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='+', bg="white", command = lambda: val_entered.operation('add')).grid(row=4, column=3)

#ROW5
btn_pm = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text=chr(177), bg="white", command = val_entered.plusminus).grid(row=5, column=0)
btn_0 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='0', bg="white", command = lambda: val_entered.num_enter(0)).grid(row=5, column=1)
btn_dec = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='.', bg="white", command = lambda: val_entered.num_enter('.')).grid(row=5, column=2)
btn_eql = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2, text='=', bg="#87CEFA", command = val_entered.total_sum).grid(row=5, column=3)


root.mainloop()
