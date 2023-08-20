import customtkinter


app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    customtkinter.set_default_color_theme("Dark-Blue")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(
    master=app,
    text="CTkButton",
    command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()