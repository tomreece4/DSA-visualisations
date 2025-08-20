import matplotlib.pyplot as plt
import numpy as np

def linear_search(size_of_array, speed, target=None):
    # Generate random list of numbers to search through so that the user doesn't have to write their own list
    number_list = np.random.randint(0, 100, size_of_array)
    x = np.arange(size_of_array)

    # Pick a random target from the list to make the search more authentic
    if target is None:
        target = np.random.choice(number_list)

    found = False
    for i in range(size_of_array):
        # Highlight the current element we're checking in red, to provide a good visual cue to the user
        colors = ['blue'] * size_of_array
        colors[i] = 'red'

        plt.bar(x, number_list, color=colors)
        plt.title(f"Searching for: {target}")
        plt.pause(speed)
        plt.cla()

        if number_list[i] == target:
            # If target found, show it in green
            colors[i] = 'green'
            plt.bar(x, number_list, color=colors)
            plt.title(f"Found: {target} at index {i}")
            plt.pause(0.5)
            plt.cla()
            found = True
            break

    if not found:
        plt.bar(x, number_list, color='blue')
        plt.title(f"{target} not found in array.")
        plt.pause(speed)
        plt.cla()

    # Highlight target occurrence in green, others blue
    colors = ['green' if number_list[i] == target else 'blue' for i in range(size_of_array)]
    plt.bar(x, number_list, color=colors)
    plt.title("Search Complete")
    plt.bar(x, number_list, color='green')
    plt.show()


def binary_search(size_of_array, speed, target=None):
    # Binary search needs to be on a sorted list
    number_list = np.sort(np.random.randint(0, 100, size_of_array))
    x = np.arange(size_of_array)

    # Pick a target from the list, to guarantee it can be found.
    if target is None:
        target = np.random.choice(number_list)

    low = 0
    high = size_of_array - 1
    found = False

    while low <= high:
        mid = (low + high) // 2

        # Colour code:
        # purple for current low/high bounds,
        # red for the middle element we're checking,
        # light grey for elements outside the current search range
        colors = ['blue'] * size_of_array
        colors[low] = 'purple'
        colors[high] = 'purple'
        colors[mid] = 'red'
        for i in range(0, low):
            colors[i] = 'lightgrey'
        for i in range(high+1, size_of_array):
            colors[i] = 'lightgrey'

        plt.bar(x, number_list, color=colors)
        plt.title(f"Target: {target} | Low: {low}, Mid: {mid}, High: {high}")
        plt.pause(speed)
        plt.cla()

        if number_list[mid] == target:
            # Found target, Highlight in green
            colors[mid] = 'green'
            plt.bar(x, number_list, color=colors)
            plt.title(f"Found: {target} at index {mid}")
            plt.pause(1.5)
            plt.bar(x, number_list, color='green')
            plt.pause(1.5)
            plt.cla()
            found = True
            break
        elif number_list[mid] < target:
            low = mid + 1  # Less than target so you want to check higher values
        else:
            high = mid - 1  # Search in the lower half

    # Final plot at the end of the search
    colors = ['green']
    plt.bar(x, number_list, color=colors)
    plt.title("Search Complete" if found else f"{target} not found")
    plt.show()
