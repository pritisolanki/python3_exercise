import pandas as pd

df = pd.read_csv("cars.csv")
df.to_json("cars_json.json")
