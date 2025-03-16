# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 21:57:18 2025

@author: lerou
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


p2_data = "SAA2_WC_2017_metocean_10min_avg.csv"
df = pd.read_csv(p2_data, sep=",", na_values=["NULL"], parse_dates=["TIME_SERVER"], dayfirst=True)
df.set_index("TIME_SERVER", inplace=True)

df = df.dropna()

def ddmm2dd(ddmm):
    degrees = np.floor(ddmm / 100)
    minutes = (ddmm - degrees * 100) / 60
    return degrees + minutes
df["LATITUDE"] = df["LATITUDE"].apply(ddmm2dd)
df["LONGITUDE"] = df["LONGITUDE"].apply(ddmm2dd)
df.loc[df["N_S"] == "S", "LATITUDE"] *= -1
df.loc[df["E_W"] == "W", "LONGITUDE"] *= -1

df_selected = df.loc[:'2017-07-04']

plt.style.use("grayscale")
plt.figure(figsize=(10,5))
plt.plot(df_selected.index, df_selected["TSG_TEMP"], label="Temperature (°C)", linewidth=1)
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Time Series of Temperature")
plt.legend()
plt.grid()
plt.savefig("temperature_timeseries.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df_selected["TSG_SALINITY"], bins=np.arange(30, 35.5, 0.5), color="blue", edgecolor="black")
plt.xlabel("Salinity (PSU)")
plt.ylabel("Frequency")
plt.title("Salinity Distribution")
plt.grid()
plt.savefig("salinity_histogram.png", dpi=300)
plt.show()

temperature_stats = {
    "Mean": df_selected["TSG_TEMP"].mean(),
    "Standard Deviation": df_selected["TSG_TEMP"].std(),
    "Interquartile Range": df_selected["TSG_TEMP"].quantile(0.75) - df_selected["TSG_TEMP"].quantile(0.25)
}

salinity_stats = {
    "Mean": df_selected["TSG_SALINITY"].mean(),
    "Standard Deviation": df_selected["TSG_SALINITY"].std(),
    "Interquartile Range": df_selected["TSG_SALINITY"].quantile(0.75) - df_selected["TSG_SALINITY"].quantile(0.25)
}

stats_df = pd.DataFrame([temperature_stats, salinity_stats], index=["TSG_TEMP", "TSG_SALINITY"])
print(stats_df)

plt.figure(figsize=(8, 6))
sc = plt.scatter(df_selected["WIND_SPEED_TRUE"], df_selected["AIR_TEMPERATURE"], c=df_selected["LATITUDE"], cmap="viridis", edgecolors="black")
plt.colorbar(label="Latitude")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Air Temperature (°C)")
plt.title("Wind Speed vs Air Temperature (Colored by Latitude)")
plt.grid()
plt.savefig("wind_temp_scatter.png", dpi=300)
plt.show()

