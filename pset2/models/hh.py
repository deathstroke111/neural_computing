import numpy as np

from models.gating import *


class HodgkinHuxley:

    def __init__(self):

        self.C = 1.0

        self.gNa_bar = 120
        self.gK_bar = 36
        self.gL = 0.3

        self.ENa = 45
        self.EK = -82
        self.EL = -59

    def simulate(
        self,
        t_max=100,
        dt=0.01,
        pulse_amp=10,
        pulse_start=30,
        pulse_end=60,
    ):

        t = np.arange(0, t_max, dt)

        V = np.zeros_like(t)
        m = np.zeros_like(t)
        h = np.zeros_like(t)
        n = np.zeros_like(t)
        I = np.zeros_like(t)

        V[0] = -70

        m[0] = alpham(V[0]) / (alpham(V[0]) + betam(V[0]))
        h[0] = alphah(V[0]) / (alphah(V[0]) + betah(V[0]))
        n[0] = alphan(V[0]) / (alphan(V[0]) + betan(V[0]))

        I[(t >= pulse_start) & (t <= pulse_end)] = pulse_amp

        for k in range(len(t) - 1):

            am = alpham(V[k])
            bm = betam(V[k])
            ah = alphah(V[k])
            bh = betah(V[k])
            an = alphan(V[k])
            bn = betan(V[k])

            dm = am * (1 - m[k]) - bm * m[k]
            dh = ah * (1 - h[k]) - bh * h[k]
            dn = an * (1 - n[k]) - bn * n[k]

            m[k + 1] = m[k] + dt * dm
            h[k + 1] = h[k] + dt * dh
            n[k + 1] = n[k] + dt * dn

            gNa = self.gNa_bar * (m[k] ** 3) * h[k]
            gK = self.gK_bar * (n[k] ** 4)

            INa = gNa * (V[k] - self.ENa)
            IK = gK * (V[k] - self.EK)
            IL = self.gL * (V[k] - self.EL)

            dV = (I[k] - INa - IK - IL) / self.C

            V[k + 1] = V[k] + dt * dV

        return t, V, I, m, h, n