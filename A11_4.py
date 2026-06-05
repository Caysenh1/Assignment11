import ttkbootstrap as ttk

window = ttk.Window(themename = 'superhero')
window.resizable(width = False, height = False)
window.title("Destiny Chooser")
icon = ttk.PhotoImage(file = 'destiny.png')
window.iconphoto(False, icon)

#FRAMES
top_frame = ttk.Frame(window)
pic_frame = ttk.Frame(window)
check_frame = ttk.Frame(window)
b_frame = ttk.Frame(window)

top_frame.pack()
pic_frame.pack()
check_frame.pack()
b_frame.pack()

#Label-topframe
Label0 = ttk.Label(top_frame, text="CHOOSE YOUR DESTINY...",
                   font=("Cambria", 18))
Label0.pack()
#image-buttons
vader = ttk.PhotoImage(file="vader.png")
vbutton = ttk.Button(pic_frame, image=vader, bootstyle = 'light')
vbutton.pack(side='left',padx=5)
yoda = ttk.PhotoImage(file='yoda.png')
ybutton = ttk.Button(pic_frame, image=yoda, bootstyle ='light')
ybutton.pack(side='left', padx=5)
#check_framewidgets
rad1 = ttk.Radiobutton(
    check_frame,
    text="Dark Side",
    value="A")
rad1.pack(side='left', padx=5, pady=5)
rad2 = ttk.Radiobutton(
    check_frame,
    text="Light Side",
    value="B")
rad2.pack(side='left', padx=5, pady=5)
Check1 = ttk.Checkbutton(check_frame, text="Force Sensitive",
                         bootstyle="round-toggle")
Check1.pack(side='left', padx=5, pady=5)
Check2 = ttk.Checkbutton(check_frame, text="Lightsaber Skilled",
                         bootstyle="round-toggle")
Check2.pack(side='left', padx=5, pady=5)
#B_Frame widget
bbutton = ttk.Button(b_frame, text="Folllow your Destiny...",
                     bootstyle='danger')
bbutton.pack(pady=5)

