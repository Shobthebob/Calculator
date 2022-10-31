from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")
root.resizable(0,0)

# Main function that reads the numbers and operations
def command(n1):
	cur = Output.get( ) # The current expression
	
	# To make sure no one uses an operator twice
	if(not str(n1).isnumeric()):
		Bmu.config(state="disabled")
		Bd.config(state="disabled")
		Bpe.config(state="disabled")
		Bdot.config(state="disabled")
	else:
		Bmu.config(state="normal")
		Bd.config(state="normal")
		Bpe.config(state="normal")

	# To make sure no one uses the decimal uneccessarily
	if(str(n1)=="."):
		Bdot.config(state="disabled")
	if(cur!="") and ((cur[-1]=='+') or (cur[-1]=='-') or (cur[-1]=='*') or (cur[-1]=='/') or (cur[-1]=='%')):
		Bdot.config(state="normal")
			
	Output.delete(0, END)
	Output.insert(0, str(cur) + str(n1))

# Function for the AC button on the calc that clears the screen
def clear():
	Output.delete(0, END)

# Function to display the result of the expression
def result():	
	try:
		s = Output.get( )
		Output.delete(0, END)
		Output.insert(0, eval(s))
	except:
		Output.insert(0, "ERROR")

# Creating and Positioning our entry widgit to display everything
Output = Entry(root, width=30)
Output.grid(row=0, column=0, ipady=10, columnspan=4)

# Creating Number Buttons
B1 = Button(root, text="1", width=6, command=lambda: command(1))
B2 = Button(root, text="2", width=6, command=lambda: command(2))
B3 = Button(root, text="3", width=6, command=lambda: command(3))
B4 = Button(root, text="4", width=6, command=lambda: command(4))
B5 = Button(root, text="5", width=6, command=lambda: command(5))
B6 = Button(root, text="6", width=6, command=lambda: command(6))
B7 = Button(root, text="7", width=6, command=lambda: command(7))
B8 = Button(root, text="8", width=6, command=lambda: command(8))
B9 = Button(root, text="9", width=6, command=lambda: command(9))
B0 = Button(root, text="0", width=6, command=lambda: command(0))

# Positioning Number Buttons
B1.grid(row=4, column=0, ipady=7)
B2.grid(row=4, column=1, ipady=7)
B3.grid(row=4, column=2, ipady=7)
B4.grid(row=3, column=0, ipady=7)
B5.grid(row=3, column=1, ipady=7)
B6.grid(row=3, column=2, ipady=7)
B7.grid(row=2, column=0, ipady=7)
B8.grid(row=2, column=1, ipady=7)
B9.grid(row=2, column=2, ipady=7)
B0.grid(row=5, column=0, ipady=7)

# Creating and Positioning the decimal point
Bdot = Button(root, text=".", width=6, command=lambda: command("."))
Bdot.grid(row=5, column=1, ipady=7)

# Creating Operator Buttons
Bp = Button(root, text="+", width=6, command=lambda: command("+"))
Bmi = Button(root, text="-", width=6, command=lambda: command("-"))
Bmu = Button(root, text="X", width=6, command=lambda: command("*"))
Bd = Button(root, text="/", width=6, command=lambda: command("/"))
Bpe = Button(root, text="%", width=6, command=lambda: command("%"))

# Positioning Operator Buttons
Bp.grid(row=4, column=3, ipady=7)
Bmi.grid(row=3, column=3, ipady=7)
Bmu.grid(row=2, column=3, ipady=7)
Bd.grid(row=1, column=3, ipady=7)
Bpe.grid(row=1, column=2, ipady=7)

Be = Button(root, text="=", width=14, command=result)
Be.grid(row=5, column=2, ipady=7, columnspan=2)

Bc = Button(root, text="AC", width=6, command=clear)
Bc.grid(row=1, column=1, ipady=7)

Bb = Button(root, text="exit", width=6, command=root.destroy)
Bb.grid(row=1, column=0, ipady=7)

# To make sure no one starts with an operator
if(Output.get()==""):
	Bmu.config(state="disabled")
	Bd.config(state="disabled")
	Bpe.config(state="disabled")

root.mainloop()