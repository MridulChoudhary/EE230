import numpy as np
import matplotlib.pyplot as plt

# Read data from the file
data = []
with open("aol_data.txt", "r") as file:
    next(file)  # Skip header
    for line in file:
        values = line.strip().split()
        frequency = float(values[1])
        aol = float(values[4])
        data.append((frequency, aol))

# Convert to numpy arrays
data = np.array(data)
frequency = data[:, 0]
aol = data[:, 1]

# Convert to dB
aol_db = 20 * np.log10(aol)

# Calculate roll-off slope using the 5 highest frequency values
sorted_indices = np.argsort(frequency)[-5:]
high_freqs = frequency[sorted_indices]
high_magnitudes = aol_db[sorted_indices]

slope = (high_magnitudes[-1] - high_magnitudes[0]) / (np.log10(high_freqs[-1]) - np.log10(high_freqs[0]))
print(f"Estimated roll-off slope: {slope:.2f} dB/decade")

# Determine -3dB frequency
dc_gain_db = aol_db[np.argmax(frequency)]  # Assume highest AOL is DC gain
threshold_db = dc_gain_db - 3

# Find the closest value to -3dB cutoff
diff = np.abs(aol_db - threshold_db)
f_3dB_index = np.argmin(diff)
f_3dB = frequency[f_3dB_index]
print(f"Estimated -3dB Frequency: {f_3dB:.2f} Hz")

# Plot Bode plot
plt.figure(figsize=(8, 6))
plt.semilogx(frequency, aol_db, marker='o', linestyle='-', color='b', label='Magnitude Response')
plt.axhline(threshold_db, color='r', linestyle='--', label='-3dB Line')
plt.axvline(f_3dB, color='g', linestyle='--', label=f'-3dB Frequency: {f_3dB:.2f} Hz')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Bode Plot of AOL')
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
