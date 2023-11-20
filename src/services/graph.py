class Graph:
    """
    The directed Graph data structure.
    """

    def __init__(
        self,
        adjacency_list: dict[str, set[str]] = None
    ):
        """
        @param adjacency_list:
            The dictionary that represents an adjacency list of the directed
            graph.
        """
        self.vertices = adjacency_list or {}

    def add_edge(
        self,
        from_node: str,
        to_node: str,
    ):
        """
        Adds a new node to the existing ones.

        @param from_node:
            From which node, a new one can be achieved.
        @param to_node:
            What node is added.
        """
        vertices = self.vertices.setdefault(from_node, set())
        vertices.add(to_node)
        self.vertices.setdefault(to_node, set())

    def transpose(self) -> 'Graph':
        """
        Transpose and returns a new graph.

        @return:
            The transposed graph.
        """
        transposed = Graph()
        for node in self.vertices:
            for connected_node in self.vertices[node]:
                transposed.add_edge(connected_node, node)
        return transposed

    def dfs(
        self,
        node: str,
        visited_nodes: list[str],
        visit_stack: list[str],
    ):
        """
        The Depth-first search algorithm for traversing the graph.

        @param node:
            The node from which the traversing is started.
        @param visited_nodes:
            The list of the already visited nodes.
        @param visit_stack:
            The order of which the traversing is executed.
        """
        visited_nodes.append(node)
        for connected_node in self.vertices[node]:
            if connected_node not in visited_nodes:
                self.dfs(
                    node=connected_node,
                    visited_nodes=visited_nodes,
                    visit_stack=visit_stack,
                )
        visit_stack.append(node)

    def kosaraju(self) -> list[list[str]]:
        """
        The Kosaraju algorithm for looking the strongly connected
        components of the graph.

        @return:
            The list with the strongly connected components.
        """
        visit_stack = []
        visited_nodes = []

        for node in self.vertices:
            if node not in visited_nodes:
                self.dfs(
                    node=node,
                    visited_nodes=visited_nodes,
                    visit_stack=visit_stack,
                )

        trans_graph = self.transpose()
        trans_graph_visited_nodes = []
        sccs = []

        for node in visit_stack[::-1]:
            if node not in trans_graph_visited_nodes:
                trans_graph.dfs(
                    node=node,
                    visited_nodes=trans_graph_visited_nodes,
                    visit_stack=(strongly_connected_components := []),
                )
                sccs.append(strongly_connected_components)

        return sccs

    @property
    def node_pairs(self) -> list[tuple[str, str]]:
        """
        The node pairs of the graph.

        @return:
            The pairs of the nodes.
        """
        return [
            (node, inner_node)
            for node, nodes_list in self.vertices.items()
            for inner_node in nodes_list
        ]
