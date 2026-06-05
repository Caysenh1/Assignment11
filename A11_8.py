import ttkbootstrap as ttk

import tkinter.messagebox as mbox

window = ttk.Window(themename = 'simplex')
window.resizable(width = False, height = False)
window.title("Password Manager")
icon = ttk.PhotoImage(file = 'key.png')
window.iconphoto(False, icon)

#LOGIC

def confirm():
    if len(Ent1.get()) < 8:
        mbox.showerror(title="Error", message="Your password must have at least 8 characters.")
    elif Ent1.get() == Ent2.get():
        mbox.showinfo(title="Success", message="Your password has been changed.")
    else:
        mbox.showerror(title="Error", message="Passwords do not match. Try again.")


#FRAMES
top = ttk.Frame(window)
top.pack()
bot = ttk.Frame(window)
bot.pack(fill='both', expand=True)

#WIDGETS
Lab1 = ttk.Label(top, text="Create a password(8 characters minimum): ", anchor='w')
Lab1.pack(pady=5, padx=(5, 20))
Ent1 = ttk.Entry(top, show="*")
Ent1.pack(pady=5, padx=10, fill='both', expand=True)
Lab2 = ttk.Label(top, text="Confirm your password: ")
Lab2.pack(pady=5, padx=5, anchor='w')
Ent2 = ttk.Entry(top, show="*")
Ent2.pack(pady=(5,20), padx=10, fill='both', expand=True)


#BOTWIDGETS
Canc = ttk.Button(bot, text='Cancel', width=10)
Canc.pack(side='right', padx=10, pady=10)

OK = ttk.Button(bot, text="OK", width=10, command=confirm)
OK.pack(side='right', padx=5, pady=10)
