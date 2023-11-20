from typing import Annotated

import typer
from typer import Option, FileText

from services.facade import HardConnectedComponentsFacade
from services.json_parser import AdjacencyListJSONParser


def main(
    adjacency_file: Annotated[FileText, Option(
        help="The JSON file that contains an adjacency list.",
        exists=True,
        mode='r',
    )],
):
    """
    Constructs a graph, visualize it and its strongly connected components.
    """
    HardConnectedComponentsFacade().visualize_graph(
        adjacency_list=AdjacencyListJSONParser(file=adjacency_file).parse(),
    )


if __name__ == '__main__':
    typer.run(main)
