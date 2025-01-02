#! /bin/python3

import matplotlib.pyplot as plt

# Load insert sizes from file
with open("insert_sizes.txt", "r") as file:
    insert_sizes = [int(line.strip()) for line in file]

# Plot the distribution of insert sizes
plt.figure(figsize=(10, 6))
plt.hist(insert_sizes, bins=1, edgecolor="black")
plt.title('Insert Size Distribution')
plt.xlabel('Fragment Size (bp)')
plt.ylabel('Frequency')
plt.show()

