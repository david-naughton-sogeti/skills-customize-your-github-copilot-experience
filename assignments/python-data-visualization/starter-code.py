# Starter Code: Python Data Visualization

"""
This starter code will help you get started with loading data and creating basic plots using matplotlib.
You can switch to plotly if you prefer interactive charts.
"""

import matplotlib.pyplot as plt
import csv

# Example: Load data from a CSV file (or use a list)
data = [10, 15, 7, 12, 9, 14]
labels = ['A', 'B', 'C', 'D', 'E', 'F']

# Line chart
plt.figure(figsize=(8, 4))
plt.plot(labels, data, marker='o')
plt.title('Line Chart Example')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# Bar chart
plt.figure(figsize=(8, 4))
plt.bar(labels, data, color='skyblue')
plt.title('Bar Chart Example')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# (Optional) Try creating a scatter plot, pie chart, or histogram below!
