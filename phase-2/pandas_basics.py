# This script demonstrates basic operations with Pandas, a powerful library for numerical computing in Python.

import pandas as pd

data = {
    "name": ["Nand", "Asha", "Ravi"],
    "score" : [72, 85, 90],
    "age": [19, 20, 21]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("Columns:")
print(df.columns)
print("Shape", df.shape)