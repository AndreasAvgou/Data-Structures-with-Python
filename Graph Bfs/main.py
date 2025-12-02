# Filename: main.py
from graph_algo import bfs

def get_user_input(N):
    try:
        p = input("Give start node (1-%d) or out of range to exit: " % (N))
        return int(p)
    except ValueError:
        return -1 # Return invalid to trigger exit or retry

def main():
    # Adjacency Matrix
    graph_matrix = [
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    ]

    N = len(graph_matrix)

    # Input Loop
    start_node = get_user_input(N)
    
    while 1 <= start_node <= N:
        # Run BFS (sending start_node - 1 because Python is 0-indexed)
        bfs(start_node - 1, graph_matrix)
        
        # Ask again
        start_node = get_user_input(N)

    print("Exiting program.")

if __name__ == "__main__":
    main()