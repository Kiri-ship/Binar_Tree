import tkinter
import customtkinter
import turtle

def button_callback():
    print("button clicked")


def slider_interation_event(self):
    label_value_interation.configure(text=int(slider_interation.get()))


app = customtkinter.CTk()
app.geometry("1200x650")
app.title("L-system visualizer")
app.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")


canvas = turtle.ScrolledCanvas(app)
canvas.place(relx=0, rely=0, relheight=1, relwidth=0.8)



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




button_start = customtkinter.CTkButton(MenuFrame, text="Start", width=70)
button_start.grid(row=3,column=0, pady=5, sticky="n")

button_restart = customtkinter.CTkButton(MenuFrame, text="Restart", width=70)
button_restart.grid(row=3,column=1, pady=5, sticky="n")

button_stop = customtkinter.CTkButton(MenuFrame, text="Stop", width=70)
button_stop.grid(row=3,column=2, pady=5, sticky="n")

app.mainloop()