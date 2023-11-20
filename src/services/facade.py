import networkx as nx
from matplotlib import pyplot as plt

from services.graph import Graph


class HardConnectedComponentsFacade:
    """
    Contains all logic for operations with a graph.
    """

    @staticmethod
    def visualize_graph(
        adjacency_list: dict[str, set[str]],
    ):
        """
        Visualizes a graph from the provided adjacency list and its strongly
        connected components.

        @param adjacency_list:
            The graph will be constructed from this adjacency list.
        """
        (visualize_graph := nx.DiGraph()).add_edges_from(
            ebunch_to_add=(graph := Graph(
                adjacency_list=adjacency_list,
            )).node_pairs,
        )
        nx.draw(
            G=visualize_graph,
            pos=(pos := nx.spring_layout(visualize_graph)),
            with_labels=True,
            arrows=True,
        )
        plt.show()
        node_to_component = {
            node: idx
            for idx, component in enumerate(graph.kosaraju())
            for node in component
        }
        nx.draw(
            visualize_graph,
            pos,
            node_color=[node_to_component[node] for node in visualize_graph.nodes()],
            with_labels=True,
            cmap=plt.cm.get_cmap('viridis'),
        )
        plt.show()
