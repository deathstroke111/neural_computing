import numpy as np
import matplotlib.pyplot as plt

def calculate_vs(G_e, alpha):
    """Calculates somatic voltage V_s given G_e and alpha."""
    return (100 * G_e) / (10 * G_e + 10 * alpha + 11)

# Define the range for G_e on a log scale
G_e_values = np.logspace(np.log10(0.01), np.log10(1000), 500)

# Define the values for alpha
alphas = [0, 0.2, 0.5, 1, 2, 5]

plt.figure(figsize=(10, 6))

# Plot V_s vs G_e for each alpha value
for alpha in alphas:
    V_s = calculate_vs(G_e_values, alpha)
    plt.plot(G_e_values, V_s, label=f'$\\alpha = {alpha}$')

# Set plot labels and title
plt.xscale('log')
plt.xlabel('$G_e$ (Log Scale)')
plt.ylabel('$V_s$ (Somatic Voltage)')
plt.title('Somatic Voltage ($V_s$) vs $G_e$ for varying $\\alpha$')
plt.legend(title='Alpha Value')
plt.grid(True, which="both", ls="-") # Show grid lines for both major and minor ticks

# Display the plot
plt.show()