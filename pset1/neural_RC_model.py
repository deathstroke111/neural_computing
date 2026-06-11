import numpy as np
import matplotlib.pyplot as plt

# Cell Parameters
C =  0.4524# Capacitance in nF
R =  22.1043# Resistance in MegaOhm
Vrest =  -70# Leakage current reversal potential in mV

# Integration parameters
dt = 0.1          # integration time-step in ms
Tdur = 1000       # simulation total time in ms
V0 =  Vrest # initial condition in mV

k = int(np.ceil(Tdur / dt))   # total number of iterations

V = np.zeros(k + 1)           # Voltage vector in mV
V[0] = V0                     # initial condition

# time vector
t = dt * np.arange(k + 1)     # time vector in ms

# Current pulse parameters
Tstart = 100 # current pulse start time in ms
Tstop = 200 # current pulse stop time in ms
Iamplitude =  0.1 # current pulse amplitude in nA

I = np.zeros(k + 1)           # current vector in nA
I[(t >= Tstart) & (t < Tstop)] = Iamplitude

# Integration with Exponential Euler loop
tau = R * C   # membrane time constant (ms if R and C units are consistent)

for j in range(k):
    Vinf = Vrest + R * I[j]   # steady-state voltage at this step
    V[j + 1] = Vinf + (V[j] - Vinf) * np.exp(-dt / tau)

# Plotting Voltage and Current on separate figures
plt.figure(figsize=(10, 4)) # Create a figure for the first plot (e.g., Voltage)
plt.subplot(1, 2, 1) # Select the first subplot (left side)
plt.plot(t, V, color='orange', label='Voltage')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.title('Membrane Voltage Response')
plt.grid(True)

plt.subplot(1, 2, 2) # Select the second subplot (right side)
plt.plot(t, I, color='green', label='Current')
plt.xlabel('Time (ms)')
plt.ylabel('Current (nA)')
plt.title('Applied Current')
plt.grid(True)

plt.tight_layout() # Adjust layout to prevent overlap
plt.show()