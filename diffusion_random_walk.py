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
plt.figure(figsize=(10, 6))

# Calculate mean displacement from center for each time step
mean_displacement = np.mean(X, axis=0)
std_displacement = np.std(X, axis=0)

plt.plot(t, mean_displacement, 'b-', linewidth=2, label='Mean')
plt.fill_between(t, mean_displacement - std_displacement, mean_displacement + std_displacement, alpha=0.3, label='±1 Std Dev')
plt.xlabel('Time')
plt.ylabel('Displacement from Center')
plt.title('Mean Particle Displacement Over Time')
plt.legend()
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