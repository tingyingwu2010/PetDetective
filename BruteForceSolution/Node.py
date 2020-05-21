class Node:
    def __init__(self, name):
        self.name = name
        self.connections = {}

    def add_connection(self, node, distance):
        self.connections[node] = distance

    def get_distance_to(self, node):
        return self.connections[node]

    def __repr__(self):
        return self.name
