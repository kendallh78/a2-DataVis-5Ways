import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV data using pandas
csv_path = "/Users/kendallhaddigan/Desktop/A2/penglings.csv"
data = pd.read_csv(csv_path)

# Set up dimensions
width = 600
height = 400

# Set up matplotlib figure and axis
fig, ax = plt.subplots(figsize=(width / 100, height / 100))

# Define scales and color scale
x_min = data['flipper_length_mm'].min()
x_max = data['flipper_length_mm'].max()
y_min = data['body_mass_g'].min()
y_max = data['body_mass_g'].max()

x_scale = np.linspace(x_min, x_max, width)
y_scale = np.linspace(y_min, y_max, height)

color_dict = {'Adelie': '#FBA043', 'Chinstrap': '#9935CC', 'Gentoo': '#469F9F'}
colors = data['species'].map(color_dict)

# Calculate dot size based on bill length
dot_size = np.interp(data['bill_length_mm'], (data['bill_length_mm'].min(), data['bill_length_mm'].max()), (70, 250))

# Draw gridlines behind the scatter plot
ax.set_axisbelow(True)
ax.grid(color='white', linestyle='-', linewidth=0.5)

# Draw scatter plot with varying dot size based on bill length
ax.scatter(data['flipper_length_mm'], data['body_mass_g'], c=colors, s=dot_size, alpha=0.8, zorder=2)

# Draw axes
ax.set_xlabel('Flipper Length (mm)')
ax.set_ylabel('Body Mass (g)')

# Add title
ax.set_title('Pengling Body Mass Prediction')

# Set background color
ax.set_facecolor('#EBEBEB')

# Show the plot
plt.show()
