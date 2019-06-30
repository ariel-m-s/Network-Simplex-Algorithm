from sys import argv
from graph import Graph
from simplex import solve


if __name__ == "__main__":
    graph = Graph(argv[1])

    # Set initial feasible solution
    graph.base_size = 3
    graph.set_flow(from_id=1, to_id=2, value=4)
    graph.set_flow(from_id=2, to_id=3, value=6)
    graph.set_flow(from_id=3, to_id=4, value=5)

    solve(graph)

    print(graph)
