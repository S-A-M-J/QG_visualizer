
import plotly.graph_objects as go
import numpy as np

# Create data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Create a 3D surface plot
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

# Set layout
fig.update_layout(scene=dict(zaxis=dict(range=[-2, 2])))

# Show the interactive plot
fig.show()