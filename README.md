# This is a PyHumMod
This is a python implementation of the [HumMod](https://http://hummod.org/) model of human physiology. The HumMod model is written in a custom XML language. By re-writing the model in python I hope to make it more accessible.

The HumMod model of physiology is the result of collaboration between many physiologists over many decades. It consists of over 10,000 variables and the equations that relate them. Running the model means setting a lot of parameters then stepping forward in short time steps and recalculating the values of the body's parameters at each timestep.

## Required python packages:
- scipy

# run from command line:
from the PyHumMod directory run:
> python model.py

# the structure
HumMod consists of hundreds of files representing different components of human phsyiology. In pyHumMod each file is represented by a class. All classes are defined in a single file: src/hummod.py

Functions that solve differential equations or define custom subic splines are in src/special_functions.py
