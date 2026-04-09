import numpy as np
import matplotlib.pyplot as plt

# Parameters
numParticles = 500   # Number of particles
maxTime = 1000       # End time (steps)

# Time vector
t = np.arange(0, maxTime + 1)

# Initial positions (all zeros)
x0 = np.zeros(numParticles)

# Matrix to store positions
X = np.zeros((numParticles, maxTime + 1))

# Assign initial condition
X[:, 0] = x0

# Main loop
for idx in range(1, maxTime + 1):
    # Generate random steps: +1 or -1
    dX = 2 * np.random.binomial(1, 0.5, size=numParticles) - 1
    
    # Update positions
    X[:, idx] = X[:, idx - 1] + dX

# Plot dynamic histogram
plt.figure(figsize=(12, 7))

# Plot trajectories for all particles
for particle_idx in range(numParticles):
    plt.plot(t, X[particle_idx, :], linewidth=0.5, alpha=0.5)

plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Trajectories of All Particles')
plt.grid(True, alpha=0.3)
plt.show()

'''
plt.figure()
ax = plt.gca()

for idx in range(maxTime + 1):
    ax.clear()
    ax.hist(X[:, idx], bins=bins, density=True)
    ax.set_ylim(0, 0.2)
    plt.pause(0.01)

plt.show()
'''