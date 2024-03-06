from tkinter import *
FONT = ("Ariel", 12, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
web_entry.grid(column=1, row=1, columnspan=2, sticky='W')

email_us_entry = Entry(width=61)
email_us_entry.grid(column=1, row=2, columnspan=2, sticky='W')

pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3, sticky='W')

gen_btn = Button(text="Generate Password", width=15, font=FONT)
gen_btn.grid(column=2, row=3, sticky='e')

add_btn = Button(text="Add", width=36, font=FONT)
add_btn.grid(column=1, row=4, columnspan=2, sticky='W')


window.mainloop()
