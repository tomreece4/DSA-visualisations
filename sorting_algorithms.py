import matplotlib.pyplot as plt
import numpy as np


# Performs a bubble sort on the specified amount of random numbers from 0-100
def bubble_sort(size_of_array, speed):
    number_list = np.random.randint(0, 100, size_of_array)
    x = np.arange(0, size_of_array, 1)

    for i in range(size_of_array):
        for j in range(0, size_of_array - i - 1):
            colors = ['blue'] * size_of_array
            colors[j] = 'red'
            colors[j + 1] = 'red'
            plt.bar(x, number_list, color=colors)
            plt.pause(speed)
            plt.clf()
            if number_list[j] > number_list[j + 1]:
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
    colors = ['green'] * size_of_array
    plt.bar(x, number_list, color=colors)
    plt.show()


def selection_sort(size_of_array, speed):
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
            plt.pause(speed)
            plt.clf()
            if number_list[j] < number_list[min_idx]:
                # Update min_idx if a smaller element is found
                min_idx = j
        number_list[i], number_list[min_idx] = number_list[min_idx], number_list[i]
    colors = ['green'] * size_of_array
    plt.bar(x, number_list, color=colors)
    plt.show()


def insertion_sort(size_of_array, speed):
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
            plt.pause(speed)
            plt.clf()

            j -= 1

        number_list[j + 1] = key

    colors = ['green'] * size_of_array
    plt.bar(x, number_list, color=colors)
    plt.show()


def quick_sort(size_of_array,speed):
    number_list = np.random.randint(0, 100, size_of_array)
    x = np.arange(size_of_array)

    def partition(low, high):
        pivot = number_list[high]
        i = low - 1
        # visualize pivot selection
        for j in range(low, high):
            # color current element and pivot
            colors = ['blue'] * size_of_array
            colors[j] = 'red'
            colors[high] = 'purple'
            plt.bar(x, number_list, color=colors)
            plt.pause(speed)
            plt.clf()

            if number_list[j] <= pivot:
                i += 1
                # swap elements
                number_list[i], number_list[j] = number_list[j], number_list[i]
                colors = ['blue'] * size_of_array
                colors[i] = 'red'
                colors[j] = 'red'
                plt.bar(x, number_list, color=colors)
                plt.pause(speed)
                plt.clf()

        # place pivot in correct position
        number_list[i + 1], number_list[high] = number_list[high], number_list[i + 1]
        colors = ['blue'] * size_of_array
        colors[i + 1] = 'red'
        colors[high] = 'red'
        plt.bar(x, number_list, color=colors)
        plt.pause(speed)
        plt.clf()
        return i + 1

    def _quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            _quick_sort(low, pi - 1)
            _quick_sort(pi + 1, high)

    _quick_sort(0, size_of_array - 1)

    # final sorted array in green
    colors = ['green'] * size_of_array
    plt.bar(x, number_list, color=colors)
    plt.show()


def merge_sort(size_of_array, speed):
    """
     Generates a random array of given size and visualizes merge sort step by step.
     """
    arr = np.random.randint(0, 100, size_of_array)
    x = np.arange(size_of_array)

    def merge(left, mid, right):
        # Copy subarrays
        L = arr[left:mid + 1].copy()
        R = arr[mid + 1:right + 1].copy()
        i = 0
        j = 0
        k = left
        # Merge back into arr
        while i < len(L) and j < len(R):
            # Highlight elements being compared
            colors = ['blue'] * size_of_array
            colors[left + i] = 'red'
            colors[mid + 1 + j] = 'purple'
            plt.bar(x, arr, color=colors)
            plt.pause(speed)
            plt.clf()

            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            # Show the placement
            colors = ['blue'] * size_of_array
            colors[k - 1] = 'red'
            plt.bar(x, arr, color=colors)
            plt.pause(speed)
            plt.clf()

        # Copy any remaining elements of L
        while i < len(L):
            arr[k] = L[i]
            colors = ['blue'] * size_of_array
            colors[k] = 'red'
            plt.bar(x, arr, color=colors)
            plt.pause(speed)
            plt.clf()
            i += 1
            k += 1

        # Copy any remaining elements of R
        while j < len(R):
            arr[k] = R[j]
            colors = ['blue'] * size_of_array
            colors[k] = 'purple'
            plt.bar(x, arr, color=colors)
            plt.pause(speed)
            plt.clf()
            j += 1
            k += 1

    def _merge_sort(left, right):
        if left < right:
            mid = (left + right) // 2
            _merge_sort(left, mid)
            _merge_sort(mid + 1, right)
            merge(left, mid, right)

    _merge_sort(0, size_of_array - 1)

    # Final display in green
    colors = ['green'] * size_of_array
    plt.bar(x, arr, color=colors)
    plt.show()
