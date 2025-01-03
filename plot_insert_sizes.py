#! /bin/python3

import matplotlib.pyplot as plt
import statistics
import numpy as np

# Load insert sizes from file
insert_sizes = []
with open("/Users/valishashah/Desktop/all_projects/HaLab_assessment/Sequencing_analysis_assignment/DATA/insert_sizes_filtered.txt", "r") as file:
    for line in file:
        insert_sizes.append(int(line.strip()))

import pandas as pd

insert_sizes = [size for size in insert_sizes if size >= 50]

## Calculating summary statistics 
mean_size = statistics.mean(insert_sizes)
median_size = statistics.median(insert_sizes)
std_dev = statistics.stdev(insert_sizes)
quartiles = np.percentile(insert_sizes, [25, 50, 75])

print(f"Min Insert Size: {min(insert_sizes)}")
print(f"Max Insert Size: {max(insert_sizes)}")
print(f"Mean Insert Size: {mean_size}")
print(f"Median Insert Size: {median_size}")
print(f"Standard Deviation: {std_dev}")
print(f"Quantiles (25%, 50%, 75%): {quartiles}")

### histogram
plt.figure(figsize=(10, 6))
plt.hist(insert_sizes, bins=100)
plt.xlim(0,1000)
plt.show()


# Plotting boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(insert_sizes, vert=False)
plt.title('Insert Size Distribution (Boxplot)')
plt.xlabel('Fragment Size (Insert Size)')
plt.xlim(50, 10000)
# plt.show()


import seaborn as sns

# Plotting the density plot
plt.figure(figsize=(10, 6))
sns.kdeplot(insert_sizes, fill=True)
plt.title('Insert Size Distribution (Density Plot)')
plt.xlabel('Fragment Size (Insert Size)')
plt.ylabel('Density')
plt.xlim(50, 10000)
plt.show()

