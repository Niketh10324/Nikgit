import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the parabola function
def parabola(x):
    return np.sqrt(8 * x)

# Define the limits of integration (x-values)
x_start = 0
x_end = 2

# Calculate the area using integration (upper half and lower half)
area_half, _ = quad(lambda x: parabola(x), x_start, x_end)
total_area = 2 * area_half  # Multiply by 2 to include both halves

# Print the area in fractional form
print(f"The total area enclosed by the parabola and the line x = 2 is: {total_area:.2f} (approximately), which is 32/3 in fractional form.")

# Create values for plotting
x_values = np.linspace(0, 2, 400)
y_positive = parabola(x_values)
y_negative = -parabola(x_values)

# Plot the parabola and the line
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_positive, label=r'$y^2 = 8x$', color='blue')
plt.plot(x_values, y_negative, color='blue')  # Plot the negative part of the parabola
plt.axvline(x=2, color='red', linestyle='--', label='Line $x=2$')

# Fill the area between the curve and the line
plt.fill_between(x_values, y_negative, y_positive, where=(x_values <= 2), color='lightblue', alpha=0.5)

# Set up the plot limits and labels
plt.xlim(-1, 3)
plt.ylim(-5, 5)
plt.title('Area Enclosed by the Parabola and the Line')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
plt.savefig('/home/niketh/Nikgit/M4/figs/fig1.png')
