from Map import Map
from Node import Node


class MapFactory:
    @staticmethod
    def create_map_from_file(filepath):
        """Create map from file.

        Parameters:
            filepath (str): file path to load the map from

        Returns:
            Map: map
        """
        from utilities import FileUtilities
        file_content = FileUtilities.get_sanitized_content_from_file(filepath)

        car_node_name = file_content.pop(0)
        pet_nodes_name = file_content.pop(0).split(" ")
        house_nodes_names = file_content.pop(0).split(" ")
        m = MapFactory.create_map_from_node_names(car_node_name, pet_nodes_name, house_nodes_names)

        while file_content:
            conn_repr = file_content.pop(0).split(" ")

            node_source = m.get_node_by_name(conn_repr[0])
            node_destination = m.get_node_by_name(conn_repr[1])
            distance = int(conn_repr[2])

            node_source.add_connection_to(node_destination, distance)
            node_destination.add_connection_to(node_source, distance)

        return m

    @staticmethod
    def create_map_from_node_names(car_node_name, pet_node_names, house_node_names):
        """Create map from node names.

        Parameters:
            car_node_name (str): car node's name
            pet_node_names (list of str): the list of pet's node names
            house_node_names (list of str): the list of house's node names

        Returns:
            Map: map
        """
        node_names = list(car_node_name)
        node_names.extend(pet_node_names)
        node_names.extend(house_node_names)
        nodes = list(map(lambda x: Node(x), node_names))

        m = Map(nodes)
        m.car_node = m.get_node_by_name(car_node_name)
        m.pet_nodes = list(map(lambda x: m.get_node_by_name(x), pet_node_names))
        m.house_nodes = list(map(lambda x: m.get_node_by_name(x), house_node_names))

        return m
