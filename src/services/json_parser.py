import json
from io import TextIOWrapper
from typing import Any

import typer


class AdjacencyListJSONParser:
    """
    Parses a JSON file and validates that it contains a valid
    adjacency list.
    """

    def __init__(
        self,
        file: TextIOWrapper,
    ):
        """
        @param file:
            The path in filesystem to the JSON file.
        """
        self.file = file

    def parse(self) -> dict[str, set[str]]:
        """
        Loads a content from the provided file and validates that it
        is a valid adjacency list.

        @return:
            The dictionary of graph nodes.
        """
        file_content = self._load_file()
        return self._get_valid_adjacency_list(
            adjacency_list=file_content,
        )

    def _load_file(self):
        """
        Opens a json file and returns its content.

        @raise Exit:
            If the content isn't valid JSON file, raises an exception
            with status code 1.
        @return:
            The content of json file.
        """
        try:
            return json.load(self.file)
        except json.decoder.JSONDecodeError:
            print("The content of provided file isn't a valid JSON.")
            raise typer.Exit(
                code=1,
            )

    @staticmethod
    def _get_valid_adjacency_list(
        adjacency_list: Any,
    ) -> dict[str, set[str]]:
        """
        Validates that the adjacency list is a valid dictionary with valid
        node names.

        @param adjacency_list:
            The adjacency list to be validated.
        @raise Exit:
            1. If the adjacency list isn't a dictionary, raises an exception.
            2. If the key in the adjacency list isn't a string, raises an
            exception.
            3. If the value of adjacency list isn't a list, raises an exception.
            4. If the node name in the list isn't a string, raises an exception.
        @return:
            The dictionary with the valid adjacency list.
        """
        if not isinstance(adjacency_list, dict):
            print(
                f"The adjacency list must be described as an object, not '{type(adjacency_list).__name__}'."
            )
            raise typer.Exit(
                code=1,
            )
        absent_nodes = {}
        for key, value in adjacency_list.items():
            if not isinstance(key, str):
                print(
                    f"'{key}' is invalid key of adjacency list. It must be a string."
                )
                raise typer.Exit(
                    code=1,
                )
            if not isinstance(value, list):
                print(f"{value} is not a list.")
                raise typer.Exit(
                    code=1,
                )
            for node_name in value:
                if not isinstance(node_name, str):
                    print(f"The {value} is an invalid list of nodes. It must contain only strings.")
                    raise typer.Exit(
                        code=1,
                    )
                if node_name not in adjacency_list:
                    absent_nodes[node_name] = set()
        (valid_adjacency_list := {key: set(value) for key, value in adjacency_list.items()}).update(absent_nodes)
        return valid_adjacency_list
