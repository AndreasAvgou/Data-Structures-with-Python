# Filename: graph_algo.py
from my_queue import GraphQueue

def bfs(start_node, matrix):
    N = len(matrix)
    
    # Create the visited array (Mark) initialized to 0
    mark = [0] * N
    
    # Initialize the Queue with size N*N (as per original code)
    q_size = N * N
    my_q = GraphQueue(q_size)
    
    # Step 1: Enqueue the start node
    flag = my_q.enqueue(start_node)
    mark[start_node] = 1
    
    print(f"\n--- Starting BFS from Node {start_node + 1} ---")

    # Step 2: Loop while queue is not empty (flag == 1 means success)
    while flag == 1:
        i, flag = my_q.dequeue()
        
        if flag == 1:
            print("Visiting Node: %d" % (i + 1))
            
            # Check neighbors
            for j in range(N):
                # If there is an edge (1) and not visited (0)
                if matrix[i][j] == 1 and mark[j] == 0:
                    my_q.enqueue(j)
                    mark[j] = 1
    print("--- BFS Completed ---\n")