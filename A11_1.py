import ttkbootstrap as ttk

window = ttk.Window(themename = 'flatly')
window.resizable(width = False, height = False)
window.title("Account Info")
icon = ttk.PhotoImage(file = 'info.png')
window.iconphoto(False, icon)
#FRAMES
top_frame = ttk.Labelframe(
    window,
    text = "Account Information"
)

top_frame.pack()

bottom_frame = ttk.Labelframe(
    window,
    text = 'Submission')

bottom_frame.pack(fill='x')

#WIDGETS NAMES
Labelname1 = ttk.Label(
    top_frame,
    text = "First name: ",
    width = 20
)
Labelname2 = ttk.Label(
    top_frame,
    text = "Last name: ",
    width = 20
)
Labelname3 = ttk.Label(
    top_frame,
    text = "Username: ",
    width = 20
)
#WIDGET ENTRY
Entry1 = ttk.Entry(top_frame, width = 40)
Entry2 = ttk.Entry(top_frame, width = 40)
Entry3 = ttk.Entry(top_frame, width = 40)

#Widget Buttons
button1 = ttk.Button(bottom_frame, text = 'Save', width = 16)
button1.pack(side = 'left', pady=5, padx=5, expand=True)
button2 = ttk.Button(bottom_frame, text = 'Clear', width = 16)
button2.pack(side = 'left', pady=5, padx=5, expand=True)
button3=ttk.Button(bottom_frame, text = 'Exit', width = 16)
button3.pack(side = 'left', pady=5, padx=5, expand=True)


#GRID STUFF
Labelname1.grid(row=0, column=0)
Labelname2.grid(row=1, column=0)
Labelname3.grid(row=2, column=0)

Entry1.grid(row=0, column=1)
Entry2.grid(row=1, column=1)
Entry3.grid(row=2, column=1) 

window.mainloop()
