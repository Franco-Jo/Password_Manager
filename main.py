from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ("Ariel", 11, "bold")

# ------------------------------- LOGIN SEARCH ---------------------------------- #


def search():
    """Searches for login info that matches text in the search Entry box"""
    website = web_entry.get()

    try:
        with open('data.json', 'r') as file:
            login_data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="hmmmmm....", message="Sorry, data file not found.")
    else:
        if website in login_data:
            email = login_data[website]["email_name"]
            passw = login_data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword:{passw}")
        else:
            messagebox.showwarning(title='error', message="No information found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """generates random password and copies to clipboard"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    char_list = [choice(letters) for _ in range(randint(8, 10))]
    sym_list = [choice(symbols) for _ in range(randint(2, 4))]
    num_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = char_list + sym_list + num_list

    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    """writes user info to file"""
    website = web_entry.get()
    email_name = email_us_entry.get()
    password = pass_entry.get()

    new_data = {
        website: {
            "email_name": email_us_entry.get(),
            "password": pass_entry.get()
        }
    }

    if len(website) == 0 or len(email_name) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as file:
                # Reading old data
                data = json.load(file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', "w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
        else:
            with open('data.json', "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

web_lbl = Label(text="Website:", font=FONT)
web_lbl.grid(column=0, row=1, sticky='W')

email_un_lbl = Label(text="Email/Username:", font=FONT)
email_un_lbl.grid(column=0, row=2, sticky='W')

pass_lbl = Label(text="Password:", font=FONT)
pass_lbl.grid(column=0, row=3, sticky='W')

web_entry = Entry(width=33)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2, sticky='W')

email_us_entry = Entry(width=58)
email_us_entry.insert(0, "Jonathan.f651@gmail.com")
email_us_entry.grid(column=1, row=2, columnspan=2, sticky='W')

pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3, sticky='W')

gen_btn = Button(text="Generate Password", width=15, font=FONT, command=generate_password)
gen_btn.grid(column=2, row=3, sticky='W')

add_btn = Button(text="Add", width=36, font=FONT, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky='W')

search_btn = Button(text="Search", width=15, font=FONT, command=search)
search_btn.grid(column=2, row=1, sticky='W')

window.mainloop()
