import numpy as np

# Cell Parameters
C =  # Capacitance in nF
R =  # Resistance in MegaOhm
Vrest =  # Leakage current reversal potential in mV

# Integration parameters
dt = 0.1          # integration time-step in ms
Tdur = 1000       # simulation total time in ms
V0 =  # initial condition in mV

k = int(np.ceil(Tdur / dt))   # total number of iterations

V = np.zeros(k + 1)           # Voltage vector in mV
V[0] = V0                     # initial condition

# time vector
t = dt * np.arange(k + 1)     # time vector in ms

# Current pulse parameters
Tstart =  # current pulse start time in ms
Tstop =  # current pulse stop time in ms
Iamplitude =  # current pulse amplitude in nA

I = np.zeros(k + 1)           # current vector in nA
I[(t >= Tstart) & (t < Tstop)] = Iamplitude

# Integration with Exponential Euler loop
tau = R * C   # membrane time constant (ms if R and C units are consistent)

for j in range(k):
    Vinf = Vrest + R * I[j]   # steady-state voltage at this step
    V[j + 1] = Vinf + (V[j] - Vinf) * np.exp(-dt / tau)