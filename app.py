import customtkinter
from udp_listener import udp_listener as udp
import threading
import math

DIAMETER = 1.84
LENGHT = 1.86
TANK1_CAPACITY = 4950

def calculate_liters(data):
    fuel_height = DIAMETER - float(data)/100
    alfa = math.acos((DIAMETER - 2 * fuel_height) / DIAMETER)
    liters = 1000*LENGHT * (alfa * (DIAMETER/2)**2 - (DIAMETER/2 - fuel_height) * math.sqrt(DIAMETER * fuel_height - fuel_height**2))
    return liters


def update_liters_and_percentage(liters_label, percentage_label, progress_bar, data):
    liters = calculate_liters(data)
    capacity_percentage = (liters / TANK1_CAPACITY) * 100

    liters_label_text = f"Liters: {liters:.2f}"
    liters_label.configure(text=liters_label_text)

    percentage_label_text = f"{capacity_percentage:.2f}%"
    percentage_label.configure(text=percentage_label_text)

    progress_bar_value = liters / TANK1_CAPACITY
    progress_bar.set(progress_bar_value)


#starting values
progressbar_value1 = 0.5
percentage_tank1 = progressbar_value1 * 100
liters1 = 0 

app = customtkinter.CTk()
app.geometry("600x500")
app.title("Fuel Indicator")

label_tank = customtkinter.CTkLabel(app, text="Tank 1:", font=(None, 30))
label_tank.grid(row=0, column=0, padx=40, pady=40)

progressbar = customtkinter.CTkProgressBar(app, orientation="vertical", width=80, corner_radius=5)
progressbar.grid(row=1, column=0, padx=40, pady=10)
progressbar.set(progressbar_value1)

label_percentage = customtkinter.CTkLabel(app, text=f"{percentage_tank1}%", font=(None, 20))
label_percentage.grid(row=1, column=0, padx=40, pady=40)

label_liters = customtkinter.CTkLabel(app, text=f"Liters: {liters1}", font=(None, 20))
label_liters.grid(row=2, column=0, padx=40, pady=40)

udp_thread = threading.Thread(target=udp, args=((update_liters_and_percentage, label_liters, label_percentage, progressbar),))
udp_thread.start()

app.mainloop()



