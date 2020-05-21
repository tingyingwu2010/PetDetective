def print_welcome_message():
    print("In order to build the graph, you will have to enter the nodes and the distance between them.")
    print("You will have to enter only the pets. The `Car` and the houses will be added by default.")
    print("All the names must be unique and spaces are prohibited.")
    print()


def read_graph_info():
    """ Reads information about the graph and returns the data structures related to it.

    :return (list of str, list of str, list of str, list of tuple of str): nodes list, pets list, houses list, edges with weight.
    """
    pets_input = input("Enter the pets separated by spaces: ")
    pets = pets_input.split(' ')
    houses = list(map(lambda x: x+'_House', pets))

    nodes = ['Car']
    nodes.extend(pets)
    nodes.extend(houses)

    edges = []
    for i in range(0, len(nodes)):
        for j in range(i + 1, len(nodes)):
            if i == j:
                continue
            w = input("Enter the distance between the {} and the {}: ".format(nodes[i], nodes[j]))
            e = (nodes[i], nodes[j], w)
            edges.append(e)
    return nodes, pets, houses, edges


def print_structure_instructions():
    print("***********************************************")
    print("Graph Structure below. Copy the following data in the `graph.in` file.")


def print_structure(nodes, pets, houses, edges):
    """ Prints the graph structure.

    :param list of str nodes: list of nodes
    :param list of str pets: list of pets
    :param list of str houses: list of houses
    :param list of tuple of str edges: list of edges with the weight
    """
    print(" ".join(nodes))
    print(nodes[0])
    print(" ".join(pets))
    print(" ".join(houses))

    edges_repr = []
    for e in edges:
        edges_repr.append(" ".join(e))
    print("\n".join(edges_repr))


if __name__ == "__main__":
    print_welcome_message()
    nodes, pets, houses, edges = read_graph_info()
    print_structure_instructions()
    print_structure(nodes, pets, houses, edges)
