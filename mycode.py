import pandas as pd
import os

# Create data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Create a sample DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie","David","Eve","Frank"],
    "Age": [25, 30, 35,20,22,28],
    "City": ["New York", "Los Angeles", "Chicago","Washington DC","New Jersey","Houston"]
})

# Save the DataFrame to a CSV file in the data directory
df.to_csv("data/sample.csv", index=False)

print("Data saved to data/sample.csv")  