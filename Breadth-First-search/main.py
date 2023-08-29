from graph import Graph


def main() -> None:
    graph = Graph.read_file("edges.txt")
    graph.non_recursive_bfs("1")
    graph.recursive_bfs("1")


if __name__ == "__main__":
    main()
