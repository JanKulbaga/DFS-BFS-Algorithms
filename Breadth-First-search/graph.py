from __future__ import annotations
from collections import defaultdict
from typing import Any
from queue import Queue


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

    def non_recursive_bfs(self, start_node: Any) -> None:
        path = []
        queue = Queue()
        queue.put(start_node)
        visited = set()
        while not queue.empty():
            current_node = queue.get()
            path.append(current_node)
            if current_node in visited:
                continue
            visited.add(current_node)
            for node in self.edges[current_node]:
                queue.put(node)
        print("Non recursive: ", end="")
        print(" -> ".join(path))

    def recursive_bfs(self, start_node: Any) -> None:
        path = []
        visited = set()
        queue = Queue()
        queue.put(start_node)
        self._recursive_bfs(queue, visited, path)
        print("Recursive: ", end="")
        print(" -> ".join(path))

    def _recursive_bfs(
        self, queue: Queue[Any], visited: set[Any], path: list[Any]
    ) -> None:
        if queue.empty():
            return
        current_node = queue.get()
        path.append(current_node)
        visited.add(current_node)
        for node in self.edges[current_node]:
            if node not in visited:
                queue.put(node)    
        self._recursive_bfs(queue, visited, path)
