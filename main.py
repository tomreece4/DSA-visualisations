import searching_algorithms
import sorting_algorithms
import traversal_algorithms

if __name__ == "__main__":

    import tkinter as tk
    from tkinter import ttk, messagebox

    def run():
        algo = algo_var.get()
        try:
            param = int(param_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter an integer parameter.")
            return

        speed = speed_var.get()

        # call the corresponding visualization function
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
                                  "Linear Search"
                              ])
    algo_menu.grid(column=1, row=0, sticky=tk.EW)

    # Parameter entry (array size or tree depth)
    ttk.Label(mainframe, text="Size / Depth:").grid(column=0, row=1, sticky=tk.W)
    param_entry = ttk.Entry(mainframe)
    param_entry.grid(column=1, row=1, sticky=tk.EW)
    param_entry.insert(0, "20")

    # Speed slider
    ttk.Label(mainframe, text="Speed").grid(column=0, row=2, sticky=tk.W)
    speed_var = tk.DoubleVar(value=0.1)
    speed_slider = ttk.Scale(mainframe, variable=speed_var, from_=1.0, to=0.01, orient="horizontal")
    speed_slider.grid(column=1, row=2, sticky=tk.EW)

    # Run button
    run_button = ttk.Button(mainframe, text="Run", command=run)
    run_button.grid(column=0, row=3, columnspan=2, pady=5)


    # Make columns expand
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    mainframe.columnconfigure(1, weight=1)

    root.mainloop()
