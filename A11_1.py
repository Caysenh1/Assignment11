import ttkbootstrap as ttk

window = ttk.Window(themename = 'flatly')
window.resizable(width = False, height = False)

#FRAMES
top_frame = ttk.Labelframe(
    window,
    text = "Account Information"
)

top_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
top_frame.columnconfigure(0,weight=1)

bottom_frame = ttk.Labelframe(
    window,
    text = "Submission"
)

#WIDGETS
label1 = 


