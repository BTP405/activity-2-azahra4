import matplotlib.pyplot as plt
import numpy as np

def graphSnowfall(filename):
    def fileopen(filename):
        counts = [0] * 5  # Initialize counters for each range (A list with 5 elements set to 0- [0,0,0,0,0])
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line: #To make sure line is not empty space
                    intnum = int(line)
                    index = (intnum - 1) // 10  # Calculate the index for counts (floor Division) 10//10 =1 but we want the index to be 0 so to adjust the index we do (10-1)//10 = 0 
                    counts[index] += 1 #The increment according to the index.
        return counts
    plt.style.use('_mpl-gallery')
    # Make data:
    x_labels = ['0-10cm', '11-20cm', '21-30cm', '31-40cm', '41-50cm']
    x = np.arange(len(x_labels))
    y = fileopen(filename) #Using the closure function here

    # Plot
    fig, ax = plt.subplots()

    ax.bar(x, y, width=0.8, edgecolor="white", linewidth=0.7)

    ax.set(xticks=x, xticklabels=x_labels,
           ylim=(0, max(y) + 1), yticks=np.arange(0, max(y) + 1))

    plt.subplots_adjust(bottom=0.12, left=0.12)

    plt.show()

graphSnowfall("q2_test.txt")
