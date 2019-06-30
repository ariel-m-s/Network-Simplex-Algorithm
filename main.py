from graph import Graph
from simplex import solve


if __name__ == "__main__":
    graph = Graph("data/graph.csv")

    # Set initial feasible solution
    graph.base_size = 3
    graph.set_flow(1, 2, 4)
    graph.set_flow(2, 3, 6)
    graph.set_flow(3, 4, 5)

    solve(graph)

    print(graph)
