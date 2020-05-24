from Map import Map
from Node import Node


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
        if cargo > car_capacity:    # Cargo Overflow
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
            return False            # Nodes order in route is not consecutive
    return True


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
