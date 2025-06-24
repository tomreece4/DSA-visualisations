import matplotlib.pyplot as plt
import numpy as np


# Performs a bubble sort on the specified amount of random numbers from 0-100
def bubble_sort(size_of_array):
    number_list = np.random.randint(0, 100, size_of_array)
    x = np.arange(0, size_of_array, 1)

    for i in range(size_of_array):
        for j in range(0, size_of_array - i - 1):
            colors = ['blue'] * size_of_array
            colors[j] = 'red'
            colors[j + 1] = 'red'
            plt.bar(x, number_list, color=colors)
            plt.pause(0.01)
            plt.clf()
            if number_list[j] > number_list[j + 1]:
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
    plt.show()
