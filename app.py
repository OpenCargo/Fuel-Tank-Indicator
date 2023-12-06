import customtkinter
from udp_listener import udp_listener as udp
import threading
import math
from datetime import datetime

CAPACITY1 = 4950
CAPACITY2 = 4950
CAPACITY3 = 4950


UDP_PORT1 = 12345
UDP_PORT2 = 12346
UDP_PORT3 = 12347

def calculate_liters(data, capacity):
    data=float(data)-20
    percentage = (135 - data )/1.35
    liters = capacity * percentage / 100
    return round(percentage), round(liters)


def update_ui(liters_label, percentage_label, progress_bar, time_label, capacity,data):
    percentage, liters= calculate_liters(data, capacity)

    liters_label_text = f"Liters: {liters}"
    liters_label.configure(text=liters_label_text)

    percentage_label_text = f"{percentage}%"
    percentage_label.configure(text=percentage_label_text)

    progress_bar_value = liters / capacity
    progress_bar.set(progress_bar_value)

    time = datetime.now().strftime('%d-%m %H:%M')
    time_label.configure(text=f"{time}")


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
time = datetime.now().strftime('%d-%m %H:%M')
app = customtkinter.CTk()
app.geometry("700x500")
app.minsize(700,500)
app.title("Fuel Indicator")

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)

label_tank1 = customtkinter.CTkLabel(app, text="Tank 1:", font=(None, 30))
label_tank1.grid(row=0, column=0, padx=40, pady=40)
progressbar1 = customtkinter.CTkProgressBar(app, orientation="vertical", width=80, corner_radius=5)
progressbar1.grid(row=1, column=0, padx=40, pady=10)
progressbar1.set(progressbar_value1)
label_percentage1 = customtkinter.CTkLabel(app, text=f"{percentage_tank1}%", font=(None, 20))
label_percentage1.grid(row=1, column=0, padx=40, pady=40)
label_liters1 = customtkinter.CTkLabel(app, text=f"Liters: {liters1}", font=(None, 20))
label_liters1.grid(row=2, column=0, padx=40, pady=40)
label_last_update1 = customtkinter.CTkLabel(app, text =f"{time}", font = (None, 15))
label_last_update1.grid(row=3, column=0, padx=40, pady=0)


label_tank2 = customtkinter.CTkLabel(app, text="Tank 2:", font=(None, 30))
label_tank2.grid(row=0, column=1, padx=40, pady=40)
progressbar2 = customtkinter.CTkProgressBar(app, orientation="vertical", width=80, corner_radius=5)
progressbar2.grid(row=1, column=1, padx=40, pady=10)
progressbar2.set(progressbar_value2)
label_percentage2 = customtkinter.CTkLabel(app, text=f"{percentage_tank2}%", font=(None, 20))
label_percentage2.grid(row=1, column=1, padx=40, pady=40)
label_liters2 = customtkinter.CTkLabel(app, text=f"Liters: {liters2}", font=(None, 20))
label_liters2.grid(row=2, column=1, padx=40, pady=40)
label_last_update2 = customtkinter.CTkLabel(app, text =f"{time}", font = (None, 15))
label_last_update2.grid(row=3, column=1, padx=40, pady=0)

label_tank3 = customtkinter.CTkLabel(app, text="Tank 3:", font=(None, 30))
label_tank3.grid(row=0, column=2, padx=40, pady=40)
progressbar3 = customtkinter.CTkProgressBar(app, orientation="vertical", width=80, corner_radius=5)
progressbar3.grid(row=1, column=2, padx=40, pady=10)
progressbar3.set(progressbar_value3)
label_percentage3 = customtkinter.CTkLabel(app, text=f"{percentage_tank3}%", font=(None, 20))
label_percentage3.grid(row=1, column=2, padx=40, pady=40)
label_liters3 = customtkinter.CTkLabel(app, text=f"Liters: {liters3}", font=(None, 20))
label_liters3.grid(row=2, column=2, padx=40, pady=40)
label_last_update3 = customtkinter.CTkLabel(app, text =f"{time}", font = (None, 15))
label_last_update3.grid(row=3, column=2, padx=40, pady=0)

udp_thread1 = threading.Thread(target=udp, args=(UDP_PORT1,(update_ui, label_liters1, label_percentage1, progressbar1, label_last_update1, CAPACITY1)))
udp_thread2 = threading.Thread(target=udp, args=(UDP_PORT2,(update_ui, label_liters2, label_percentage2, progressbar2, label_last_update2, CAPACITY2)))
udp_thread3 = threading.Thread(target=udp, args=(UDP_PORT3,(update_ui, label_liters3, label_percentage3, progressbar3, label_last_update3, CAPACITY3)))

udp_thread1.start()
udp_thread2.start()
udp_thread3.start()
app.mainloop()



