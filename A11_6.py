import ttkbootstrap as ttk

window = ttk.Window(themename = 'darkly')
window.resizable(width = False, height = False)
window.title("Area Calculator")
icon = ttk.PhotoImage(file = 'area.png')
window.iconphoto(False, icon)
#LOGIC
x = 1

def area():
    b= float(Base.get())
    h = float(Height.get())
    if combo.get() == "Rectangle":
        x = b*h
        Result.config(text=x)
    if combo.get() == "Triangle":
        x = (b*h)/2
        Result.config(text=x)
#Frames
t_frame = ttk.Labelframe(text="Variable Input")
t_frame.pack(pady=5, padx=5)
b_frame = ttk.Labelframe(text="Calculate")
b_frame.pack(fill='both', expand=True, padx=5, pady=5)
#Widgets-t_frame
combo = ttk.Combobox(t_frame, state='readonly', values=["Rectangle", 'Triangle'])
combo.pack(side='left', pady=5, padx=5)

BaseText = ttk.Label(t_frame, text="Base: ")
BaseText.pack(side='left')

BaseVar = ttk.StringVar()
Base = ttk.Entry(t_frame, textvariable=BaseVar)
Base.pack(side='left')

HeightText = ttk.Label(t_frame, text="Height: ")
HeightText.pack(side='left')

HeightVar = ttk.StringVar()
Height = ttk.Entry(t_frame, textvariable=HeightVar)
Height.pack(side='left', padx=5, pady=5)
#Widgets-b_frame


calc = ttk.Button(b_frame,
                  width=25,
                  text="Calculate",
                  command=area)
calc.pack(side='left', padx=5)
Result = ttk.Label(b_frame, text=0, font=("Helvetica", 18))
Result.pack()

