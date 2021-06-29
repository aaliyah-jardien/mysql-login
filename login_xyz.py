from tkinter import *
from tkinter import messagebox

# WINDOW FEATURES
window = Tk()
window.geometry("500x250")
window.title("Login page")
window.config(bg="silver")
window.resizable(0, 0)

# LABELS
name_lab = Label(window, text="Please enter username :", font="arial 13 bold italic", bg="lime")
name_lab.place(x=30, y=30)

pass_lab = Label(window, text="Please enter password: ", font="arial 13 bold italic", bg="lime")
pass_lab.place(x=30, y=70)

# ENTRIES
name_ent = Entry(window, bg="lime")
name_ent.place(x=280, y=30)

pass_ent = Entry(window, bg="lime", show="*")
pass_ent.place(x=280, y=70)

# @Lifechoices1234
# FUNCTIONS
def clear_func():
    sure = messagebox.askyesno(title="Alert", message="Are you sure you want to clear your information?")
    if sure:
        name_ent.delete(0, END)
        pass_ent.delete(0, END)

    else:
        return None

# def login_func():



# BUTTONS
clear_btn = Button(window, text="Clear", command=clear_func, font="arial 12 bold", bg="lime", border="5")
clear_btn.place(x=30, y=140)

login_btn = Button(window, text="Login", command="", font="arial 12 bold", bg="lime", border="5")
login_btn.place(x=200, y=140)

regis_btn = Button(window, text="Register", command="", font="arial 12 bold", bg="lime", border="5")
regis_btn.place(x=340, y=140)

# FIN
window.mainloop()
