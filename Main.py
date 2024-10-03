import tkinter as tk
from tkinter import ttk, messagebox
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def plot_visualization():
    data_points = coords_text.get("1.0", tk.END).strip()
    
    x, y, z, sizes, labels = [], [], [], [], []
    
    try:
        points = data_points.split(';')  
        for point in points:
            coords = point.strip().split(',')  
            if len(coords) != 5:
                raise ValueError("Each point must have five values (Latency, Throughput, T_clk, Area, name).")
            Latency, Throuput, T_clk, Area, DFD_name= coords[0], coords[1], coords[2], coords[3], coords[4]
            x.append(float(Latency))      
            y.append(float(Throuput))      
            z.append(float(T_clk))      
            sizes.append(float(Area)*50)
            labels.append(DFD_name.strip())  

        # Create a 3D scatter plot
        fig = plt.Figure(figsize=(6, 5), dpi=100)
        ax = fig.add_subplot(111, projection='3d')
        scatter = ax.scatter(x, y, z, s=sizes, c='blue', marker='o')  

        
        ax.set_xlabel('Latency')
        ax.set_ylabel('Throughput')
        ax.set_zlabel('T_clk')

        
        for i in range(len(x)):
            ax.text(x[i], y[i], z[i], labels[i], fontsize=9, ha='right')

        
        for widget in plot_frame.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))


root = tk.Tk()
root.title("DFD Design & Trade-off visualizer")
root.geometry("1000x1000")


input_frame = ttk.Frame(root)
input_frame.pack(padx=10, pady=10, fill=tk.X)


instructions = ttk.Label(input_frame, text="Enter coordinates as 'Latency, Throughput, T_clk, Area, Name;' (e.g., 3, 0.33 (1/3), 2.2, 50, DFD1;) (the values per DFD should be separated by a semi-colon (;) except for the last one which doesnt need  (the values per DFD should be separated by a semi-colon (;) except for the last one which doesnt need it)t)")
instructions.pack(pady=5)


coords_text = tk.Text(input_frame, height=5, width=50)
coords_text.pack(padx=5, pady=5)


plot_button = ttk.Button(root, text="Plot 3D Scatter Plot", command=plot_visualization)
plot_button.pack(pady=20)


plot_frame = ttk.Frame(root)
plot_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


root.mainloop()
