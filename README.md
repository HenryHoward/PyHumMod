# This is a PyHumMod
This is a python implementation of the HumMod model of human physiology. The HumMod model is written in a custom XML language that can be difficult to read. I wrote a script to convert the custom XML language to python. That conversion script is available in this repository and can be used to re-convert HumMod if the XML is updated.

The HumMod model of physiology is the result of collaboration between many physiologists over many decades. It consists of over 10,000 variables and the equations that relate them. Running the model means setting a lot of parameters then stepping forward in short time steps and recalculating the values of the body's parameters at each timestep.

## Required python packages:
- scipy

# run from command line:

from the PyHumMod directory run:
> python model.py
