import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the experimental data from CSV file

file_path = os.path.join(".." , "MOSFET Data.csv")
data = pd.read_csv(file_path)

# Extract Vgs and Id columns (modify column names if necessary)
Vgs = data.iloc[:, 0]  # Assuming first column is Vgs
Id = data.iloc[:, 1]   # Assuming second column is Id

Vgs2 = data.iloc[:, 3]  # Assuming first column is Vgs
Id2 = data.iloc[:, 4]   # Assuming second column is Id

# Plot Id vs Vgs
plt.figure(figsize=(8,6))
plt.plot(Vgs, Id, marker='o', linestyle='-', color='b', label="NMOS")
plt.plot(Vgs2, Id2, marker='s', linestyle='-', color='r', label="PMOS" )
plt.xlabel("Gate-to-Source Voltage, Vgs (V)")
plt.ylabel("Drain Current, Id (A)")
plt.title("MOSFET Id vs. Vgs Characterization")
plt.legend()
plt.grid(True)
plt.show()
