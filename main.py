import sorting_algorithms

choice = input("Select an algorithm: ")
if choice == "bubble sort":
    size = int(input("How many values would you like to apply bubble sort to: "))
    sorting_algorithms.bubble_sort(size)