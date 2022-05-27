# This is a PyHUMMOD
This is a python implementation of the HUMMOD model of human physiology. The HUMMOD model is written in a custom XML language that can be difficult to read. I wrote a script to convert the custom XML language to python. That conversion script is available in this repository and can be used to re-convert HUMMOD if the XML is updated.

The HUMMOD model of physiology is the result of collaboration between many physiologists over many decades. It consists of over 10,000 variables and the equations that relate them. Running the model means setting a lot of parameters then stepping forward in short time steps and recalculating the values of the body's parameters at each timestep.

## Required python packages:
- scipy

# run from command line:

edit the config file to set the parameters how you like and state which outputs you want to log

from the PyHumMod directory run:
> python model.py
