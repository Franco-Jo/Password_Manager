from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = ("Ariel", 11, "bold")


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

    if len(website) == 0 or len(email_name) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/Username: "
                                                              f"{email_name} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("./login_info.txt", 'a') as file:
                file.write(f'{website} | {email_name} | {password}\n')
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

web_entry = Entry(width=61)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2, sticky='W')

email_us_entry = Entry(width=61)
email_us_entry.insert(0, "Jonathan.f651@gmail.com")
email_us_entry.grid(column=1, row=2, columnspan=2, sticky='W')

pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3, sticky='W')

gen_btn = Button(text="Generate Password", width=15, font=FONT, command=generate_password)
gen_btn.grid(column=2, row=3, sticky='e')

add_btn = Button(text="Add", width=36, font=FONT, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky='W')

window.mainloop()
