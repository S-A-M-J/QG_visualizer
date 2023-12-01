#QG_calc.py

import math

from colorama import Fore, Style

import tkinter as tk
from tkinter import ttk

class InputData:
    def __init__(self, radius, density1, density2, distance):
        self.density1 = density1
        self.distance = distance
        self.radius = radius
        self.density2 = density2


def calculate_sphere_data(radius, density):
    volume = 4/3 * math.pi * radius **3
    mass = volume * density
    return mass

def calculate_gravity_acceleration(mass, distance):
    gravity = mass * (6.67408 * 10**-11) / distance **2
    return gravity

def calculate_result():

    # Get values from the entry widgets
    radius = float(radius_entry.get())
    distance = float(distance_entry.get())
    density1 = float(density1_entry.get())
    density2 = float(density2_entry.get())
    mass1 = calculate_sphere_data(radius, density1*1000)
    mass2 = calculate_sphere_data(radius, density2*1000)
    gravity1 = calculate_gravity_acceleration(mass1, distance)
    gravity2 = calculate_gravity_acceleration(mass2, distance)
    gravity_difference = gravity1 - gravity2
    threshold = float(thresh_label.get()) * 10**-9

    if gravity_difference is not None:
        result_label.config(text=f"The difference in acceleration due to gravity is: {gravity_difference} m/s^2")
        if abs(gravity_difference) > threshold:
            detectable_label.config(text="Difference should be detectable", foreground="green")
        else:
            detectable_label.config(text="Difference is probably not detectable", foreground="red")
        
    else:
        result_label.config(text="Invalid input. Please enter numeric values.")

    




# Create the main window
window = tk.Tk()
window.title("Gravitational Force Calculator")

# Create notebook (tabbed interface)
notebook = ttk.Notebook(window)

# Create and place labels and entry widgets on the first tab
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Calculator')

# Create and place labels and entry widgets on the first tab
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Settings')

# Create and place labels and entry widgets
radius_label = ttk.Label(tab1, text="Radius of Sphere (m):")
radius_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
radius_entry = ttk.Entry(tab1)
radius_entry.grid(row=0, column=1, padx=10, pady=5)
radius_entry.insert(tk.END, "1")

distance_label = ttk.Label(tab1, text="Distance to QG (m):")
distance_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
distance_entry = ttk.Entry(tab1)
distance_entry.grid(row=1, column=1, padx=10, pady=5)
distance_entry.insert(tk.END, "1")

density1_label = ttk.Label(tab1, text="Density of Sphere 1 (g/ccm):")
density1_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
density1_entry = ttk.Entry(tab1)
density1_entry.grid(row=2, column=1, padx=10, pady=5)
density1_entry.insert(tk.END, "0.5")

density2_label = ttk.Label(tab1, text="Density of Sphere 2 (g/ccm):")
density2_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
density2_entry = ttk.Entry(tab1)
density2_entry.grid(row=3, column=1, padx=10, pady=5)
density2_entry.insert(tk.END, "1.5")


# Create a button to trigger the calculation
calculate_button = ttk.Button(tab1, text="Calculate", command=calculate_result)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create a label to display the result
result_label = ttk.Label(tab1, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=5)

# Create a label to display the result
detectable_label = ttk.Label(tab1, text="")
detectable_label.grid(row=6, column=0, columnspan=2, pady=5)

# Tab 2 - settings
# Create and place labels and entry widgets
thresh_label = ttk.Label(tab2, text="Detectability Threshold * 10^(-9) (m/s^2):")
thresh_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
thresh_label = ttk.Entry(tab2)
thresh_label.grid(row=0, column=1, padx=10, pady=5)
thresh_label.insert(tk.END, "10")

# Pack the notebook to make it visible
notebook.pack(expand=True, fill="both")
# Start the GUI event loop
window.mainloop()
