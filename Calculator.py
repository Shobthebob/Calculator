from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")
root.geometry("186x234")
root.resizable(0,0)

def command(n1):
	cur = Output.get( )
	if(not str(n1).isnumeric()):
		Bp.config(state="disabled")
		Bmi.config(state="disabled")
		Bmu.config(state="disabled")
		Bd.config(state="disabled")
		Bpe.config(state="disabled")
		Bdot.config(state="disabled")
	else:
		Bp.config(state="enabled")
		Bmi.config(state="enabled")
		Bmu.config(state="enabled")
		Bd.config(state="enabled")
		Bpe.config(state="enabled")

	if(str(n1)=="."):
		Bdot.config(state="disabled")
	if(cur!="") and ((cur[-1]=='+') or (cur[-1]=='-') or (cur[-1]=='*') or (cur[-1]=='/') or (cur[-1]=='%')):
		Bdot.config(state="enabled")
			
	Output.delete(0, END)
	Output.insert(0, str(cur) + str(n1))
			
def clear():
	Output.delete(0, END)

def result():
	s = Output.get( )
	Output.delete(0, END)
	Output.insert(0, eval(s))

Output = Entry(root, width=30)
Output.grid(row=0, column=0, ipady=10, columnspan=4)
# Output.configure(state="disabled")

B1 = ttk.Button(root, text="1", width=6, command=lambda: command(1))
B1.grid(row=4, column=0, ipady=7)

B2 = ttk.Button(root, text="2", width=6, command=lambda: command(2))
B2.grid(row=4, column=1, ipady=7)

B3 = ttk.Button(root, text="3", width=6, command=lambda: command(3))
B3.grid(row=4, column=2, ipady=7)

B4 = ttk.Button(root, text="4", width=6, command=lambda: command(4))
B4.grid(row=3, column=0, ipady=7)

B5 = ttk.Button(root, text="5", width=6, command=lambda: command(5))
B5.grid(row=3, column=1, ipady=7)

B6 = ttk.Button(root, text="6", width=6, command=lambda: command(6))
B6.grid(row=3, column=2, ipady=7)

B7 = ttk.Button(root, text="7", width=6, command=lambda: command(7))
B7.grid(row=2, column=0, ipady=7)

B8 = ttk.Button(root, text="8", width=6, command=lambda: command(8))
B8.grid(row=2, column=1, ipady=7)

B9 = ttk.Button(root, text="9", width=6, command=lambda: command(9))
B9.grid(row=2, column=2, ipady=7)

B0 = ttk.Button(root, text="0", width=6, command=lambda: command(0))
B0.grid(row=5, column=0, ipady=7)

Bdot = ttk.Button(root, text=".", width=6, command=lambda: command("."))
Bdot.grid(row=5, column=1, ipady=7)

Bp = ttk.Button(root, text="+", width=6, command=lambda: command("+"))
Bp.grid(row=4, column=3, ipady=7)

Bmi = ttk.Button(root, text="-", width=6, command=lambda: command("-"))
Bmi.grid(row=3, column=3, ipady=7)

Bmu = ttk.Button(root, text="X", width=6, command=lambda: command("*"))
Bmu.grid(row=2, column=3, ipady=7)

Bd = ttk.Button(root, text="/", width=6, command=lambda: command("/"))
Bd.grid(row=1, column=3, ipady=7)

Be = ttk.Button(root, text="=", width=14, command=result)
Be.grid(row=5, column=2, ipady=7, columnspan=2)

Bc = ttk.Button(root, text="AC", width=6, command=clear)
Bc.grid(row=1, column=1, ipady=7)

Bb = ttk.Button(root, text="exit", width=6, command=root.destroy)
Bb.grid(row=1, column=0, ipady=7)

Bpe = ttk.Button(root, text="%", width=6, command=lambda: command("%"))
Bpe.grid(row=1, column=2, ipady=7)




root.mainloop()