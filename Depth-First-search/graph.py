from __future__ import annotations
from collections import defaultdict
from typing import Any


class Graph:
    def __init__(self) -> None:
        self.edges = defaultdict(list)

    @staticmethod
    def read_file(file_name: str) -> Graph:
        with open(file_name, "r") as f:
            graph = Graph()
            for line in f:
                node_u, node_v = line.split()
                graph.add_edge(node_u, node_v)
        return graph

    def add_edge(self, node_u: Any, node_v: Any) -> None:
        self.edges[node_u].append(node_v)

    def non_recursive_dfs(self, start_node: Any) -> None:
        path = []
        stack = [start_node]
        visited = set()
        while stack:
            current_node = stack.pop()
            path.append(current_node)
            if current_node in visited:
                continue
            visited.add(current_node)
            for node in self.edges[current_node]:
                stack.append(node)
        print("Non recursive: ", end="")
        print(" -> ".join(path))

    def recursive_dfs(self, start_node: Any) -> None:
        path = []
        visited = set()
        self._recursive_dfs(start_node, visited, path)
        print("Recursive: ", end="")
        print(" -> ".join(path))

    def _recursive_dfs(
        self, current_node: Any, visited: set[Any], path: list[Any]
    ) -> None:
        visited.add(current_node)
        path.append(current_node)
        for node in self.edges[current_node]:
            if node not in visited:
                self._recursive_dfs(node, visited, path)
