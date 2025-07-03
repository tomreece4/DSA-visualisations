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
    colors = ['green'] * size_of_array
    plt.bar(x, number_list, color=colors)
    plt.show()


def selection_sort(size_of_array):
    number_list = np.random.randint(0, 100, size_of_array)
    x = np.arange(0, size_of_array, 1)

    for i in range(size_of_array):
        # Assume the current position holds
        # the minimum element
        min_idx = i
        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, size_of_array):
            colors = ['blue'] * size_of_array
            colors[j] = 'red'
            colors[min_idx] = 'red'
            plt.bar(x, number_list, color=colors)
            plt.pause(0.01)
            plt.clf()
            if number_list[j] < number_list[min_idx]:
                # Update min_idx if a smaller element is found
                min_idx = j
        number_list[i], number_list[min_idx] = number_list[min_idx], number_list[i]
    colors = ['green'] * size_of_array
    plt.bar(x, number_list, color=colors)
    plt.show()


def insertion_sort(size_of_array):
    number_list = np.random.randint(0, 100, size_of_array)
    x = np.arange(0, size_of_array, 1)
    for i in range(1, len(number_list)):
        key = number_list[i]
        j = i - 1
        while j >= 0 and key < number_list[j]:
            number_list[j + 1] = number_list[j]

            temp_list = number_list.copy()
            temp_list[j + 1] = key

            colors = ['blue'] * size_of_array
            colors[j] = 'red'
            colors[j + 1] = 'purple'

            plt.bar(x, temp_list, color=colors)
            plt.pause(0.5)
            plt.clf()

            j -= 1

        number_list[j + 1] = key

    colors = ['green'] * size_of_array
    plt.bar(x, number_list, color=colors)
    plt.show()


insertion_sort(15)
