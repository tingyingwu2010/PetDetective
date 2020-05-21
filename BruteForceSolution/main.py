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


def compute_path(path):
    """ Compute distance for path

    :param list of node path: list of nodes
    :return int: distance
    """
    current_node = path.pop(0)
    score = 0
    for node in path:
        score += current_node.get_weight(node)
        current_node = node
    return score


def find_shortest_route(graph, car_node, pet_nodes, house_nodes):
    """ Find shortest route to deliver all the pets and return the distance and the route.

    :param Graph graph: graph
    :param Node car_node: car node
    :param list of Node pet_nodes: pet nodes
    :param list of Node house_nodes: house nodes

    :return int, list of Node: distance, route
    """
    import itertools

    nodes_names = list(map(lambda x: x.name, graph.nodes))
    permutations = list(itertools.permutations(nodes_names[1:]))

    all_distances = {}
    for perm in permutations:
        irregular_perm = False
        for index in range(0, len(pet_nodes)):
            p_node = pet_nodes[index]
            h_node = house_nodes[index]
            if perm.index(p_node.name) > perm.index(h_node.name):
                irregular_perm = True
                break
        if irregular_perm:
            continue

        path = list(map(lambda x: graph.get_node(x), perm))
        path.insert(0, car_node)
        distance = compute_path(path)
        all_distances[distance] = path
    min_distance = min(all_distances.keys())
    return min_distance, all_distances[min_distance]


if __name__ == '__main__':
    graph, car, pets, houses = load_graph('resources/graph_3_pets.in')
    distance, route = find_shortest_route(graph, car, pets, houses)
    print("The shortest route is {}, with a distance of {}.".format(route, distance))
