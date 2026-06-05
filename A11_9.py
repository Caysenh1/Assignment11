import ttkbootstrap as ttk

window = ttk.Window(themename = 'superhero')
window.resizable(width = False, height = False)
window.title("Slideshow")
icon = ttk.PhotoImage(file = 'jedi.png')
window.iconphoto(False, icon)

#FRAMES
picframe = ttk.Frame(window)
picframe.pack()
butframe = ttk.Frame(window)
butframe.pack()

#WIDGETS
slide1 = ttk.PhotoImage(file="slide1.PNG")
Pic1 = ttk.Label(picframe, image=slide1)
Pic1.pack()

slide2 = ttk.PhotoImage(file="slidePic2.PNG")
Pic2 = ttk.Label(picframe, image=slide2)

slide3 = ttk.PhotoImage(file="slidePic3.PNG")
Pic3 = ttk.Label(picframe, image=slide3)

slide4 = ttk.PhotoImage(file="slidePic4.PNG")
Pic4 = ttk.Label(picframe, image=slide4)

slide5 = ttk.PhotoImage(file="slidePic5.PNG")
Pic5 = ttk.Label(picframe, image=slide5)

but1 = ttk.Button(butframe, text="Previous")
but1.pack()

but2=ttk.Button(butframe, text="Next")
but2.pack()
