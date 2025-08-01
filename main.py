import searching_algorithms
import sorting_algorithms
import traversal_algorithms

if __name__ == "__main__":

    import tkinter as tk
    from tkinter import ttk, messagebox

    def update_param_slider(*args):
        algo = algo_var.get()
        if algo in ["Bubble Sort", "Selection Sort", "Insertion Sort", "Quick Sort", "Merge Sort", "Linear Search", "Binary Search"]:
            param_slider.config(from_=5, to=200)
            param_slider.set(30)
        elif algo in ["Depth-First Search", "Breadth-First Search"]:
            param_slider.config(from_=2, to=5)
            param_slider.set(4)

    def run():
        algo = algo_var.get()
        param = int(param_var.get())
        speed = speed_var.get()

        if algo == "Bubble Sort":
            sorting_algorithms.bubble_sort(param, speed)
        elif algo == "Selection Sort":
            sorting_algorithms.selection_sort(param, speed)
        elif algo == "Insertion Sort":
            sorting_algorithms.insertion_sort(param, speed)
        elif algo == "Quick Sort":
            sorting_algorithms.quick_sort(param, speed)
        elif algo == "Merge Sort":
            sorting_algorithms.merge_sort(param, speed)
        elif algo == "Depth-First Search":
            traversal_algorithms.dfs_visualize(param, speed)
        elif algo == "Breadth-First Search":
            traversal_algorithms.bfs_visualize(param, speed)
        elif algo == "Linear Search":
            searching_algorithms.linear_search(param, speed)
        elif algo == "Binary Search":
            searching_algorithms.binary_search(param, speed)

    # GUI setup
    root = tk.Tk()
    root.title("Algorithm Visualizer")

    mainframe = ttk.Frame(root, padding=10)
    mainframe.pack(fill=tk.BOTH, expand=True)

    # Algorithm selection
    ttk.Label(mainframe, text="Algorithm:").grid(column=0, row=0, sticky=tk.W)
    algo_var = tk.StringVar(value="Bubble Sort")
    algo_menu = ttk.Combobox(mainframe, textvariable=algo_var, state="readonly",
                              values=[
                                  "Bubble Sort",
                                  "Selection Sort",
                                  "Insertion Sort",
                                  "Quick Sort",
                                  "Merge Sort",
                                  "Depth-First Search",
                                  "Breadth-First Search",
                                  "Linear Search",
                                  "Binary Search",
                              ])
    algo_menu.grid(column=1, row=0, sticky=tk.EW)
    algo_menu.bind("<<ComboboxSelected>>", update_param_slider)

    # Parameter slider with label
    ttk.Label(mainframe, text="Size / Depth:").grid(column=0, row=1, sticky=tk.W)
    param_var = tk.DoubleVar(value=30)
    param_slider = ttk.Scale(mainframe, variable=param_var, from_=5, to=200, orient="horizontal",
                             command=lambda val: param_value_label.config(text=str(int(float(val)))))
    param_slider.grid(column=1, row=1, sticky=tk.EW)
    param_value_label = ttk.Label(mainframe, text=str(int(param_var.get())), width=5)
    param_value_label.grid(column=2, row=1, sticky=tk.W)

    # Speed slider with live value display
    ttk.Label(mainframe, text="Frame Delay (secs)").grid(column=0, row=2, sticky=tk.W)
    speed_var = tk.DoubleVar(value=0.1)
    speed_slider = ttk.Scale(mainframe, variable=speed_var, from_=0.1, to=1, orient="horizontal",
                             command=lambda val: speed_value_label.config(text=f"{float(val):.2f}"))
    speed_slider.grid(column=1, row=2, sticky=tk.EW)
    speed_value_label = ttk.Label(mainframe, text=f"{speed_var.get():.2f}", width=5)
    speed_value_label.grid(column=2, row=2, sticky=tk.W)

    # Run button
    run_button = ttk.Button(mainframe, text="Run", command=run)
    run_button.grid(column=0, row=3, columnspan=2, pady=5)

    # Make columns expand
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    mainframe.columnconfigure(1, weight=1)

    update_param_slider()
    root.mainloop()

