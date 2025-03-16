# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def ddmm2dd(ddmm):
    thedeg = np.floor(ddmm/100.)
    themin = (ddmm - thedeg * 100.)/60
    return thedeg + themin

p1_data = "CTD_corrections_p1.dat"
df = pd.read_csv(p1_data, delimiter="\t")

depth = df["Depth"]
temperature = df["Temperature (psu)"]
salinity = df["Salinity (psu)"]

fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(10, 6))

axes[0].plot(temperature, depth, color='red', label="Temperature")
axes[0].set_xlabel("Temperature (°C)")
axes[0].set_ylabel("Depth (m)")
axes[0].invert_yaxis()
axes[0].grid()
axes[0].legend()

axes[1].plot(temperature, depth, color='blue', label="Salinity")
axes[1].set_xlabel("Salinity (psu)")
axes[1].grid()
axes[1].legend()

plt.tight_layout()
plt.savefig("temperature_salinity_profiles.png", dpi=300)
plt.show()


