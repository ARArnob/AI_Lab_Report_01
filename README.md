# Lab Report 01: IDDFS Implementation

**Student Name:** [Md. Ariful Islam Arnob]
**Student ID:** [232002238]  
**Course:** CSE-316

This repository contains a Python implementation of the **Iterative Deepening Depth-First Search (IDDFS)** algorithm, completed for the CSE316 Artificial Intelligence Lab.

## Objective

The goal is to determine if a valid path exists from a given starting cell to a target cell within a 2D grid. The algorithm navigates adjacent cells (Up, Down, Left, Right) while avoiding walls (represented by `1`), ensuring that each empty cell (`0`) is visited optimally within expanding depth limits.

## How to Run

Run the Python script in your terminal and provide the inputs (grid dimensions, grid layout, start coordinates, and target coordinates).

```bash
python iddfs.py

```

## Example Test Case

**Input:**

```text
4 4
0 1 0 1
0 0 0 1
1 1 0 0
0 0 1 0
Start: 0 0
Target: 2 3

```

**Output:**

```text
Path found at depth 5 using IDDFS
Traversal Order: [(0,0), (1,0), (1,1), (1,2), (2,2), (2,3)]

```
