# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 20:06:00 2025

@author: lerou
"""

import pandas as pd

filename = "CTD_corrections_p1.dat"

df = pd.read_csv("CTD_corrections_p1.dat", delimiter="\t")

print(df.head())
