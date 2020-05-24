from MapFactory import MapFactory
from Map import Map
from Node import Node
from route import *


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
