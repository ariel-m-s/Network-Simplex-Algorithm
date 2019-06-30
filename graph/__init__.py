from typing import (Union, TextIO, Iterable)
from graph.node import Node
from graph.exceptions import (DimensionsCorruptError,
                              NodesCorruptError, EdgesCorruptError,
                              EdgeNotFoundError)
from graph.utilities import verify_node_existance


class Graph:
    def __init__(self, path: str):
        self.nodes = dict()
        self.base_size = 0

        self._load(path)

    @property
    def is_balanced(self) -> bool:
        return sum(map(lambda x: x.supply, self.nodes.values())) == 0

    def _add_node(self, id_: int, supply: int):
        self.nodes[id_] = Node(id_, supply)

    @verify_node_existance
    def _add_edge(self, from_id: int, to_id: int, cost: int):
        self.nodes[from_id].point_to(to_id, cost)
        self.nodes[to_id].get_pointed_by(from_id, cost)

    @staticmethod
    def _get_line_data(file: TextIO) -> Iterable:
        return map(lambda x: float(x) if "." in x else int(x),
                   file.readline().strip().split(","))

    def _load(self, path: int):
        with open(file=path, mode="r") as file:
            try:
                N, A = map(int, Graph._get_line_data(file))
            except (TypeError, ValueError):
                raise DimensionsCorruptError()

            try:
                for _ in range(N):
                    node_data = Graph._get_line_data(file)
                    self._add_node(*node_data)
            except (TypeError, ValueError):
                raise NodesCorruptError()

            try:
                for _ in range(A):
                    edge_data = Graph._get_line_data(file)
                    self._add_edge(*edge_data)
            except (TypeError, ValueError):
                raise EdgesCorruptError()

    @verify_node_existance
    def set_flow(self, from_id: int, to_id: int, value: Union[None, int]):
        from_node = self.nodes[from_id]
        to_node = self.nodes[to_id]

        from_node.set_flow_to(to_id, value)
        to_node.set_flow_from(from_id, value)

    @verify_node_existance
    def increment_flow_safe(self, from_id: int, to_id: int, value: int):
        from_node = self.nodes[from_id]

        try:
            current_value = from_node.out_[to_id]["flow"]
        except KeyError:
            raise EdgeNotFoundError(from_id, to_id)

        self.set_flow(from_id, to_id, (current_value or 0) + value)

    def __repr__(self):
        return "\n\n".join(repr(node) for node in self.nodes.values())
