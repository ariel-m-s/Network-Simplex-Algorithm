class GraphElementNotFoundError(KeyError):
    pass


class NodeNotFoundError(GraphElementNotFoundError):
    def __init__(self, node_id: str, *args, **kwargs):
        super().__init__(f"node '{node_id}' not found.",
                         *args, **kwargs)


class EdgeNotFoundError(GraphElementNotFoundError):
    def __init__(self, from_id: str, to_id: str, *args, **kwargs):
        super().__init__(f"edge '{from_id} -> {to_id}' not found.",
                         *args, **kwargs)


class GraphFileCorruptError(ValueError):
    pass


class DimensionsCorruptError(GraphFileCorruptError):
    def __init__(self, *args, **kwargs):
        super().__init__(f"can't load graph dimensions from corrupt file.",
                         *args, **kwargs)


class NodesCorruptError(GraphFileCorruptError):
    def __init__(self, *args, **kwargs):
        super().__init__(f"can't load graph nodes from corrupt file.",
                         *args, **kwargs)


class EdgesCorruptError(GraphFileCorruptError):
    def __init__(self, *args, **kwargs):
        super().__init__(f"can't load graph edges from corrupt file.",
                         *args, **kwargs)


class GraphPropertyError(Exception):
    pass


class SuppliesNotBalancedError(GraphPropertyError):
    def __init__(self, *args, **kwargs):
        super().__init__(f"the nodes' supplies are not balanced.",
                         *args, **kwargs)


class WrongBaseSizeError(GraphPropertyError):
    def __init__(self, *args, **kwargs):
        super().__init__(f"base must be of size N - 1.",
                         *args, **kwargs)


class NodeSupplyNotFulfilledError(GraphPropertyError):
    def __init__(self, node_id: int, *args, **kwargs):
        super().__init__(f"supply/demand at node '{node_id}' not fulfilled.",
                         *args, **kwargs)


class NegativeCycleError(GraphPropertyError):
    def __init__(self, *args, **kwargs):
        super().__init__(f"the problem is unbounded.",
                         *args, **kwargs)
