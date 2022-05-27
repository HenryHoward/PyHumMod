"""from modules import Context
from modules import Structure

from modules import LeftHeartPumping_Pumping
"""

from src import hummod

def step():
  hummod.Structure.Context_func()
  hummod.Structure.Parms_func()
  hummod.Structure.Dervs_func()
  hummod.Structure.Wrapup_func()

for n in range(0, 10):
    step()
    print("step done, SV is:", hummod.LeftHeartPumping_Pumping.StrokeVolume )