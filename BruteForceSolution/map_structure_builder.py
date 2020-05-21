def print_welcome_message():
    print("In order to build the map, you will have to enter the nodes and the distance between them.")
    print("For nodes, you will have to enter only the pets. The `Car` and the houses will be added by default.")
    print("All the names must be unique and spaces are prohibited.")
    print()


def fetch_map_information():
    """Fetch information about the map and return the map data representation.

    Map data representation:
    {
        nodes (list of str): list of all nodes
        car (str): name of car node
        pets (list of str): list of pet nodes
        houses (list of str): list of house nodes
        connections (list of tuple of str): list of connections between nodes in the format (node node distance)
    }

    Returns:
        dict: map data representation
    """
    map_data = {
        'nodes': None,
        'car': None,
        'pets': None,
        'house': None,
        'connections': None
    }

    pets_input = input("Enter the pets separated by spaces: ")
    pets = pets_input.split(' ')
    map_data['pets'] = pets

    houses = list(map(lambda x: x+'_House', pets))
    map_data['houses'] = houses

    nodes = ['Car']
    map_data['car'] = 'Car'

    nodes.extend(pets)
    nodes.extend(houses)
    map_data['nodes'] = nodes

    connections = []
    for i in range(0, len(nodes)):
        for j in range(i + 1, len(nodes)):
            if i == j:
                continue
            w = input("Enter the distance between the {} and the {}: ".format(nodes[i], nodes[j]))
            conn = (nodes[i], nodes[j], w)
            connections.append(conn)
    map_data['connections'] = connections

    return map_data


def print_map_structure(map_data):
    """Print map structure

    Args:
        map_data (dict): map data representation
    """
    print("***********************************************")
    print("Map structure below. Copy the following data in the `map.in` file.")
    print(" ".join(map_data['nodes']))
    print(map_data['car'])
    print(" ".join(map_data['pets']))
    print(" ".join(map_data['houses']))

    connections = map_data['connections']
    connections_repr = []
    for conn in connections:
        connections_repr.append(" ".join(conn))
    print("\n".join(connections_repr))


if __name__ == "__main__":
    print_welcome_message()
    data = fetch_map_information()
    print_map_structure(data)
