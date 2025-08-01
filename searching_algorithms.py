import matplotlib.pyplot as plt
import numpy as np

def linear_search(size_of_array, speed, target=None):
    number_list = np.random.randint(0, 100, size_of_array)
    x = np.arange(size_of_array)

    if target is None:
        target = np.random.choice(number_list)  # Pick a target that definitely exists

    found = False
    for i in range(size_of_array):
        colors = ['blue'] * size_of_array
        colors[i] = 'red'  # Highlight current element being compared
        plt.bar(x, number_list, color=colors)
        plt.title(f"Searching for: {target}")
        plt.pause(speed)
        plt.clf()
        if number_list[i] == target:
            colors[i] = 'green'
            plt.bar(x, number_list, color=colors)
            plt.title(f"Found: {target} at index {i}")
            plt.pause(0.5)
            plt.clf()
            found = True
            break

    if not found:
        plt.bar(x, number_list, color='blue')
        plt.title(f"{target} not found in array.")
        plt.pause(speed)
        plt.clf()

    colors = ['green' if number_list[i] == target else 'blue' for i in range(size_of_array)]
    plt.bar(x, number_list, color=colors)
    plt.title("Search Complete")
    plt.bar(x, number_list, color='green')
    plt.show()
