import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Example dataset loading
data = pd.read_csv("ipl_dataset.csv")

# Show first rows
print(data.head())

# Example analysis
total_matches = data.shape[0]
print("Total Matches:", total_matches)
