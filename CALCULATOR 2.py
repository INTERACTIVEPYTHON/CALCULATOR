# import everything from tkinter module
from tkinter import *
expression = ""

# Function to update expression
def press(num):

  global expression

  # concatenation of string
  expression = expression + str(num)


  equation.set(expression)


# Function to evaluate the final expression
def equal():
  if equation !=0 :

    global expression
    total = str(eval(expression))

    equation.set(total)

    expression = ""

  else:

    equation.set(" error ")
    expression = ""


# Function to clear the contents
def clear():
  global expression
  expression = ""
  equation.set("")

if __name__ == "__main__":
    #window
    gui = Tk()

    

    # set the title
    gui.title("Simple Calculator")
  
    gui.geometry("328x325")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation)

    expression_field.grid(columnspan=5, ipadx=100)

    equation.set('0')

    # create Buttons
    button1 = Button(gui, text=' 1 ', font=('arial',10,'bold'),fg='black', bg='red',command=lambda: press(1), height=4, width=9)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', font=('arial',10,'bold'), fg='black', bg='red',command=lambda: press(2), height=4, width=9)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', font=('arial',10,'bold'), fg='black', bg='red',command=lambda: press(3), height=4, width=9)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', font=('arial',10,'bold'), fg='black', bg='blue',command=lambda: press(4), height=4, width=9)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', font=('arial',10,'bold'), fg='black', bg='blue',command=lambda: press(5), height=4, width=9)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', font=('arial',10,'bold'), fg='black', bg='blue',command=lambda: press(6), height=4, width=9)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', font=('arial',10,'bold'), fg='black', bg='green',command=lambda: press(7), height=4, width=9)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', font=('arial',10,'bold'), fg='black', bg='green',command=lambda: press(8), height=4, width=9)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', font=('arial',10,'bold'), fg='black', bg='green',command=lambda: press(9), height=4, width=9)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', font=('arial',10,'bold'), fg='black', bg='yellow',command=lambda: press(0), height=4, width=9)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', font=('arial',10,'bold'), fg='black', bg='yellow',command=lambda: press("+"), height=4, width=9)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', font=('arial',10,'bold'), fg='black', bg='light green',command=lambda: press("-"), height=4, width=9)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', font=('arial',10,'bold'), fg='black', bg='light blue',command=lambda: press("*"), height=4, width=9)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', font=('arial',10,'bold'), fg='black', bg='light green',command=lambda: press("/"), height=4, width=9)
    divide.grid(row=5, column=1)

    equal = Button(gui, text=' = ', font=('arial',10,'bold'), fg='black', bg='light blue', command=equal, height=4, width=9)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', font=('arial',10,'bold'), fg='black', bg='purple',command=clear, height=4, width=9)
    clear.grid(row=5, column
=3)

    #RUN
    gui.mainloop()
