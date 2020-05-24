from Node import Node


class Map:
    def __init__(self, nodes):
        """Initialize a Map.

        Parameters:
            nodes (list of Node): the list of nodes to initialize the map with
        """
        self.nodes = nodes
        self.car_node = None
        self.pet_nodes = []
        self.house_nodes = []

    def get_node_by_name(self, name):
        """Return a node by name.

        Parameters:
            name (str): node name

        Returns:
             Node: node
        """
        for n in self.nodes:
            if n.name == name:
                return n
