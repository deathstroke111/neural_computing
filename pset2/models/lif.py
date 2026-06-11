import numpy as np

def simulate_lif(
    I_amp=1.5,           # nA
    t_max=300,           # ms
    dt=0.1,              # ms
    EL=-70,              # mV
    V_thresh=-50,        # mV
    V_reset=-65,         # mV
    Rm=10,               # MOhm
    Cm=1,                # nF
    pulse_start=50,
    pulse_end=250,
):
    """
    Simulate a leaky integrate-and-fire neuron.
    """

    t = np.arange(0, t_max, dt)
    V = np.zeros_like(t)
    I = np.zeros_like(t)

    tau_m = Rm * Cm  # ms

    V[0] = EL

    spike_times = []

    I[(t >= pulse_start) & (t <= pulse_end)] = I_amp

    for k in range(len(t) - 1):

        dV = (
            -(V[k] - EL)
            + Rm * I[k]
        ) / tau_m

        V[k + 1] = V[k] + dt * dV

        if V[k + 1] >= V_thresh:
            spike_times.append(t[k + 1])
            V[k + 1] = V_reset

    return t, V, I, np.array(spike_times)