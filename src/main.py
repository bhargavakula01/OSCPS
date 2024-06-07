import tkinter as tk
from tkinter import ttk
import numpy as np

class ChemicalProcessSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Chemical Process Simulator")
        
        # Create input fields
        self.create_input_fields()
        
        # Create button to run simulation
        self.run_button = ttk.Button(root, text="Run Simulation", command=self.run_simulation)
        self.run_button.grid(row=4, column=1, pady=10)
        
        # Create text widget to display results
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.grid(row=5, column=0, columnspan=3, pady=10)

    def create_input_fields(self):
        ttk.Label(self.root, text="Initial Concentration of A [A0] (mol/L)").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.a0_entry = ttk.Entry(self.root)
        self.a0_entry.grid(row=0, column=1, pady=5)
        
        ttk.Label(self.root, text="Rate Constant k (1/s)").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.k_entry = ttk.Entry(self.root)
        self.k_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(self.root, text="Total Time t (s)").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.t_entry = ttk.Entry(self.root)
        self.t_entry.grid(row=2, column=1, pady=5)
        
        ttk.Label(self.root, text="Time Steps").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.steps_entry = ttk.Entry(self.root)
        self.steps_entry.grid(row=3, column=1, pady=5)
        
    def run_simulation(self):
        # Get input values
        try:
            A0 = float(self.a0_entry.get())
            k = float(self.k_entry.get())
            t_total = float(self.t_entry.get())
            steps = int(self.steps_entry.get())
        except ValueError:
            self.result_text.insert(tk.END, "Please enter valid numerical values.\n")
            return
        
        # Time points
        t = np.linspace(0, t_total, steps)
        
        # Concentration of A over time (first-order kinetics)
        A_t = A0 * np.exp(-k * t)
        
        # Clear previous results
        self.result_text.delete(1.0, tk.END)
        
        # Display results
        self.result_text.insert(tk.END, f"Time (s)\tConcentration of A (mol/L)\n")
        for time, conc in zip(t, A_t):
            self.result_text.insert(tk.END, f"{time:.2f}\t\t{conc:.4f}\n")

# Create the main window
root = tk.Tk()

# Create an instance of the simulator
simulator = ChemicalProcessSimulator(root)

# Run the main event loop
root.mainloop()

