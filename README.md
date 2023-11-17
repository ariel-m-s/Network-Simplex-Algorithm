# Network Simplex algorithm implementation in Python

## Overview

This repository contains a Python implementation of the Network Simplex algorithm, a widely used optimization algorithm for solving network flow problems. The algorithm is designed to efficiently find the optimal flow in a network, considering both capacities and costs associated with the edges.

## Features

- **Network Simplex algorithm**: The repository includes the implementation of the Network Simplex algorithm in Python, providing a powerful tool for solving network flow optimization problems.

- **Graph representation**: The graph is represented using a CSV file, making it easy to input custom graphs for optimization.

- **Error handling**: The code includes comprehensive error handling to ensure robustness and graceful handling of potential issues during execution.

## Files and structure

1. `simplex.py`

This file contains the implementation of the Network Simplex algorithm. The algorithm is designed to work with a graph representation of the optimization problem. It includes functions for calculating potentials, determining reduced costs, finding cycles, updating flow, and solving the optimization problem.

2. `main.py`

This file provides an example of how to use the program. It demonstrates how to create a graph, set an initial feasible solution, and solve the optimization problem using the Network Simplex algorithm.

3. `graph/__init__.py`

This file initializes the Graph class, representing the graph used in the Network Simplex algorithm. It includes methods for adding nodes and edges, loading graph data from a file, setting flow values, and checking if the graph's supplies are balanced.

This file initializes the `graph` module, which contains the necessary components for representing the graph used in the algorithm.

6. `graph/exceptions.py`

This file defines custom exceptions (for error handling) that may be raised during the algorithm's execution. These exceptions include errors related to missing graph elements, corrupt graph files, unbalanced supplies, wrong base size, unfulfilled node supplies, and negative cycles.

9. `graph/node.py`

This file defines the `Node` class, representing a graph node. Each node contains information about its ID, supply, and incoming and outgoing edges. The class includes methods for setting flow values.

8. `graph/utilities.py`

Utility functions for graph operations, including a function for verifying the existence of nodes before performing operations on them.

## Example usage

To use the program, follow these steps:

- Create a CSV file representing the graph, following the specified format.
- Use the `Graph` class to load the graph from the CSV file.
- Set an initial feasible solution using the `set_flow` method.
- Call the `solve` function from `simplex.py` to solve the optimization problem.

An example of this can be found in the `main.py` file.

Then, to run the program:

```bash
python main.py path/to/your/graph.csv
```

Replace `path/to/your/graph.csv` with the path to your custom graph file.

## Custom graph file format

The graph is represented in a CSV file with the following format:

- The first line should contain the dimensions of the graph in the format: `<N>, <A>`, where `N` is the number of nodes and `A` is the number of edges.
- The next `N` lines should contain information about each node in the format: `<node_id>, <node_supply>` (demand is represented as negative supply).
- The following `A` lines should contain information about each edge in the format: `<node_from_id>, <node_to_id>, <edge_cost>`.

Make sure to provide a properly formatted graph file for the algorithm to work correctly. See an example in `data/graph.csv`.

Note: Ensure the input graph is balanced and the base size equals N - 1. The algorithm expects a feasible solution as an initial state.
