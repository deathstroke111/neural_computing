import matplotlib.pyplot as plt
import numpy as np
from models.gating import *

V = np.arange(-100, 100)

ah = alphah_double(V)
bh = betah(V)
ah2 = alphah_double(V)

h_inf_original = ah/(ah+bh)

h_inf_double_alpha = ah2/((ah2)+bh)

plt.plot(V, h_inf_original, color='green', label='original')
plt.plot(V, h_inf_double_alpha, color='red', label='double alpha')
plt.title('V vs inactivation gating variable')
plt.xlabel('V in mV')
plt.ylabel('h infinity')
plt.legend()
plt.show()