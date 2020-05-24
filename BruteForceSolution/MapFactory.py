from Map import Map
from Node import Node


class MapFactory:
    @staticmethod
    def create_map_from_file(filepath):
        """Create map from file.

        Args:
            filepath (str): file path to load the map from

        Returns:
            Map: map
        """
        from utilities import FileUtilities
        file_content = FileUtilities.get_sanitized_content_from_file(filepath)

        all_nodes_name = file_content.pop(0).split(" ")
        all_nodes = list(map(lambda x: Node(x), all_nodes_name))
        m = Map(all_nodes)

        car_node_name = file_content.pop(0)
        m.car_node = m.get_node_by_name(car_node_name)
        pet_nodes_name = file_content.pop(0).split(" ")
        m.pet_nodes = list(map(lambda x: m.get_node_by_name(x), pet_nodes_name))
        house_nodes_names = file_content.pop(0).split(" ")
        m.house_nodes = list(map(lambda x: m.get_node_by_name(x), house_nodes_names))

        while file_content:
            conn_repr = file_content.pop(0).split(" ")

            node_source = m.get_node_by_name(conn_repr[0])
            node_destination = m.get_node_by_name(conn_repr[1])
            distance = int(conn_repr[2])

            node_source.add_connection_to(node_destination, distance)
            node_destination.add_connection_to(node_source, distance)

        return m
