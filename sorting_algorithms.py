import matplotlib.pyplot as plt
import numpy as np


def bubble_sort(size_of_array, speed):
    # Create a random list to sort
    number_list = np.random.randint(0, 100, size_of_array)
    x = np.arange(size_of_array)

    for i in range(size_of_array):
        sorted_boundary = size_of_array - i  # Last i elements are sorted already

        for j in range(0, sorted_boundary - 1):
            # Blue for unsorted, green for sorted, red for current pair
            colors = ['blue'] * size_of_array
            for k in range(sorted_boundary, size_of_array):
                colors[k] = 'green'
            colors[j] = 'red'
            colors[j + 1] = 'red'

            plt.bar(x, number_list, color=colors)
            plt.pause(speed)
            plt.cla()

            # Swap if out of order
            if number_list[j] > number_list[j + 1]:
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]

                # Show swapped elements in orange briefly
                colors = ['blue'] * size_of_array
                for k in range(sorted_boundary, size_of_array):
                    colors[k] = 'green'
                colors[j] = 'orange'
                colors[j + 1] = 'orange'

                plt.bar(x, number_list, color=colors)
                plt.pause(speed)
                plt.cla()

    # Highlight sorted array in green
    colors = ['green'] * size_of_array
    plt.bar(x, number_list, color=colors)
    plt.show()


def selection_sort(size_of_array, speed):
    number_list = np.random.randint(0, 100, size_of_array)
    x = np.arange(size_of_array)

    for i in range(size_of_array):
        min_idx = i

        for j in range(i + 1, size_of_array):
            # Blue for unsorted, green for sorted, red for current candidate,
            # yellow for current minimum
            colors = ['blue'] * size_of_array
            for k in range(i):
                colors[k] = 'green'
            colors[j] = 'red'
            colors[min_idx] = 'yellow'

            plt.bar(x, number_list, color=colors)
            plt.pause(speed)
            plt.cla()

            if number_list[j] < number_list[min_idx]:
                min_idx = j

        # Swap the found minimum into place
        number_list[i], number_list[min_idx] = number_list[min_idx], number_list[i]

        # Show swapped elements in orange
        colors = ['blue'] * size_of_array
        for k in range(i + 1):
            colors[k] = 'green'
        colors[i] = 'orange'
        colors[min_idx] = 'orange'

        plt.bar(x, number_list, color=colors)
        plt.pause(speed)
        plt.cla()

    # Array sorted
    colors = ['green'] * size_of_array
    plt.bar(x, number_list, color=colors)
    plt.show()


def insertion_sort(size_of_array, speed):
    number_list = np.random.randint(0, 100, size_of_array)
    x = np.arange(size_of_array)

    plt.figure()
    for i in range(1, size_of_array):
        key = number_list[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and number_list[j] > key:
            number_list[j + 1] = number_list[j]

            temp = number_list.copy()
            temp[i] = key  # Place key for visualisation

            # Green for sorted part, red for current element being compared,
            # yellow for key
            colors = ['blue'] * size_of_array
            for k in range(i + 1):
                colors[k] = 'green'
            colors[j] = 'red'
            colors[i] = 'yellow'

            plt.cla()
            plt.bar(x, temp, color=colors)
            plt.ylim(0, 110)
            plt.pause(speed)

            j -= 1

        # Insert key at correct position
        number_list[j + 1] = key

        colors = ['blue'] * size_of_array
        for k in range(i + 1):
            colors[k] = 'green'
        colors[j + 1] = 'orange'

        plt.cla()
        plt.bar(x, number_list, color=colors)
        plt.ylim(0, 110)
        plt.pause(speed)

    plt.cla()
    colors = ['green'] * size_of_array
    plt.bar(x, number_list, color=colors)
    plt.ylim(0, 110)
    plt.show()


def quick_sort(size_of_array, speed):
    number_list = np.random.randint(0, 100, size_of_array)
    x = np.arange(size_of_array)

    def partition(low, high):
        pivot = number_list[high]
        i = low - 1
        for j in range(low, high):
            # Red for current element, purple for pivot
            colors = ['blue'] * size_of_array
            colors[j] = 'red'
            colors[high] = 'purple'
            plt.bar(x, number_list, color=colors)
            plt.pause(speed)
            plt.cla()

            if number_list[j] <= pivot:
                i += 1
                number_list[i], number_list[j] = number_list[j], number_list[i]
                colors = ['blue'] * size_of_array
                colors[i] = 'red'
                colors[j] = 'red'
                plt.bar(x, number_list, color=colors)
                plt.pause(speed)
                plt.cla()

        number_list[i + 1], number_list[high] = number_list[high], number_list[i + 1]
        colors = ['blue'] * size_of_array
        colors[i + 1] = 'red'
        colors[high] = 'red'
        plt.bar(x, number_list, color=colors)
        plt.pause(speed)
        plt.cla()
        return i + 1

    def _quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            _quick_sort(low, pi - 1)
            _quick_sort(pi + 1, high)

    _quick_sort(0, size_of_array - 1)

    colors = ['green'] * size_of_array
    plt.bar(x, number_list, color=colors)
    plt.show()


def merge_sort(size_of_array, speed):
    arr = np.random.randint(0, 100, size_of_array)
    x = np.arange(size_of_array)

    def draw_array(data, color_map, title=""):
        plt.cla()
        plt.bar(x, data, color=color_map)
        plt.title(title)
        plt.ylim(0, 110)
        plt.pause(speed)

    def merge(left, mid, right):
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        merged = []
        i = j = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                merged.append(L[i])
                i += 1
            else:
                merged.append(R[j])
                j += 1
        merged.extend(L[i:])
        merged.extend(R[j:])

        # Write merged results back to original array and highlight changes
        for idx, val in enumerate(merged):
            arr[left + idx] = val
            colors = ['blue'] * size_of_array
            for i in range(left, right + 1):
                colors[i] = 'purple'
            colors[left + idx] = 'red'
            draw_array(arr, colors, f"Merging {left}-{right}")

    def _merge_sort(left, right):
        if left < right:
            mid = (left + right) // 2

            # Highlight left and right splits in yellow and orange
            colors = ['blue'] * size_of_array
            for i in range(left, mid + 1):
                colors[i] = 'yellow'
            for i in range(mid + 1, right + 1):
                colors[i] = 'orange'
            draw_array(arr, colors, f"Splitting: {left}-{mid} | {mid+1}-{right}")

            _merge_sort(left, mid)
            _merge_sort(mid + 1, right)
            merge(left, mid, right)

    _merge_sort(0, size_of_array - 1)

    draw_array(arr, ['green'] * size_of_array, "Sorted")
    plt.show()



