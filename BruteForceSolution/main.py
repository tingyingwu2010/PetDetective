from Graph import Graph
from Node import Node


def load_graph(filepath):
    """ Load graph from file and returns the graph and its nodes.

    :param str filepath: file path
    :return graph, node, list of node, list of node: graph, car node, list of pet nodes, list of house nodes
    """
    from utilities import FileUtilities
    file_content = FileUtilities.get_sanitized_content_from_file(filepath)

    all_nodes_name = file_content.pop(0).split(" ")
    all_nodes = list(map(lambda x: Node(x), all_nodes_name))
    graph = Graph(all_nodes)

    car_node_name = file_content.pop(0)
    car_node = graph.get_node(car_node_name)
    pet_nodes_name = file_content.pop(0).split(" ")
    pet_nodes = list(map(lambda x: graph.get_node(x), pet_nodes_name))
    house_nodes_names = file_content.pop(0).split(" ")
    house_nodes = list(map(lambda x: graph.get_node(x), house_nodes_names))

    while file_content:
        edge_repr = file_content.pop(0).split(" ")
        node_source = graph.get_node(edge_repr[0])
        node_destination = graph.get_node(edge_repr[1])
        weight = int(edge_repr[2])

        node_source.add_connection(node_destination, weight)
        node_destination.add_connection(node_source, weight)
    return graph, car_node, pet_nodes, house_nodes


if __name__ == '__main__':
    graph, car, pets, houses = load_graph('resources/graph.in')
    print(graph, car, pets, houses)
