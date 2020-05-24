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


def is_route_valid(the_map, route, car_capacity):
    """Check if route is valid and return the boolean result.
    There are 2 conditions for a route to be valid:
    - no cargo overflow - car capacity should not be exceeded
    - route nodes order consecutivity is valid - a pet node should be traversed before pet's house node

    Parameters:
        the_map (Map): the map that holds the route
        route (list of Node): a list of nodes representing the route
        car_capacity (int): the cargo capacity of the car

    Returns:
        True if the route is valid, False if the route is invalid
    """
    return is_cargo_kept_under_limit(the_map, route, car_capacity) and is_nodes_order_consecutive(the_map, route)


def is_cargo_kept_under_limit(the_map, route, car_capacity):
    """Check if cargo is kept under limit on route.

    Parameters:
        the_map (Map): the map that holds the route
        route (list of Node): a list of nodes representing the route
        car_capacity (int): the cargo capacity of the car

    Returns:
        True if cargo is kept under limit, False if not
    """
    cargo = 0
    for node in route:
        if node in the_map.pet_nodes:
            cargo += 1
        if node in the_map.house_nodes:
            cargo -= 1
        if cargo > car_capacity:  # Cargo Overflow
            return False
    return True


def is_nodes_order_consecutive(the_map, route):
    """Check if nodes order is consecutive.
    The order is consecutive if every pet node is traversed before it's house node.

    Parameters:
        the_map (Map): the map that holds the route
        route (list of Node): a list of nodes representing the route

    Returns:
        True if the nodes order is consecutive, False if not
    """
    for index in range(0, len(the_map.pet_nodes)):
        p_node = the_map.pet_nodes[index]
        h_node = the_map.house_nodes[index]
        if route.index(p_node) > route.index(h_node):
            return False  # Nodes order in route is not consecutive
    return True


def find_shortest_route_for_capacitated_car(the_map, car_capacity):
    """Find shortest route to deliver all the pets and return the distance and the route.
    The method is optimized to use only half of the permutations.
    Routes that start with a pet's house are not valid. The second half of the permutations start with a pet's house.

    Parameters:
        the_map (Map): the map
        car_capacity (int): the cargo capacity of the car

    Returns:
        int: the shortest route distance
        list of nodes: the shortest route
    """
    import itertools
    from math import factorial
    perm_limit = int(factorial(len(the_map.pet_nodes) * 2) / 2)     # We don't need all the permutations, cut in half
    permutations = list(itertools.islice(itertools.permutations(the_map.nodes[1:]), perm_limit))

    all_distances = {}
    for perm in permutations:
        route = list(perm)
        if not is_route_valid(the_map, route, car_capacity):
            continue

        route.insert(0, the_map.car_node)
        distance = get_distance_for_route(route)
        all_distances[distance] = route

    min_distance = min(all_distances.keys())
    return min_distance, all_distances[min_distance]


if __name__ == '__main__':
    m = MapFactory.create_map_from_file('resources/map_5_pets.in')
    dist, r = find_shortest_route_for_capacitated_car(m, 4)
    print("The shortest route is {}, with a distance of {}.".format(r, dist))
