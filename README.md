# Graph-Teory-Assignment3-Group-3

## 1. Identity
**Informatics ITS Graph Theory class Group 3**

* Dzulfiqar Rafi'ussunnah - 5025251011
* Padhang Abiyu Fikri - 5025251014
* Aditya Lingga Mardika - 5025251158
* Muhammad Faris Alfarrel - 5025251002

---

## 2. Short Explanation About Algorithms
Our group implemented three distinct algorithms to find an Eulerian Trail or Eulerian Circuit:

* **Fleury’s Algorithm:** Fleury’s Algorithm constructs an Eulerian trail or circuit by traversing each edge exactly once. The algorithm avoids choosing a bridge when another unused edge is available, helping prevent the graph from becoming disconnected before all edges are traversed. The algorithm starts at any vertex if there are no odd-degree vertices, or at one of the odd-degree vertices if there are two
* **Hierholzer’s Algorithm:**Hierholzer’s Algorithm constructs an Eulerian trail or circuit by building cycles from unused edges and merging them into the existing trail. The algorithm starts from an appropriate vertex, follows unused edges until returning to the starting vertex, and then creates additional cycles from vertices that still have unused edges. This process continues until every edge has been used exactly once.
* **Backtracking Algorithm:** A recursive algorithm that constructs an Eulerian trail or circuit by exploring unused edges one at a time. At each step, the algorithm selects an unused edge and continues the traversal. If the selected edge leads to a state where a complete Eulerian trail or circuit cannot be formed, the algorithm backtracks and tries another unused edge. The process continues until all edges have been traversed exactly once.
---

## 3. Prerequisites to Run the Code
* Python 3.x installed on your system.
* A terminal or command-line interface.
* No external libraries are required (only Python standard libraries).
* Install IDE you prefer and run on it.

---

## 4. Instructions to Run the Code
You can run the Python scripts directly from your terminal.

---

## 5. Result of Sample Run
* Hierholzer’s Algorithm
<img width="426" height="195" alt="WhatsApp Image 2026-09-22 at 21 22 30" src="https://github.com/user-attachments/assets/38fbcd97-9dd7-45ca-93f8-0dbf02a1c299" />
<img width="621" height="649" alt="WhatsApp Image 2026-09-22 at 21 22 30 (1)" src="https://github.com/user-attachments/assets/6d2592ee-96b7-4f2b-80cf-9fa771aefc37" />


