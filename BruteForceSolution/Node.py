class Node:
    def __init__(self, name):
        self.name = name
        self.connections = {}

    def add_connection(self, node, weight):
        self.connections[node] = weight

    def __repr__(self):
        return self.name
