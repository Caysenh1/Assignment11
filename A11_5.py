import ttkbootstrap as ttk

window = ttk.Window(themename = 'pulse')
window.resizable(width = False, height = False)
window.title("Restaurant")
icon = ttk.PhotoImage(file = 'meal.png')
window.iconphoto(False, icon)
#FRAMES
t_frame = ttk.Frame(window, borderwidth=1, relief = "solid", padding = 5)
m_frame = ttk.Frame(window, borderwidth=1, relief = "solid", padding = 5)
b_frame = ttk.Frame(window, borderwidth=1, relief = "solid", padding = 5)
t_frame.pack(fill='both', expand=True, padx=5, pady=5)
m_frame.pack(padx=5, pady=5)
b_frame.pack(padx=5, pady=5)
#Labels
Label0 = ttk.Label(t_frame,justify="center",text="Restaurant Order", font=("Arial", 18, 'bold'))
Label0.pack()
Label2 = ttk.Label(m_frame, text="Select Meal Combo: ")
Label2.grid(row=0, column=0)
Label3 = ttk.Label(m_frame, text="Special Instructions: ")
Label3.grid(row=1, column=0)
#Combo and Entry
combo = ttk.Combobox(
    m_frame,
    values = ["Epic Breakfast",
              "Healthy Lunch",
              "Carb Load Time",
              "Daily Special"],
    state="readonly")
combo.grid(row=0, column=1, pady=5)
Entry = ttk.Entry(m_frame, width=23)
Entry.grid(row=1, column=1)
#BUTTOns
button1 = ttk.Button(b_frame, text="Submit Order", width=17)
button1.pack(side='left', padx=2)
button2 = ttk.Button(b_frame, text="Clear Order", width=17)
button2.pack(padx=2)
