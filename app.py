import customtkinter


value = 0.5
app = customtkinter.CTk()
app.geometry("600x500")
app.title("Fuel Indicator")

label = customtkinter.CTkLabel(app, text ="Tank 1:")
label.grid(row=0,column=0, padx=40, pady=40)
progressbar = customtkinter.CTkProgressBar(app, orientation="vertical", mode= "determinate")
progressbar.grid(row=1, column=0, padx=40, pady=40)
progressbar.set(value)
label = customtkinter.CTkLabel(app, text ="%")
label.grid(row=1,column=1, padx=40, pady=40)
label = customtkinter.CTkLabel(app, text ="Liters:")
label.grid(row=2,column=0, padx=40, pady=40)
label = customtkinter.CTkLabel(app, text ="0")
label.grid(row=2,column=1, padx=40, pady=40)

app.mainloop()