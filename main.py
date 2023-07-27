from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json


# ---------------------------- PASSWORD Search ------------------------------- #
def search():
    Search.config(bg="blue")
    try:
        # loading and updating the data
        with open(file="data.json", mode="r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
         messagebox.showinfo(title="Search password",message="No file found")
    try:
        web = web_entry.get()
        Pass = data[web]["Password"]
        Found_pass = messagebox.showinfo(title="Search password",message=f"Website: {web}\nPassword: {Pass}")
        # Password_entry.insert(0, data[web]["Password"])
        if Found_pass:
           pyperclip.copy(data[web]["Password"])  # copy the searched password to clipboard
    except (KeyError):
         messagebox.showinfo(title="Search password",message="no such wedsite")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters_list = list(string.ascii_letters)
    numbers_list = [str(i) for i in range(10)]
    symbols_list = ['!', '#', '$', '%', '(', ')', '*', '+']

    password_list = []

    while len(password_list) < 8:
        password_list.append(random.choice(letters_list))
        password_list.append(random.choice(numbers_list))
        password_list.append(random.choice(symbols_list))
    generated_password = "".join(password_list)
    Password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)  # this is to copy the password to the clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    web = web_entry.get()
    Pass = Password_entry.get()
    email = Email_entry.get()
    new_data = {
        web: {
            "email": email,
            "Password": Pass

        }
    }
    if not web or not Pass:
        retry_msg = messagebox.showinfo(title="missing info", message="please enter complete information")

    if web and Pass:
        confirmation_msg = messagebox.askokcancel(title=web, message=f"these are thr details \nEmail: {email}\n"
                                                                     f"Password: {Pass}")
        if confirmation_msg:
            try:
                # loading and updating the data
                with open(file="data.json", mode="r") as file:
                    data = json.load(file)

            except (FileNotFoundError, json.decoder.JSONDecodeError):
                # Writing the new data into the file in JSON format
                with open(file="data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open(file="data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_entry.delete(0, END)
                Password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


# Create the main tkinter window
windows = Tk()
windows.title("Password Manager")
windows.minsize(width=500, height=300)
# Load the image using PhotoImage
photo = PhotoImage(file="logo.png")
# Create a canvas with a specific width and height
canvas = Canvas(windows, width=500, height=300)
canvas.grid(column=1, row=0, padx=20, pady=20)
# Place the image on the canvas at the center (you can adjust x and y as needed)
x = 250
y = 150
canvas.create_image(x, y, image=photo)

# Labels
website = Label(text="website")
website.grid(column=0, row=1, sticky=W, pady=1)
Email = Label(text="Email/Username")
Email.grid(column=0, row=2, sticky="w")
Password = Label(text="Password:")
Password.grid(column=0, row=3, sticky="w")

# entries
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, pady=1)
web_entry.focus()
Email_entry = Entry(width=35)
Email_entry.grid(column=1, row=2, columnspan=2)
Email_entry.insert(0, "rijjafarhan2@gmail.com")  # this is to have a popup of this email
Password_entry = Entry(width=21)
Password_entry.grid(column=1, row=3)

# buttons
generate_password = Button(text="Generate Password", command=generate_pass)
generate_password.grid(column=2, row=3)
Add = Button(text="Add", width=36, command=save_data)
Add.grid(column=1, row=4, columnspan=2)
Search = Button(text="Search", width=10, command=search)
Search.grid(column=2, row=1)

# Run the main tkinter event loop
windows.mainloop()
