from functools import reduce
from enum import Enum
from graph.exceptions import (SuppliesNotBalancedError, WrongBaseSizeError)

DeltaSign = Enum('Sign', ['PLUS', 'MINUS'])


def _get_potentials(graph: 'Graph') -> dict:
    potentials = dict()

    for this_id, node in graph.nodes.items():

        if not potentials:
            potentials[this_id] = 0

        if this_id not in potentials.keys():
            continue

        for other_id, edge in node.in_.items():
            if (edge["flow"] is not None and
                    other_id not in potentials.keys()):
                potentials[other_id] = potentials[this_id] + edge["cost"]

        for other_id, edge in node.out_.items():
            if (edge["flow"] is not None and
                    other_id not in potentials.keys()):
                potentials[other_id] = potentials[this_id] - edge["cost"]

    return potentials


def get_reduced_costs(graph: 'Graph') -> dict:
    potentials = _get_potentials(graph)
    reduced_costs = dict()

    for this_id, node in graph.nodes.items():

        for other_id, edge in node.in_.items():
            if (other_id, this_id) not in reduced_costs.keys():
                reduced_costs[other_id, this_id] = edge["cost"] - \
                    (potentials[other_id] - potentials[this_id])

        for other_id, edge in node.out_.items():
            if (this_id, other_id) not in reduced_costs.keys():
                reduced_costs[this_id, other_id] = edge["cost"] - \
                    (potentials[this_id] - potentials[other_id])

    return reduced_costs


def get_cycle(graph: 'Graph', target: int, discovered: list) -> list:
    if discovered[-1][0] == target:
        return discovered

    node = graph.nodes[discovered[-1][0]]

    for other_id, edge in node.in_.items():
        if edge["flow"] is not None and other_id not in discovered:
            cycle = get_cycle(graph, target,
                              discovered + [(other_id, DeltaSign.MINUS)])
            if cycle:
                return cycle

    for other_id, edge in node.out_.items():
        if edge["flow"] is not None and other_id not in discovered:
            cycle = get_cycle(graph, target,
                              discovered + [(other_id, DeltaSign.PLUS)])
            if cycle:
                return cycle


def update_flow(graph: 'Graph', cycle: list):
    delta_value = float("inf")

    for i in range(1, len(cycle)):

        this_id, delta_sign = cycle[i]
        if delta_sign is DeltaSign.PLUS:
            continue

        prev_id, _ = cycle[i - 1]
        this_node = graph.nodes[this_id]
        delta_value = min(delta_value, this_node.out_[prev_id]["flow"])

    for i in range(len(cycle)):

        this_id, delta_sign = cycle[i]
        prev_id, _ = cycle[i - 1]
        this_node = graph.nodes[this_id]

        if delta_sign is DeltaSign.PLUS:
            graph.increment_flow_safe(prev_id, this_id, delta_value)

        elif delta_sign is DeltaSign.MINUS:
            graph.increment_flow_safe(this_id, prev_id, - delta_value)

    for i in range(1, len(cycle)):

        this_id, delta_sign = cycle[i]
        prev_id, _ = cycle[i - 1]
        this_node = graph.nodes[this_id]

        if (delta_sign is DeltaSign.PLUS and
           this_node.in_[prev_id]["flow"] == 0):
            graph.set_flow(prev_id, this_id, None)
            break

        if (delta_sign is DeltaSign.MINUS and
           this_node.out_[prev_id]["flow"] == 0):
            graph.set_flow(this_id, prev_id, None)
            break


def solve(graph: 'Graph'):
    if not graph.is_balanced:
        raise SuppliesNotBalancedError()
    if graph.base_size != len(graph.nodes) - 1:
        raise WrongBaseSizeError()

    while True:

        reduced_costs = get_reduced_costs(graph)
        if reduce(lambda x, y: x and (y >= 0), reduced_costs.values(), True):
            break

        entering_edge = min(reduced_costs.keys(),
                            key=lambda x: reduced_costs[x])
        cycle = get_cycle(graph, entering_edge[0],
                          [(entering_edge[1], DeltaSign.PLUS)])
        update_flow(graph, cycle)
