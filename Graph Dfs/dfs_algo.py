# Filename: dfs_algo.py

def dfs_recursive(current_node, matrix, visited):
    """
    Helper function that performs the actual recursion.
    """
    N = len(matrix)
    
    # Mark the current node as visited
    visited[current_node] = 1
    print("Now in node %d" % (current_node + 1))
    
    # Check all adjacent nodes
    for j in range(N):
        # If there is a connection (1) and it has not been visited (0)
        if matrix[current_node][j] == 1 and visited[j] == 0:
            dfs_recursive(j, matrix, visited)

def run_dfs(start_node, matrix):
    """
    Wrapper function to initialize the visited array and start DFS.
    """
    N = len(matrix)
    
    # Initialize the Mark/visited array with 0s
    # This replaces the global 'Mark' variable
    visited = [0] * N
    
    print(f"\n--- Starting DFS from Node {start_node + 1} ---")
    
    # Start the recursive process
    dfs_recursive(start_node, matrix, visited)
    
    print("--- DFS Completed ---\n")