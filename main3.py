import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

entries = []

def add_new_dfd():
    global entries

    latency = latency_entry.get()
    tput = tput_entry.get()
    tclk = tclk_entry.get()
    area = area_entry.get()
    dfd_name = dfd_entry.get()

    try:
        latency = float(latency)
        tput = float(tput)
        tclk = float(tclk)
        area = float(area)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter number values for Latency, Tput, Tclk, and Area.")
        return

    if not dfd_name:
        messagebox.showerror("Input Error", "DFD Name cannot be empty!")
        return

    entries.append((latency, tput, tclk, area, dfd_name))
    messagebox.showinfo("DFD added successfully!")

    latency_entry.delete(0, tk.END)
    tput_entry.delete(0, tk.END)
    tclk_entry.delete(0, tk.END)
    area_entry.delete(0, tk.END)
    dfd_entry.delete(0, tk.END)

    update_dfd_list()

def update_dfd_list():
    dfd_listbox.delete(0, tk.END)  
    for entry in entries:
        latency, tput, tclk, area, dfd_name = entry
        dfd_listbox.insert(tk.END, f"DFD: {dfd_name} | Latency: {latency}, Tput: {tput}, Tclk: {tclk}, Area: {area}")

def plot_dfd():
    if len(entries) == 0:
        messagebox.showerror("No DFD entries to plot!")
        return

    size_scale = size_slider.get()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for latency, tput, tclk, area, dfd_name in entries:
        ax.scatter(latency, tput, tclk, s=area * size_scale)
        
        ax.text(latency, tput, tclk, dfd_name, fontsize=9)

    ax.set_xlabel('Latency')
    ax.set_ylabel('Tput')
    ax.set_zlabel('Tclk')

    plt.show()

root = tk.Tk()
root.title("DFD Input")
root.geometry("700x700")  

tk.Label(root, text="Latency:").grid(row=0, column=0)
latency_entry = tk.Entry(root)
latency_entry.grid(row=0, column=1)

tk.Label(root, text="Tput:").grid(row=1, column=0)
tput_entry = tk.Entry(root)
tput_entry.grid(row=1, column=1)

tk.Label(root, text="Tclk:").grid(row=2, column=0)
tclk_entry = tk.Entry(root)
tclk_entry.grid(row=2, column=1)

tk.Label(root, text="Area:").grid(row=3, column=0)
area_entry = tk.Entry(root)
area_entry.grid(row=3, column=1)

tk.Label(root, text="DFD Name:").grid(row=4, column=0)
dfd_entry = tk.Entry(root)
dfd_entry.grid(row=4, column=1)

add_button = tk.Button(root, text="Add New DFD", command=add_new_dfd)
add_button.grid(row=5, column=0, columnspan=2, pady=10)

tk.Label(root, text="DFD Area Scale:").grid(row=6, column=0, padx=10, pady=5)
size_slider = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL)
size_slider.set(50)  
size_slider.grid(row=6, column=1, padx=10, pady=5)

dfd_listbox = tk.Listbox(root, width=80, height=10)
dfd_listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

plot_button = tk.Button(root, text="Plot DFD Data", command=plot_dfd)
plot_button.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
