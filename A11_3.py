import ttkbootstrap as ttk

window = ttk.Window(themename = 'journal')
window.resizable(width = False, height = False)
window.title("Calculator")
icon = ttk.PhotoImage(file = 'calculator.png')
window.iconphoto(False, icon)

#FRAMES
top_frame = ttk.Frame(window)
B_frame = ttk.Frame(window)

top_frame.pack()
B_frame.pack()
#Entry
entry = ttk.Entry(top_frame, width = 37)
entry.pack(expand=True, pady=5,padx=5)
#BUTTTTTTTOOOOOOOOOOOONS
b1 = ttk.Button(B_frame, text='1', width=5)
b2 = ttk.Button(B_frame, text='2', width=5)
b3 = ttk.Button(B_frame, text='3', width=5)
b4 = ttk.Button(B_frame, text='4', width=5)
b5 = ttk.Button(B_frame, text='5', width=5)
b6 = ttk.Button(B_frame, text='6', width=5)
b7 = ttk.Button(B_frame, text='7', width=5)
b8 = ttk.Button(B_frame, text='8', width=5)
b9 = ttk.Button(B_frame, text='9', width=5)
b0 = ttk.Button(B_frame, text='0', width=5)
bAdd = ttk.Button(B_frame, text='+', width=5)
bC = ttk.Button(B_frame, text='C', width=5)
bDiv = ttk.Button(B_frame, text='/', width=5)
bMul = ttk.Button(B_frame, text='*', width=5)
bMin = ttk.Button(B_frame, text='-', width=5)
bEq = ttk.Button(B_frame, text='=', width=5)

#Grid

b7.grid(row=0, column=0, padx=(5,2), pady=2)
b8.grid(row=0, column=1, padx=2, pady=2)
b9.grid(row=0, column=2, padx=2, pady=2)
bDiv.grid(row=0, column=3, padx=(2,5), pady=2)
b4.grid(row=1, column=0, padx=(5,2), pady=2)
b5.grid(row=1, column=1, padx=2, pady=2)
b6.grid(row=1, column=2, padx=2, pady=2)
bMul.grid(row=1, column=3, padx=(2,5), pady=2)
b1.grid(row=2, column=0, padx=(5,2), pady=2)
b2.grid(row=2, column=1, padx=2, pady=2)
b3.grid(row=2, column=2, padx=2, pady=2)
bMin.grid(row=2, column=3, padx=(2,5), pady=2)
b0.grid(row=3, column=0, padx=(5,2), pady=(2,7))
bAdd.grid(row=3, column=1, padx=2, pady=(2,7))
bC.grid(row=3, column=2, padx=2, pady=(2,7))
bEq.grid(row=3, column=3, padx=(2,5), pady=(2,7))

