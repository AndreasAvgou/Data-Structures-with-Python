# Data Structures & Algorithms with Python

This repository contains a collection collection of Python scripts developed for **Data Structures & Algorithms**.
The exercises are focusing on understanding fundamental algorithms, memory management, and efficient data manipulation.

## 📂 Project Structure

### 🔹 1: Array Operations
**Focus:** Basic array manipulation and modular programming.
This lab demonstrates fundamental operations on arrays using a modular architecture (separation of concerns).

* **Key Concepts:**
    * Linear Search (Finding Minimum).
    * Statistical Calculations (Sum, Average).
    * Input Validation & Retrieval.
    * Conditional Counting (Negative numbers).
* **Files:** `inputs.py`, `display.py`, `search.py`, `stats.py`, `counting.py`, `retrieve.py`.

---

### 🔹 2: AVL Trees (Self-Balancing BST)
**Focus:** Advanced tree data structures and recursion.
Implementation of an AVL Tree, a self-balancing Binary Search Tree (BST) that maintains $O(\log n)$ height complexity.

* **Key Concepts:**
    * **BST Operations:** Insertion and Deletion.
    * **Balancing Logic:** Tracking node height and balance factors.
    * **Rotations:** Implementation of Left (`leftRotate`) and Right (`rightRotate`) rotations to handle LL, RR, LR, and RL imbalances.
    * **Traversal:** Pre-order traversal to visualize structure.
* **Files:** `node.py`, `operations.py`, `rotations.py`, `utils.py`, `traversal.py`.
  
---

### 🔹3: Graph Algorithms (BFS)
**Focus:** Graph Traversal and Matrix Representation.
Implementation of the **Breadth-First Search (BFS)** algorithm to traverse a graph.

* **Key Concepts:**
    * **Adjacency Matrix:** Representing graph connections using a 2D array (10x10 matrix).
    * **Custom Queue:** Manual implementation of a Queue class using pointers (`front`, `rear`) instead of built-in libraries.
    * **BFS Algorithm:** Level-order traversal using a queue and a visited array (`mark`) to prevent cycles.
* **Files:** * `main.py`: Defines the graph matrix and handles user input.
    * `graph_algo.py`: Contains the BFS logic.
    * `my_queue.py`: Custom Queue class implementation using arrays.
---

### 🔹 4: Graph Algorithms (DFS)
**Focus:** Graph Traversal using Recursion.
Implementation of the **Depth-First Search (DFS)** algorithm. unlike BFS, this algorithm explores as far as possible along each branch before backtracking.
* **Key Concepts:**
    * **Recursion:** Uses the system call stack (LIFO) instead of a manual data structure.
    * **Backtracking:** The algorithm retreats when it hits a dead end or a visited node.
    * **Visited Array:** Prevents infinite loops in cyclic graphs.
* **Files:** `main.py`, `dfs_algo.py`.

---

*(More will be added)*

## 🚀 How to Run

Each one is contained within its own module/folder. To run a specific :

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```

2.  **Navigate to the Lab folder** (e.g., for Lab 2):
    ```bash
    cd 2_AVLTrees
    ```

3.  **Run the main script:**
    ```bash
    python main.py
    ```

## 🛠️ Technologies Used

* **Language:** Python 3.x
* **Tools:** Standard Library (no external dependencies required).

