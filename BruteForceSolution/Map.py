from Node import Node


class Map:
    def __init__(self, nodes):
        self.nodes = nodes

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
