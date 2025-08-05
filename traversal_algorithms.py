import matplotlib.pyplot as plt
import numpy as np
from collections import deque


# Compute positions for a binary tree so that it's laid out nicely
def compute_positions(num_nodes):
    pos = {}

    def _pos(idx, x, y, dx):
        if idx >= num_nodes:
            return
        pos[idx] = (x, y)
        # left child
        _pos(2 * idx + 1, x - dx, y - 1, dx / 2)
        # right child
        _pos(2 * idx + 2, x + dx, y - 1, dx / 2)

    _pos(0, 0.5, 0, 0.25)
    return pos


def dfs_visualize(depth, speed):
    """
    Build a complete binary tree of depth `depth` (so 2**depth - 1 nodes),
    then animate a pre-order DFS on it.
    """
    # number of nodes in a full binary tree of this depth
    num_nodes = 2 ** depth - 1
    # random values for each node
    values = np.random.randint(0, 100, size=num_nodes)
    # precompute (x,y) for drawing
    pos = compute_positions(num_nodes)

    visited = set()

    def _dfs(idx):
        visited.add(idx)

        # First draw all the edges _behind_ the nodes:
        for parent in range(num_nodes):
            for child in (2 * parent + 1, 2 * parent + 2):
                if child < num_nodes:
                    x0, y0 = pos[parent]
                    x1, y1 = pos[child]
                    plt.plot([x0, x1], [y0, y1],
                             color='gray',
                             zorder=1)  # low z-order = behind

        # Then draw all the nodes on top:
        for i in range(num_nodes):
            x, y = pos[i]
            if i == idx:
                c = 'red'
            elif i in visited:
                c = 'green'
            else:
                c = 'blue'
            plt.scatter(x, y,
                        s=800,
                        color=c,
                        zorder=2)  # higher z-order = front
            plt.text(x, y,
                     str(values[i]),
                     va='center',
                     ha='center',
                     color='white',
                     zorder=3)  # even above the dots

        plt.axis('off')
        plt.pause(speed)
        plt.cla()

        # recurse…
        left = 2 * idx + 1
        if left < num_nodes:
            _dfs(left)
        right = 2 * idx + 2
        if right < num_nodes:
            _dfs(right)

    # start recursion
    _dfs(0)

    # final state: all green
    for i in range(num_nodes):
        x, y = pos[i]
        plt.scatter(x, y, s=800, color='green', zorder=3)
        plt.text(x, y, str(values[i]), va='center', ha='center', color='white')
    for parent in range(num_nodes):
        for child in (2 * parent + 1, 2 * parent + 2):
            if child < num_nodes:
                x0, y0 = pos[parent]
                x1, y1 = pos[child]
                plt.plot([x0, x1], [y0, y1], color='gray')
    plt.axis('off')
    plt.show()


def bfs_visualize(depth, speed):
    num_nodes = 2 ** depth - 1
    values = np.random.randint(0, 100, size=num_nodes)
    pos = compute_positions(num_nodes)
    visited = set()
    queue = deque([0])

    while queue:
        idx = queue.popleft()
        visited.add(idx)

        # 1) draw all edges underneath
        for parent in range(num_nodes):
            for child in (2 * parent + 1, 2 * parent + 2):
                if child < num_nodes:
                    x0, y0 = pos[parent]
                    x1, y1 = pos[child]
                    plt.plot([x0, x1], [y0, y1],
                             color='gray',
                             zorder=1)

        # 2) draw nodes on top
        for i in range(num_nodes):
            x, y = pos[i]
            if i == idx:
                col = 'red'
            elif i in visited:
                col = 'green'
            else:
                col = 'blue'
            plt.scatter(x, y,
                        s=800,
                        color=col,
                        zorder=2)
            plt.text(x, y,
                     str(values[i]),
                     va='center',
                     ha='center',
                     color='white',
                     zorder=3)

        plt.axis('off')
        plt.pause(speed)
        plt.cla()

        # enqueue children
        left, right = 2 * idx + 1, 2 * idx + 2
        if left < num_nodes:  queue.append(left)
        if right < num_nodes: queue.append(right)

    # final state: all green
    for parent in range(num_nodes):
        for child in (2 * parent + 1, 2 * parent + 2):
            if child < num_nodes:
                x0, y0 = pos[parent]
                x1, y1 = pos[child]
                plt.plot([x0, x1], [y0, y1],
                         color='gray',
                         zorder=1)
    for i in range(num_nodes):
        x, y = pos[i]
        plt.scatter(x, y,
                    s=800,
                    color='green',
                    zorder=2)
        plt.text(x, y,
                 str(values[i]),
                 va='center',
                 ha='center',
                 color='white',
                 zorder=3)

    plt.axis('off')
    plt.show()

