import ttkbootstrap as ttk

window = ttk.Window(themename = 'journal')
window.resizable(width = False, height = False)
window.title("Compound Interest")
icon = ttk.PhotoImage(file = 'dollar.png')
window.iconphoto(False, icon)
#LOGIC
def calc():
    A = 0
    P = int(Pri.get())
    R = int(Rat.get())
    N = int(Com.get())
    T = int(Time.get())
    A = P*(1+(R/100)/N)**(N*T)
    A = round(A, 2)
    Ans.config(text=A)
#FRAMES
L_frame = ttk.Labelframe(window, text="Parameters")
L_frame.pack(side='left', pady=10, padx=10)

R_frame = ttk.Labelframe(window, text="Calculate")
R_frame.pack(side='left', expand=True, fill='both', pady=10, padx=10)
#L_FRAME LABELS
PrinL = ttk.Label(L_frame, text="Principal($): ")
AirL = ttk.Label(L_frame, text="Annual Interest Rate(%): ")
CPL = ttk.Label(L_frame, text="Compounding Period: ")
TimeL = ttk.Label(L_frame, text="Time(years): ")
#L_FRAME GRID LABELS
PrinL.grid(row=0, column=0, pady=7)
AirL.grid(row=1, column=0, pady=7)
CPL.grid(row=2, column=0, pady=7)
TimeL.grid(row=3, column=0, pady=7)
#L_FRAME ENTRY
PriVar = ttk.StringVar()
Pri = ttk.Entry(L_frame, textvariable=PriVar)
Pri.grid(row=0, column=1, pady=5)

RatVar = ttk.StringVar()
Rat = ttk.Entry(L_frame, textvariable=RatVar)
Rat.grid(row=1, column=1, pady=5)

ComVar = ttk.StringVar()
Com = ttk.Entry(L_frame, textvariable=ComVar)
Com.grid(row=2, column=1, pady=5, padx=10)

TimeVar = ttk.StringVar()
Time = ttk.Entry(L_frame, textvariable=TimeVar)
Time.grid(row=3, column=1, pady=5)

#R_FRAME WIDGETS
calc = ttk.Button(R_frame, text="Calculate",
                  width=15, command=calc)
calc.pack(side='top', padx=10, pady=10)

D = ttk.Label(R_frame, text="$", font = ("Helvetica", 18))
D.pack(side = 'left', padx=(30,0))
Ans = ttk.Label(R_frame, text=0, font = ("Helvetica", 18))
Ans.pack(side='left', padx=(20,20), fill='x', expand=True)










