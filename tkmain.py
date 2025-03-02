import tkinter
from tkinter import colorchooser
import customtkinter
import turtle

from Lsys import Pifagor_tree
from Lsys import Dragon_Line
from Lsys import Serpinsky_treangle




BLACK = (0, 0, 0)


def button_start_callback():
    if combobox.get() == "Pifagor tree":
        interation = int(slider_interation.get())
        Tree = Pifagor_tree(interation)
        String = Tree.Generate_String()
        Tree.Draw(String, turtle_screen, button_color.cget("fg_color"))
    
    elif combobox.get() == "Dragon line":
        interation = int(slider_interation.get())
        DragonLine = Dragon_Line(interation)
        String = DragonLine.Generate_String()
        DragonLine.Draw(String, turtle_screen, button_color.cget("fg_color"))

    elif combobox.get() == "Serpynsky's treangle":
        interation = int(slider_interation.get())
        Serpinsky = Serpinsky_treangle(interation)
        String = Serpinsky.Generate_String()
        Serpinsky.Draw(String, turtle_screen, button_color.cget("fg_color"))



def button_restart_callback():
    print("button restart clicked")

def button_stop_callback():
    print("button stop clicked")

def button_chosen_color():
    chosen_color = colorchooser.askcolor(initialcolor=None, parent=MenuFrame, title="Color Picker")
    if chosen_color[1]:
        color = chosen_color[1]
        button_color.configure(fg_color=color)


def slider_interation_event(self):
    label_value_interation.configure(text=int(slider_interation.get()))


app = customtkinter.CTk()
app.iconbitmap(default="logo.ico")
app.geometry("1200x650")
app.title("L-system visualizer")
app.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")


canvas = turtle.ScrolledCanvas(app)
canvas.place(relx=0, rely=0, relheight=1, relwidth=0.8)
turtle_screen = turtle.TurtleScreen(canvas)
turtle_screen.bgcolor(BLACK)


MenuFrame = customtkinter.CTkFrame(app,width=200, height=650)
MenuFrame.pack(anchor="ne", padx=6)



combobox = customtkinter.CTkComboBox(MenuFrame, values=["Pifagor tree", "Dragon line", "Serpynsky's treangle"], width=180)
combobox.grid(row=0, column=0, pady=20, columnspan=3)



slider_interation = customtkinter.CTkSlider(MenuFrame, from_=1, to=8, command=slider_interation_event)
slider_interation.set(1)
slider_interation.grid(row=2, column=0, pady=5, columnspan=3)

label_interation = customtkinter.CTkLabel(MenuFrame, text="  interation:", fg_color="transparent")
label_interation.grid(row=1, column=0, sticky="w")

value_interation = slider_interation.get()
label_value_interation = customtkinter.CTkLabel(MenuFrame, text=value_interation, fg_color="transparent")
label_value_interation.grid(row=2, column=4, padx=2)




button_start = customtkinter.CTkButton(MenuFrame, text="Start", width=70, command=button_start_callback)
button_start.grid(row=3,column=0, pady=5, sticky="n")

button_restart = customtkinter.CTkButton(MenuFrame, text="Restart", width=70, command=button_restart_callback)
button_restart.grid(row=3,column=1, pady=5, sticky="n")

button_stop = customtkinter.CTkButton(MenuFrame, text="Stop", width=70, command=button_stop_callback)
button_stop.grid(row=3,column=2, pady=5, sticky="n")

button_color = customtkinter.CTkButton(MenuFrame, text="Chehge color", width=70, command=button_chosen_color)
button_color.grid(row=4,column=0, pady=5, columnspan=3, sticky="n")





app.mainloop()