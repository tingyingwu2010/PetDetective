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

        node_source.add_connection_to(node_destination, weight)
        node_destination.add_connection_to(node_source, weight)
    return graph, car_node, pet_nodes, house_nodes


def compute_path(path):
    """ Compute distance for path

    :param list of node path: list of nodes
    :return int: distance
    """
    current_node = path.pop(0)
    score = 0
    for node in path:
        score += current_node.get_distance_to(node)
        current_node = node
    return score


def is_route_valid(pet_nodes, house_nodes, route, car_capacity):
    """ Check if route is valid and return the boolean result.
    There are 2 conditions for a route to be valid:
    - no cargo overflow - car capacity is not exceeded
    - nodes order are consecutive - a pet node is traversed before pet's house node

    :param pet_nodes:
    :param house_nodes:
    :param route:
    :param car_capacity:
    :return:
    """
    cargo = 0
    for node in route:
        if node in pet_nodes:
            cargo += 1
        if node in house_nodes:
            cargo -= 1
        if cargo > car_capacity:    # Cargo Overflow
            return False
        if cargo < 0:               # Route is not consecutive
            return False
    return True


def find_shortest_route_for_capacitated_car(graph, car_node, car_capacity, pet_nodes, house_nodes):
    """ Find shortest route to deliver all the pets and return the distance and the route.

    :param Graph graph: graph
    :param Node car_node: car node
    :param int car_capacity: car capacity
    :param list of Node pet_nodes: pet nodes
    :param list of Node house_nodes: house nodes

    :return int, list of Node: distance, route
    """
    import itertools
    permutations = list(itertools.permutations(graph.nodes[1:]))

    all_distances = {}
    for perm in permutations:
        route = list(perm)
        if not is_route_valid(pet_nodes, house_nodes, route, car_capacity):
            continue

        route.insert(0, car_node)
        distance = compute_path(route)
        all_distances[distance] = route
    min_distance = min(all_distances.keys())
    return min_distance, all_distances[min_distance]


if __name__ == '__main__':
    graph, car, pets, houses = load_graph('resources/map_5_pets.in')
    distance, route = find_shortest_route_for_capacitated_car(graph, car, 4, pets, houses)
    print("The shortest route is {}, with a distance of {}.".format(route, distance))
