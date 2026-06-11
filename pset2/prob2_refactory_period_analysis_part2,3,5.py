import matplotlib.pyplot as plt

from models.hhpaired import HodgkinHuxley


hh = HodgkinHuxley()


t, V, I, m, h, n = hh.simulate()

fig, ax = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

ax[0].plot(t, V)
ax[0].set_ylabel("Vm (mV)")

ax[1].plot(t, I)
ax[1].set_ylabel("Current")

ax[2].plot(t, m, label="m")
ax[2].plot(t, h, label="h")
ax[2].plot(t, n, label="n")
ax[2].legend()
ax[2].set_ylabel("Gating")
ax[2].set_xlabel("Time (ms)")

plt.show()