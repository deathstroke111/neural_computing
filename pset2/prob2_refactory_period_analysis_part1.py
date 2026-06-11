import matplotlib.pyplot as plt
import numpy as np
from models.gating import *

V = np.arange(-100, 100)

ah = alphah_double(V)
bh = betah(V)

h_inf = ah/(ah+bh)

plt.plot(V, h_inf)
plt.title('V vs inactivation gating variable')
plt.xlabel('V in mV')
plt.ylabel('h infinity')
plt.show()