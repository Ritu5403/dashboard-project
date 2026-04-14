import tkinter as tk
from tkinter import messagebox

# Functions
def virus():
    messagebox.showinfo("Virus.exe", "Virus Simulation Triggered!")

def ransomware():
    messagebox.showinfo("Ransomware.exe", "Ransomware Simulation Triggered!")

def rat():
    messagebox.showinfo("RAT.exe", "RAT Simulation Triggered!")

# Window
root = tk.Tk()
root.title("Cybersecurity Dashboard")
root.geometry("400x300")

label = tk.Label(root, text="Cybersecurity Dashboard", font=("Arial", 14))
label.pack(pady=20)

btn1 = tk.Button(root, text="Virus.exe", command=virus, width=20, bg="red")
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Ransomware.exe", command=ransomware, width=20, bg="orange")
btn2.pack(pady=10)

btn3 = tk.Button(root, text="RAT.exe", command=rat, width=20, bg="yellow")
btn3.pack(pady=10)

root.mainloop()