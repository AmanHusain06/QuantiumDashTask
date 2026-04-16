import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)

# Filter only Pink Morsels
df = df[df["product"] == "pink morsel"]

# 🔥 FIX: clean price column (remove $ and convert to float)
df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

# Create Sales column correctly
df["Sales"] = df["quantity"] * df["price"]

# Keep only required columns
df = df[["Sales", "date", "region"]]

# Rename columns
df.columns = ["Sales", "Date", "Region"]

# Save
df.to_csv("processed_data.csv", index=False)

print("Fixed and done")