from MapFactory import MapFactory
from Map import Map
from Node import Node


def get_distance_for_route(route):
    """Compute distance for route

    Parameters:
        route (list of Node): a list of nodes representing the route

    Returns:
        int: the distance of the route
    """
    current_node = route.pop(0)
    d = 0
    for n in route:
        d += current_node.get_distance_to(n)
        current_node = n
    return d


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


def find_shortest_route_for_capacitated_car(the_map, car_capacity):
    """Find shortest route to deliver all the pets and return the distance and the route.

    Parameters:
        the_map (Map): the map
        car_capacity (int): the cargo capacity of the car

    Returns:
        int: the shortest route distance
        list of nodes: the shortest route
    """
    import itertools
    permutations = list(itertools.permutations(the_map.nodes[1:]))

    all_distances = {}
    for perm in permutations:
        route = list(perm)
        if not is_route_valid(the_map.pet_nodes, the_map.house_nodes, route, car_capacity):
            continue

        route.insert(0, the_map.car_node)
        distance = get_distance_for_route(route)
        all_distances[distance] = route
    min_distance = min(all_distances.keys())
    return min_distance, all_distances[min_distance]


if __name__ == '__main__':
    m = MapFactory.create_map_from_file('resources/map_3_pets.in')
    dist, r = find_shortest_route_for_capacitated_car(m, 4)
    print("The shortest route is {}, with a distance of {}.".format(r, dist))
