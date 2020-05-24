class Map:
    def __init__(self, nodes):
        self.nodes = nodes

    def get_node(self, name):
        """ Returns a node by name.

        :param str name: node name
        :return Node: node
        """
        for n in self.nodes:
            if n.name == name:
                return n
