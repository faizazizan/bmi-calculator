#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objs as go
import plotly.offline as pyo
import numpy as np

# Define the BMI function
def calculate_bmi(height, weight):
    height_m = height/100
    bmi = weight / (height_m ** 2)
    return bmi

# Get user inputs from the HTML form
height_cm = float(input("Enter your height in cm: "))
weight_kg = float(input("Enter your weight in kg: "))

# Calculate the BMI
bmi = calculate_bmi(height_cm, weight_kg)

# Define the categories and colors
categories = ['Underweight', 'Normal', 'Overweight', 'Obese']
colors = ['blue', 'green', 'orange', 'red']

# Define the bins and their labels
bins = [0, 18.5, 25, 30, np.inf]
bin_labels = ['Underweight', 'Normal', 'Overweight', 'Obese']

# Categorize the BMI result
category = np.digitize(bmi, bins) - 1

# Set up Plotly figure
fig = go.Figure(data=[
    go.Scatter(x=[], y=[], mode='markers', marker=dict(size=200, color=colors)),
    go.Scatter(x=[bmi], y=[0], mode='markers', marker=dict(size=200, color='red'))
])

fig.update_layout(
    title=dict(text=f'Your BMI is {bmi:.1f} ({categories[category]})', x=0.5),
    xaxis=dict(title='BMI', range=[0, 50]),
    yaxis=dict(visible=False),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Set the x and y values for the scatter plot
x_values = []
y_values = []
for i in range(len(bins)):
    x_values.append((bins[i] + bins[i-1]) / 2)
    y_values.append(0)
    if i == category:
        y_values[-1] = 1

# Update the x and y values of the scatter plot trace
fig.data[0].x = x_values
fig.data[0].y = y_values

# Display the plot in a new tab
pyo.plot(fig, filename='bmi_plot.html', auto_open=True)


# In[ ]:




