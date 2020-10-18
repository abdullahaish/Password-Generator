# Python program to generate random 
# password using Tkinter module 
import random 
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
import pyperclip
import time

# Function for calculation of password 
def low(): 
	# entry.delete(0, END) 

	# Get the length of passowrd 
	length = var1.get() 

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()[]{};:'<>"
	password = "" 

	# if strength selected is low 
	if var.get() == 1: 
		for i in range(0, length): 
			password = password + random.choice(lower) 
		return password 

	# if strength selected is medium 
	elif var.get() == 0: 
		for i in range(0, length): 
			password = password + random.choice(upper) 
		return password 

	# if strength selected is strong 
	elif var.get() == 3: 
		for i in range(0, length): 
			password = password + random.choice(digits) 
		return password 
	else: 
		print("Please choose an option") 


# Function for generation of password 
def generate(): 
	global entry
	global auto_btn
	if combo.get() == "" or combo.get() == "Length":
		messagebox.showwarning("Warning", "Please Enter Length!")
		# messagebox.showinfo("Show Info", "Message Box")
	else:
		root.geometry("290x120")
		password1 = low() 
		Random_password = Label(root, text="Password: ") 
		Random_password.grid(row=3) 
		entry = Entry(root) 
		entry.grid(row=3, column=1, pady=5) 
		entry.insert(10, password1) 
		messagebox.showinfo("Password Generator", "Password Generate Successfully!")
		msg = messagebox.askyesno("Password Generator", "Do You Want To Copy Password?")
		if msg == True:
			copy_button = Button(root, text="Copy", command=copy1) 
			copy_button.grid(row=3, column=2, padx=5)
			root.geometry("375x120")
			auto_btn = Button(root, text="Auto", comman=auto)
			auto_btn.grid(row=3, column=3, padx=5)
				


def copy1(): 
	random_password = entry.get() 
	pyperclip.copy(random_password) 
	
def auto():
	msg1 = messagebox.askyesno("Password Generator", "Do You Want To Change Password Automatically?")
	if msg1 == False:
		root.geometry("290x120")
	else:
		time.sleep(10)
		generate()

# Main Function 

# create GUI window 
root = Tk() 
root.iconbitmap("pass.ico")
root.geometry("300x90")
var = IntVar() 
var1 = IntVar() 

# Title of your GUI window 
root.title("Password Generator") 

# create label for length of password 
c_label = Label(root, text="Length: ") 
c_label.grid(row=0, pady=5) 


generate_button = Button(root, text="Generate", command=generate) 
generate_button.grid(row=2, column=1, pady=5)  

# Radio Buttons for deciding the 
# strength of password 
# Default strength is Medium 
radio_low = Radiobutton(root, text="Low", variable=var, value=1) 
radio_low.grid(row=1, column=0) 
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0) 
radio_middle.grid(row=1, column=1) 
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3) 
radio_strong.grid(row=1, column=2) 
combo = Combobox(root, textvariable=var1) 

# Combo Box for length of your password 
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
				17, 18, 19, 20, 21, 22, 23, 24, 25, 
				26, 27, 28, 29, 30, 31, 32, "Length") 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.set("")
combo.grid(column=1, row=0) 

# start the GUI 
root.mainloop() 
