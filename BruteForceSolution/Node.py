class Node:
    """Represent a node on the map

    Attributes:
        name (str): the name of the node
        connections (dict of Node:int): dictionary for connections with other nodes and the distance to them
    """

    def __init__(self, name):
        """Initialize a Node.

        Parameters:
            name (str): the name of the node
        """
        self.name = name
        self.connections = {}

    def __repr__(self):
        return self.name

    def add_connection_to(self, node, distance):
        """Add connection to another node.

        Parameters:
            node (Node): the node to be connected to
            distance (int): the distance to the node
        """
        self.connections[node.name] = distance

    def get_distance_to(self, node):
        """Get distance to node.

        Parameters:
            node (Node): the node to get the distance to

        Returns:
            int: distance to the node
        """
        return self.connections[node.name]
