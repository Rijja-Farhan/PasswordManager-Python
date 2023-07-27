from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters_list = list(string.ascii_letters)
    numbers_list = [str(i) for i in range(10)]
    symbols_list = ['!','#','$','%','(',')','*','+' ]

    password_list = []

    while len(password_list) < 8:
        password_list.append(random.choice(letters_list))
        password_list.append(random.choice(numbers_list))
        password_list.append(random.choice(symbols_list))
    generated_password = "".join(password_list)
    Password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password) #this is to copy the password to the clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    web = web_entry.get()
    Pass = Password_entry.get()
    email =Email_entry.get()
    if not web or not Pass:
        retry_msg = messagebox.showinfo(title="missing info",message="please enter complete information")

    if web and Pass:
        confirmation_msg = messagebox.askokcancel(title=web,message=f"these are thr details \nEmail: {email}\n"
                                                                    f"Password: {Pass}")
        if confirmation_msg:
            with open(file = "data.txt",mode ="a") as file:
                file.write(f" {web} | {email} |  {Pass} \n")
                web_entry.delete(0,END)
                Password_entry.delete(0,END)




# ---------------------------- UI SETUP ------------------------------- #



# Create the main tkinter window
windows = Tk()
windows.title("Password Manager")
windows.minsize(width=500,height=300)
# Load the image using PhotoImage
photo = PhotoImage(file="logo.png")
# Create a canvas with a specific width and height
canvas = Canvas(windows, width=500, height=300)
canvas.grid(column=1, row=0,padx=20,pady=20)
# Place the image on the canvas at the center (you can adjust x and y as needed)
x = 250
y = 150
canvas.create_image(x, y, image=photo)

#Labels
website =Label(text ="website")
website.grid(column=0,row=1,sticky = W, pady = 1)
Email=Label(text ="Email/Username")
Email.grid(column=0, row=2, sticky="w")
Password =Label(text ="Password:")
Password.grid(column=0, row=3, sticky="w")

#entries
web_entry =Entry(width=35)
web_entry.grid(column=1,row=1,columnspan=2,pady = 1)
web_entry.focus()
Email_entry =Entry(width=35)
Email_entry.grid(column=1,row=2,columnspan=2)
Email_entry.insert(0,"rijjafarhan2@gmail.com") #this is to have a popup of this email
Password_entry =Entry(width=21)
Password_entry.grid(column=1,row=3)

#buttons
generate_password = Button(text="Generate Password",command=generate_pass)
generate_password.grid(column=2,row =3)
Add = Button(text="Add",width=36,command=save_data)
Add.grid(column=1,row =4,columnspan=2)


# Run the main tkinter event loop
windows.mainloop()
