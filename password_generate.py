from tkinter import *
from tkinter import ttk
import random

root = Tk()

# Title of your GUI window 
root.title("Random Password Generator") 

# Size of you window
root.geometry("500x150")

# Icon of your window
root.iconbitmap("pass.ico")

# Create Function
def low():  
	# Get the length of passowrd 
	length = mycombo.get() 

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = "" 

	# if strength selected is low 
	if length == "Low": 
		for i in range(0, length): 
			password = password + random.choice(lower) 
		return password  

	# if strength selected is medium 
	if length == "Medium": 
		for i in range(0, length): 
			password = password + random.choice(upper) 
		return password 

	# if strength selected is strong 
	if length == "High": 
		for i in range(0, length): 
			password = password + random.choice(digits) 
		return password  

def generate():
    entry.delete(0, END)
    password = low()
    entry.insert(0, password)

Random_password = Label(root, text="Password: ") 
Random_password.grid(row=2, column=0) 
# entry = Entry(root) 
# entry.grid(row=2, column=1)

length = Label(root, text="Length: ", pady=10).grid(row=0)
# Password Types Low Medium Strong
pass_type = Label(root, text="Type: ").grid(row=1)

# Create Generate Button
generate_Button = Button(root, text="Generate", command=generate).grid(row=3, column=1, padx=5)
# btn = Button(root, text="btn", command= abc).grid(row=3,column=1)

# Create Combo box
options = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, "Length")
type_pas = ["Low" , "Medium", "High"]
mycombo = ttk.Combobox(root, value=options)
mycombo.current(0)
mycombo.bind("<<ComboboxSelected>>")
mycombo.set("Select")
mycombo.grid(row=0, column=1)

var = ttk.Combobox(root, value=type_pas)
var.current(0)
var.bind("<<ComboboxSelected>>")
var.set("Select")
var.grid(row=1, column=1)

root.mainloop()