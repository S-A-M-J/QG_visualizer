#QG_calc.py

import math

from colorama import Fore, Style

import tkinter as tk
from tkinter import ttk

# Using Unicode characters for superscript
superscript_minus = '\u207B'  # Unicode for superscript minus
superscript_9 = '\u2079'      # Unicode for superscript 9
superscript_1 = '\u00B9'  # Unicode for superscript 1
superscript_0 = '\u2070'  # Unicode for superscript 0
superscript_2 = '\u00B2'  # Unicode for superscript 2
superscript_8 = '\u2078'  # Unicode for superscript 8

class InputData:
    def __init__(self, radius, density1, density2, distance):
        self.density1 = density1
        self.distance = distance
        self.radius = radius
        self.density2 = density2

def on_dropdown1_select(event):
    # Get the selected value from the dropdown
    #print(dropdown1_var.get())
    selected_option = dropdown1_var.get()

    # Extract the numerical value from the selected option
    number = selected_option.split('(')[-1].rstrip(')')
    try:
        number_value = float(number)
        # Update the entry field with the number value
        density1_entry.delete(0, tk.END)  # Clear the entry field
        density1_entry.insert(0, str(number_value))  # Insert the number value
    except ValueError:
        pass  # Handle the exception if the number extraction fails

def on_dropdown2_select(event):
    #print(dropdown2_var.get())
    # Get the selected value from the dropdown
    selected_option = dropdown2_var.get()

    # Extract the numerical value from the selected option
    number = selected_option.split('(')[-1].rstrip(')')
    try:
        number_value = float(number)
        # Update the entry field with the number value
        density2_entry.delete(0, tk.END)  # Clear the entry field
        density2_entry.insert(0, str(number_value))  # Insert the number value
    except ValueError:
        pass  # Handle the exception if the number extraction fails

def calculate_sphere_data(radius, density):
    volume = 4/3 * math.pi * radius **3
    mass = volume * density
    return mass

def calculate_gravity_acceleration(mass, distance):
    gravity = mass * (6.67408 * 10**-11) / distance **2
    gradient = (2 * mass * (6.67408 * 10**-11)) / (distance **3) 
    #print(f"Gradient: {gradient:.5e}")
    return gravity, gradient

def calculate_result():

    # Get values from the entry widgets
    radius = float(radius_entry.get())
    distance = float(distance_entry.get())
    density1 = float(density1_entry.get())
    density2 = float(density2_entry.get())
    mass1 = calculate_sphere_data(radius, density1*1000)
    mass2 = calculate_sphere_data(radius, density2*1000)
    gravity1, gradient1 = calculate_gravity_acceleration(mass1, distance)
    gravity2, gradient2 = calculate_gravity_acceleration(mass2, distance)
    gravity_difference = abs(gravity1 - gravity2)
    gradient_difference = abs(gradient1 - gradient2)
    gravity_threshold = float(thresh_gradio_entry.get()) * 10**-8
    gradient_threshold = float(thresh_gradio_entry.get()) * 10**-11

    if gravity_difference and gradient_difference is not None:
        result_label.config(text=f"The total mass of sphere 1 is: {mass1:.3f} kg\nThe total mass of sphere 2 is: {mass2:.3f} kg\n\nThe difference in acceleration due to gravity is: {gravity_difference:.5e} m/s{superscript_2}\n\nThe difference in gradient is: {gradient_difference:.5e} s{superscript_minus}{superscript_2}")
        if abs(gravity_difference) > gravity_threshold:
            detectable_by_QG_label.config(text="Difference should be detectable by QG", foreground="green")
        else:
            detectable_by_QG_label.config(text="Difference is probably not detectable by QG", foreground="red")

        if abs(gradient_difference) > gradient_threshold:
            detectable_by_QGradio_label.config(text="Difference should be detectable by QGradio", foreground="green")
        else:
            detectable_by_QGradio_label.config(text="Difference is probably not detectable by QGradio", foreground="red")
        
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

# Create a Tkinter variable for storing the dropdown selection
dropdown1_var = tk.StringVar()
dropdown1 = ttk.Combobox(tab1, textvariable=dropdown1_var)
dropdown1.grid(row=2, column=2, padx=5, pady=5)
dropdown1['values'] = ("Loam soil (1.575)", "Organic soil (0.35)", "Sandy soil (1.43)", "Silty soil (1.36)", "Clay soil (1.12)", "Quartz (2.65)", "Water (1.0)", "Bomb (3.5)", "Air (0.001)")
dropdown1.current(0)  # Default to the first option
dropdown1.bind("<<ComboboxSelected>>", on_dropdown1_select)

density2_label = ttk.Label(tab1, text="Density of Sphere 2 (g/ccm):")
density2_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
density2_entry = ttk.Entry(tab1)
density2_entry.grid(row=3, column=1, padx=10, pady=5)
density2_entry.insert(tk.END, "1.5")

# Create a Tkinter variable for storing the dropdown selection
dropdown2_var = tk.StringVar()
dropdown2 = ttk.Combobox(tab1, textvariable=dropdown2_var)
dropdown2.grid(row=3, column=2, padx=5, pady=5)
dropdown2['values'] = ("Loam soil (1.575)", "Organic soil (0.35)", "Sandy soil (1.43)", "Silty soil (1.36)", "Clay soil (1.12)", "Quartz (2.65)", "Water (1.0)", "Bomb (3.5)", "Air (0.001)")
dropdown2.current(0)  # Default to the first option
dropdown2.bind("<<ComboboxSelected>>", on_dropdown2_select)

# Create a button to trigger the calculation
calculate_button = ttk.Button(tab1, text="Calculate", command=calculate_result)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create a label to display the result
result_label = ttk.Label(tab1, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=5)

# Create a label to display the result
detectable_by_QG_label = ttk.Label(tab1, text="")
detectable_by_QG_label.grid(row=6, column=0, columnspan=2, pady=5)

# Create a label to display the result
detectable_by_QGradio_label = ttk.Label(tab1, text="")
detectable_by_QGradio_label.grid(row=7, column=0, columnspan=2, pady=5)

# Tab 2 - settings
# Create and place labels and entry widgets
thresh_gravity_label = ttk.Label(tab2, text=f"Detectability Threshold in microgal (m/s{superscript_minus}{superscript_8}):")
thresh_gravity_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
thresh_gravity_entry = ttk.Entry(tab2)
thresh_gravity_entry.grid(row=0, column=1, padx=10, pady=5)
thresh_gravity_entry.insert(tk.END, "1")

# Create and place labels and entry widgets
thresh_gradio_label = ttk.Label(tab2, text=f"Detectability Threshold in Eotvas (10{superscript_minus}{superscript_9}s{superscript_minus}{superscript_2}):")
thresh_gradio_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
thresh_gradio_entry = ttk.Entry(tab2)
thresh_gradio_entry.grid(row=1, column=1, padx=10, pady=5)
thresh_gradio_entry.insert(tk.END, "1")

# Pack the notebook to make it visible
notebook.pack(expand=True, fill="both")
# Start the GUI event loop
window.mainloop()
