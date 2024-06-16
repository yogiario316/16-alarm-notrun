import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from threading import Timer
import pygame

def set_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm_label.config(text=f"Alarm set for {alarm_time}")
    current_time = datetime.now().strftime("%H:%M:%S")
    time_diff = (datetime.strptime(alarm_time, "%H:%M:%S") - datetime.strptime(current_time, "%H:%M:%S")).total_seconds()
    if time_diff < 0:
        time_diff += 86400  # Add one day in seconds if time_diff is negative
    Timer(time_diff, play_alarm).start()

def play_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file.get())
    pygame.mixer.music.play()
    messagebox.showinfo("Alarm", "Time to wake up!")
    while pygame.mixer.music.get_busy():
        continue

# Set up GUI
root = tk.Tk()
root.title("Alarm Clock")

tk.Label(root, text="Set Time (24 hour format)").pack()

frame = tk.Frame(root)
frame.pack()

hour = tk.StringVar(root)
hour.set("00")
tk.Entry(frame, textvariable=hour, width=3).pack(side="left")

minute = tk.StringVar(root)
minute.set("00")
tk.Entry(frame, textvariable=minute, width=3).pack(side="left")

second = tk.StringVar(root)
second.set("00")
tk.Entry(frame, textvariable=second, width=3).pack(side="left")

tk.Label(root, text="Sound File Path").pack()
sound_file = tk.StringVar(root)
tk.Entry(root, textvariable=sound_file).pack()

tk.Button(root, text="Set Alarm", command=set_alarm).pack()

alarm_label = tk.Label(root, text="", fg="red")
alarm_label.pack()

root.mainloop()
