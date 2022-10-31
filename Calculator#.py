from customtkinter import *

root = CTk()
root.title("Calculator")
root.geometry("200x265")
# root.resizable(0,0)

# Main function that reads the numbers and operations
def command(n1):
	cur = Output.get( ) # The current expression
	
	# To make sure no one uses an operator twice
	if(not str(n1).isnumeric()):
		Bmu.configure(state="disabled")
		Bd.configure(state="disabled")
		Bpe.configure(state="disabled")
		Bdot.configure(state="disabled")
	else:
		Bmu.configure(state="normal")
		Bd.configure(state="normal")
		Bpe.configure(state="normal")

	# To make sure no one uses the decimal uneccessarily
	if(str(n1)=="."):
		Bdot.configure(state="disabled")
	if(cur!="") and ((cur[-1]=='+') or (cur[-1]=='-') or (cur[-1]=='*') or (cur[-1]=='/') or (cur[-1]=='%')):
		Bdot.configure(state="normal")
			
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
		Output.configure(0, "ERROR")

# Creating and Positioning our entry widgit to display everything
Output = CTkEntry(root)
Output.grid(row=0, column=0, ipady=8, ipadx=16, columnspan=4)

# Creating Number Buttons
B1 = CTkButton(root, text="1", width=50, border_color="black", border_width=4, command=lambda: command(1))
B2 = CTkButton(root, text="2", width=50, border_color="black", border_width=4, command=lambda: command(2))
B3 = CTkButton(root, text="3", width=50, border_color="black", border_width=4, command=lambda: command(3))
B4 = CTkButton(root, text="4", width=50, border_color="black", border_width=4, command=lambda: command(4))
B5 = CTkButton(root, text="5", width=50, border_color="black", border_width=4, command=lambda: command(5))
B6 = CTkButton(root, text="6", width=50, border_color="black", border_width=4, command=lambda: command(6))
B7 = CTkButton(root, text="7", width=50, border_color="black", border_width=4, command=lambda: command(7))
B8 = CTkButton(root, text="8", width=50, border_color="black", border_width=4, command=lambda: command(8))
B9 = CTkButton(root, text="9", width=50, border_color="black", border_width=4, command=lambda: command(9))
B0 = CTkButton(root, text="0", width=50, border_color="black", border_width=4, command=lambda: command(0))

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
Bdot = CTkButton(root, text=".", width=50, border_color="black", border_width=4, command=lambda: command("."))
Bdot.grid(row=5, column=1, ipady=7)

# Creating Operator Buttons
Bp = CTkButton(root, text="+", width=50, border_color="black", border_width=4, command=lambda: command("+"))
Bmi = CTkButton(root, text="-", width=50, border_color="black", border_width=4, command=lambda: command("-"))
Bmu = CTkButton(root, text="X", width=50, border_color="black", border_width=4, command=lambda: command("*"))
Bd = CTkButton(root, text="/", width=50, border_color="black", border_width=4, command=lambda: command("/"))
Bpe = CTkButton(root, text="%", width=50, border_color="black", border_width=4, command=lambda: command("%"))

# Positioning Operator Buttons
Bp.grid(row=4, column=3, ipady=7)
Bmi.grid(row=3, column=3, ipady=7)
Bmu.grid(row=2, column=3, ipady=7)
Bd.grid(row=1, column=3, ipady=7)
Bpe.grid(row=1, column=2, ipady=7)

Be = CTkButton(root, text="=", width=100, border_color="black", border_width=4, command=result)
Be.grid(row=5, column=2, ipady=7, columnspan=2)

Bc = CTkButton(root, text="AC", width=50, border_color="black", border_width=4, command=clear)
Bc.grid(row=1, column=1, ipady=7)

Bb = CTkButton(root, text="exit", width=50, border_color="black", border_width=4, command=root.destroy)
Bb.grid(row=1, column=0, ipady=7)

# To make sure no one starts with an operator
if(Output.get()==""):
	Bmu.configure(state="disabled")
	Bd.configure(state="disabled")
	Bpe.configure(state="disabled")

root.mainloop()