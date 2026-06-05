import ttkbootstrap as ttk

window = ttk.Window(themename = 'darkly')
window.resizable(width = False, height = False)
window.title("Best Movie")
icon = ttk.PhotoImage(file = 'question.png')
window.iconphoto(False, icon)

#Frames
top_frame = ttk.Frame(window)
mid_frame = ttk.Frame(window)
bottom_frame = ttk.Frame(window)

top_frame.pack()
mid_frame.pack()
bottom_frame.pack()

#Widget LABEL
Label1 = ttk.Label(top_frame, text="QUESTION", font=("Arial", 18), bootstyle = 'info')
Label2 = ttk.Label(top_frame, text="Which is the greatest of all movies?")
#Label pack
Label1.pack()
Label2.pack()
#Widget Buttons
button1 = ttk.Button(mid_frame, text="A: Star Wars Saga", width=25)
button2 = ttk.Button(mid_frame, text="B: Lord of the Rings Trilogy", width=25)
button3 = ttk.Button(mid_frame, text="C: Harry Potter Series", width=25)
button4 = ttk.Button(mid_frame, text="D: Batman Trilogy", width=25)
button5 = ttk.Button(bottom_frame, text="SUBMIT", bootstyle = 'success')
button5.pack(padx=5, pady=5)
#GRID
button1.grid(row=0, column=0, padx=10, pady=5)
button2.grid(row=0, column=1, padx=10)
button3.grid(row=1, column=0, )
button4.grid(row=1, column=1, )


window.mainloop()
