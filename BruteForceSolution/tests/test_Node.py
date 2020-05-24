import unittest
from Node import Node


class NodeTests(unittest.TestCase):
    def test_node_creation(self):
        # Given
        node_name = "A"

        # When
        node = Node(node_name)

        # Then
        self.assertEqual(node.name, node_name)

    def test_node_repr(self):
        # Given
        node_name = "A"
        node = Node(node_name)

        # When
        node_repr = "{}".format(node)

        # Then
        self.assertEqual(node_repr, node_name)

    def test_add_connection_to(self):
        # Given
        node1 = Node("A")
        node2 = Node("B")
        distance_node1_node2 = 3

        # When
        node1.add_connection_to(node2, distance_node1_node2)

        # Then
        self.assertEqual(node1.connections, {node2.name: distance_node1_node2})

    def test_get_distance_to(self):
        # Given
        node1 = Node("A")
        node2 = Node("B")
        distance_node1_node2 = 3
        node1.add_connection_to(node2, distance_node1_node2)

        # When
        distance = node1.get_distance_to(node2)

        # Then
        self.assertEqual(distance, distance_node1_node2)
