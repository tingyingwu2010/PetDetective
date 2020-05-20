def read_input():
    nodes_input = input("Enter the nodes: ")
    nodes = nodes_input.split(' ')

    edges = []
    for i in range(0, len(nodes)):
        for j in range(i + 1, len(nodes)):
            if i == j:
                continue
            w = input("Enter weight between {} and {}: ".format(nodes[i], nodes[j]))
            e = (nodes[i], nodes[j], w)
            edges.append(e)
    return nodes, edges


def print_structure(nodes, edges):
    print("Graph Structure:")
    print(" ".join(nodes))

    edges_repr = []
    for e in edges:
        edges_repr.append(" ".join(e))
    print("\n".join(edges_repr))


def build_graph_structure():
    nodes, edges = read_input()
    print_structure(nodes, edges)


if __name__ == "__main__":
    build_graph_structure()
