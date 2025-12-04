# Data Structures & Algorithms with Python

This repository contains a collection collection of Python scripts developed .
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

### 🔹 5: Singly Linked List
**Focus:** Dynamic Data Structures and Pointers.
Implementation of a **Sorted Singly Linked List**. Unlike arrays, elements (Nodes) are not stored in contiguous memory but are linked via pointers.
* **Key Concepts:**
    * **The Node:** An object containing data and a reference (`next`) to the following node.
    * **Sorted Insertion:** The `insert_node` function scans the list to place new numbers in ascending order automatically.
    * **Dynamic Memory:** Nodes are created and removed on the fly (`insert`/`delete`).
* **Files:** `main.py`, `linked_list.py`, `node.py`, `utils.py`.

---

### 🔹  6: Sorting Algorithms
**Focus:** Algorithmic Efficiency ($O(n^2)$ vs $O(n \log n)$).
A comprehensive suite of sorting algorithms implemented to demonstrate different strategies for ordering data.
* **Algorithms Implemented:**
    1.  **Bubble Sort:** Swaps adjacent elements repeatedly.
    2.  **Insertion Sort:** Builds the sorted array one item at a time.
    3.  **Selection Sort:** repeatedly finds the minimum element.
    4.  **Shell Sort:** A generalization of insertion sort using gaps (powers of 2).
    5.  **QuickSort:** Recursive divide-and-conquer strategy using a pivot.
* **Key Features:** Menu-driven interface, data copying (to preserve the original dataset for multiple tests), and modular design.
* **Files:** `main.py`, `algorithms.py`, `handlers.py`, `utils.py`.

---

### 🔹 7: Search & Sort Integration
**Focus:** Relationship between Sorting and Searching.
Demonstrates how Binary Search requires sorted data (using QuickSort) to function correctly.
* **Key Concepts:** Sequential Search vs Binary Search, Handling unsorted inputs.
* **Files:** `main.py`, `handlers.py`, `searching.py`, `sorting.py`.

---

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

