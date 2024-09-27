import numpy as np
import matplotlib.pyplot as plt

# Project title
project_title = "Trigonometric Functions Plotter"

# Generate values from -2π to 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Calculate the trigonometric functions
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

# Set up the plot
plt.figure(figsize=(10, 6))
plt.title(project_title)
plt.plot(x, y_sin, label='sin(x)', color='blue')
plt.plot(x, y_cos, label='cos(x)', color='green')
plt.plot(x, y_tan, label='tan(x)', color='red')

# Set y-limits for better visualization (tan(x) can go to infinity)
plt.ylim(-10, 10)

# Adding grid, legend, and labels
plt.grid(True)
plt.xlabel('x values (radians)')
plt.ylabel('Function values')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()

# Display the plot
plt.show()
