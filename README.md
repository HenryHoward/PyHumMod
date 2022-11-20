# This is a PyHumMod
This is a python implementation of the [HumMod](http://hummod.org/) model of human physiology. The HumMod model is written in a custom XML language. By re-writing the model in python I hope to make it more accessible.

The HumMod model of physiology is the result of collaboration between many physiologists over many decades. It consists of over 10,000 variables and the equations that relate them. Running the model means setting a lot of parameters then stepping forward in short time steps and recalculating the values of the body's parameters at each timestep.

![PyHumMod as a causal network](https://github.com//HenryHoward/pyHumMod/blob/main/PyHumMod.png?raw=true)

## Required python packages:
- scipy


# run from command line:
from the PyHumMod directory run:
> python example_default.py

to run with custom parameters, simply set the chosen parameters before running the simulation, as in example_10000_feet_altitude.py or example_beta_blockade.py


# the structure
HumMod consists of hundreds of files representing different components of human phsyiology. In pyHumMod each file is represented by a class. All classes are defined in a single file: src/hummod.py

Functions that solve differential equations or define custom cubic splines are in src/special_functions.py


# convert to python afresh
Included in this respository is the script I used to convert the standard HumMod library into python.

To do this afresh, change the source directory in HumMod_to_python_converter.py to point to a standard HumMod repository

Then, from the PyHumMod directory run:
> python HumMod_to_python_converter.py
