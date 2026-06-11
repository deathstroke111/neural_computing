import matplotlib.pyplot as plt
from models.lif import simulate_lif
import numpy as np
from scipy.optimize import curve_fit

'''
#Problem 1.1
t, V, I, spikes = simulate_lif(I_amp=1.5)
fig, ax = plt.subplots(3, 1, figsize=(10, 9), sharex=True)

ax[0].plot(t, V)
ax[0].set_ylabel("Vm (mV)")
ax[1].plot(t, I)
ax[1].set_ylabel("Current (nA)")
ax[1].set_xlabel("Time (ms)")
# Plot spikes using scatter plot at recorded times (y=1 for visibility)
ax[2].scatter(spikes, np.ones_like(spikes), marker='o', s=10)
ax[2].set_ylabel("Spikes")
ax[2].set_xlabel("Time (ms)")
plt.show()
'''



#Problem 1.2
currents = np.linspace(50, 200, 400)
rates = []
max_voltages = []

for amp in currents:
    _, V, _, spikes = simulate_lif(I_amp=amp)

    if len(spikes) < 2:
        rates.append(0)
        max_voltages.append(np.max(V)) # Record max voltage even if no spikes
    else:
        isi = np.diff(spikes)
        rate = 1000 / np.mean(isi)
        rates.append(rate)
        max_voltages.append(np.max(V))

slope, intercept = np.polyfit(currents, rates, 1)

print(f'Capacitance of membrane {1/slope}')

plt.figure(figsize=(10, 6)) # Use a single figure for the f-I curve and voltage plot

# Plotting Firing Rate (Original)
plt.subplot(1, 2, 1)
plt.plot(currents, rates, marker="o")
plt.xlabel("Injected Current (nA)")
plt.ylabel("Firing Rate (Hz)")
plt.title("LIF f-I Curve")

# Plotting Max Voltage vs Current
plt.subplot(1, 2, 2)
plt.plot(currents, max_voltages, marker="o")
plt.xlabel("Injected Current (nA)")
plt.ylabel("Max Vm (mV)")
plt.title("Peak Voltage vs Current")

plt.tight_layout() # Adjust layout to prevent overlap
plt.show()





'''
#problem 1.3
t, V, I, spikes = simulate_lif(I_amp=3.5)
fig, ax = plt.subplots(3, 1, figsize=(10, 9), sharex=True)

ax[0].plot(t, V)
ax[0].set_ylabel("Vm (mV)")
ax[1].plot(t, I)
ax[1].set_ylabel("Current (nA)")
ax[1].set_xlabel("Time (ms)")
# Plot spikes using scatter plot at recorded times (y=1 for visibility)
ax[2].scatter(spikes, np.ones_like(spikes), marker='o', s=10)
ax[2].set_ylabel("Spikes")
ax[2].set_xlabel("Time (ms)")
plt.show()
'''
