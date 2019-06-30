from typing import Union
from pprint import pformat
from graph.exceptions import EdgeNotFoundError


class Node:
    def __init__(self, id_: int, supply: int):
        self.id_ = id_
        self.supply = supply

        self.in_ = dict()
        self.out_ = dict()

    def get_pointed_by(self, node_id: int, cost: float):
        self.in_[node_id] = {"cost": cost, "flow": None}

    def point_to(self, node_id: int, cost: float):
        self.out_[node_id] = {"cost": cost, "flow": None}

    def set_flow_from(self, node_id: int, value: Union[None, int]):
        if node_id not in self.in_.keys():
            raise EdgeNotFoundError(node_id, self.id_)
        self.in_[node_id]["flow"] = value

    def set_flow_to(self, node_id: int, value: Union[None, int]):
        if node_id not in self.out_.keys():
            raise EdgeNotFoundError(self.id_, node_id)
        self.out_[node_id]["flow"] = value

    def __repr__(self):
        return pformat({"ID": self.id_, "Supply": self.supply,
                        "In": self.in_, "Out": self.out_})
