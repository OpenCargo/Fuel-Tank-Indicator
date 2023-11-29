import customtkinter
from udp_listener import udp_listener as udp
import threading
import math

DIAMETER1 = 1.84
LENGHT1 = 1.86
CAPACITY1 = 4950

DIAMETER2 = 1.84
LENGHT2 = 1.86
CAPACITY2 = 4950

DIAMETER3 = 1.84
LENGHT3 = 1.86
CAPACITY3 = 4950


UDP_PORT1 = 12345
UDP_PORT2 = 12346
UDP_PORT3 = 12347

def calculate_liters(data, diameter, lenght):
    fuel_height = diameter - float(data)/100
    alfa = math.acos((diameter - 2 * fuel_height) / diameter)
    liters = 1000*lenght * (alfa * (diameter/2)**2 - (diameter/2 - fuel_height) * math.sqrt(diameter * fuel_height - fuel_height**2))
    return liters


def update_liters_and_percentage(liters_label, percentage_label, progress_bar, capacity, diameter, lenght, data):
    liters = calculate_liters(data, diameter, lenght)
    capacity_percentage = (liters / capacity) * 100

    liters_label_text = f"Liters: {liters:.2f}"
    liters_label.configure(text=liters_label_text)

    percentage_label_text = f"{capacity_percentage:.2f}%"
    percentage_label.configure(text=percentage_label_text)

    progress_bar_value = liters / capacity
    progress_bar.set(progress_bar_value)


#starting values
progressbar_value1 = 0.5
percentage_tank1 = progressbar_value1 * 100
liters1 = 0 

progressbar_value2 = 0.5
percentage_tank2 = progressbar_value1 * 100
liters2 = 0 

progressbar_value3 = 0.5
percentage_tank3 = progressbar_value1 * 100
liters3 = 0 

app = customtkinter.CTk()
app.geometry("800x500")
app.title("Fuel Indicator")

label_tank1 = customtkinter.CTkLabel(app, text="Tank 1:", font=(None, 30))
label_tank1.grid(row=0, column=0, padx=40, pady=40)
progressbar1 = customtkinter.CTkProgressBar(app, orientation="vertical", width=80, corner_radius=5)
progressbar1.grid(row=1, column=0, padx=40, pady=10)
progressbar1.set(progressbar_value1)
label_percentage1 = customtkinter.CTkLabel(app, text=f"{percentage_tank1}%", font=(None, 20))
label_percentage1.grid(row=1, column=0, padx=40, pady=40)
label_liters1 = customtkinter.CTkLabel(app, text=f"Liters: {liters1}", font=(None, 20))
label_liters1.grid(row=2, column=0, padx=40, pady=40)


label_tank2 = customtkinter.CTkLabel(app, text="Tank 2:", font=(None, 30))
label_tank2.grid(row=0, column=1, padx=40, pady=40)
progressbar2 = customtkinter.CTkProgressBar(app, orientation="vertical", width=80, corner_radius=5)
progressbar2.grid(row=1, column=1, padx=40, pady=10)
progressbar2.set(progressbar_value2)
label_percentage2 = customtkinter.CTkLabel(app, text=f"{percentage_tank2}%", font=(None, 20))
label_percentage2.grid(row=1, column=1, padx=40, pady=40)
label_liters2 = customtkinter.CTkLabel(app, text=f"Liters: {liters2}", font=(None, 20))
label_liters2.grid(row=2, column=1, padx=40, pady=40)


label_tank3 = customtkinter.CTkLabel(app, text="Tank 3:", font=(None, 30))
label_tank3.grid(row=0, column=2, padx=40, pady=40)
progressbar3 = customtkinter.CTkProgressBar(app, orientation="vertical", width=80, corner_radius=5)
progressbar3.grid(row=1, column=2, padx=40, pady=10)
progressbar3.set(progressbar_value3)
label_percentage3 = customtkinter.CTkLabel(app, text=f"{percentage_tank3}%", font=(None, 20))
label_percentage3.grid(row=1, column=2, padx=40, pady=40)
label_liters3 = customtkinter.CTkLabel(app, text=f"Liters: {liters3}", font=(None, 20))
label_liters3.grid(row=2, column=2, padx=40, pady=40)


udp_thread1 = threading.Thread(target=udp, args=(UDP_PORT1,(update_liters_and_percentage, label_liters1, label_percentage1, progressbar1, CAPACITY1, DIAMETER1, LENGHT1)))
udp_thread2 = threading.Thread(target=udp, args=(UDP_PORT2,(update_liters_and_percentage, label_liters2, label_percentage2, progressbar2, CAPACITY2, DIAMETER2, LENGHT2)))
udp_thread3 = threading.Thread(target=udp, args=(UDP_PORT3,(update_liters_and_percentage, label_liters3, label_percentage3, progressbar3, CAPACITY3, DIAMETER3, LENGHT3)))

udp_thread1.start()
udp_thread2.start()
udp_thread3.start()
app.mainloop()



