import pandas as pd
import numpy as np
from dash import html, dash, dcc

with open("data_file.json", "r") as file:
    df = pd.read_json(file)
    # print(df.head())
    print(df)
    df.set_index("time", inplace=True)
    print(df.Close)

# time = df["time"].to_numpy
# pressure = df["pressure"].values
# temperature = df["temperature"]

# print(f"\n Time: {time}")
# print(f"\n TYPE: {type(time)}")

# print(f"\n Pressure: {pressure}")
# print(f"\n TYPE: {type(pressure)}")

# print(f"\n pressure: {temperature}")
# print(f"\n TYPE: {type(temperature)}")

# pressure = pressure.tolist()
# # time = time.tolist()
# temperature = temperature.tolist()
# print(f"\n pressure: {temperature}")
# print(f"\n pressure: {type(temperature)}")
# print(f"\n temperature: {type(temperature)}")
# print(f"\n tim: {type(time)}")