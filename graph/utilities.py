from graph.exceptions import NodeNotFoundError


def verify_node_existance(function: callable):
    def wrapper(graph: 'Graph', from_id: int, to_id: int, *args, **kwargs):
        if from_id not in graph.nodes.keys():
            raise NodeNotFoundError(from_id)
        if to_id not in graph.nodes.keys():
            raise NodeNotFoundError(to_id)
        return function(graph, from_id, to_id, *args, **kwargs)
    return wrapper
