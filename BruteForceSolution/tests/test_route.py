import unittest
from MapFactory import MapFactory
from route import *


class RouteTests(unittest.TestCase):
    def test_is_route_valid_t1(self):
        # Given
        the_map = MapFactory.create_map_from_file('../resources/map_2_pets.in')
        route_node_names = ['Cat', 'Dog', 'Cat_House', 'Dog_House']
        route = list(map(lambda x: the_map.get_node_by_name(x), route_node_names))

        # When
        result = is_route_valid(the_map, route, 2)

        # Then
        self.assertEqual(result, True)

    def test_is_route_valid_t2(self):
        # Given
        the_map = MapFactory.create_map_from_file('../resources/map_2_pets.in')
        route_node_names = ['Cat', 'Dog_House', 'Dog', 'Cat_House']
        route = list(map(lambda x: the_map.get_node_by_name(x), route_node_names))

        # When
        result = is_route_valid(the_map, route, 10)
        result = is_route_valid(the_map, route, 2)

        # Then
        self.assertEqual(result, False)

    def test_is_route_valid_t3(self):
        # Given
        the_map = MapFactory.create_map_from_file('../resources/map_3_pets.in')
        route_node_names = ['Cat', 'Dog', 'Hedgehog', 'Cat_House', 'Dog_House', 'Hedgehog_House']
        route = list(map(lambda x: the_map.get_node_by_name(x), route_node_names))

        # When
        result = is_route_valid(the_map, route, 2)

        # Then
        self.assertEqual(result, False)

    def test_is_route_valid_t4(self):
        # Given
        the_map = MapFactory.create_map_from_file('../resources/map_2_pets.in')
        route_node_names = ['Cat_House', 'Cat', 'Dog', 'Dog_House']
        route = list(map(lambda x: the_map.get_node_by_name(x), route_node_names))

        # When
        result = is_route_valid(the_map, route, 2)

        # Then
        self.assertEqual(result, False)

    def test_is_cargo_kept_under_limit_t1(self):
        # Given
        the_map = MapFactory.create_map_from_node_names(
            'Car',
            ['Cat', 'Dog'],
            ['Cat_House', 'Dog_House']
        )
        the_map = MapFactory.create_map_from_file('../resources/map_2_pets.in')
        route_node_names = ['Cat', 'Dog', 'Cat_House', 'Dog_House']
        route = list(map(lambda x: the_map.get_node_by_name(x), route_node_names))

        # When
        is_valid = is_cargo_kept_under_limit(the_map, route, 2)

        # Then
        self.assertEqual(is_valid, True)

    def test_is_cargo_kept_under_limit_t2(self):
        # Given
        the_map = MapFactory.create_map_from_file('../resources/map_3_pets.in')
        route_node_names = ['Cat', 'Dog', 'Hedgehog', 'Cat_House', 'Dog_House', 'Hedgehog_House']
        route = list(map(lambda x: the_map.get_node_by_name(x), route_node_names))

        # When
        is_valid = is_cargo_kept_under_limit(the_map, route, 2)

        # Then
        self.assertEqual(is_valid, False)

    def test_is_nodes_order_consecutive_t1(self):
        # Given
        the_map = MapFactory.create_map_from_file('../resources/map_2_pets.in')
        route_node_names = ['Cat', 'Dog', 'Cat_House', 'Dog_House']
        route = list(map(lambda x: the_map.get_node_by_name(x), route_node_names))

        # When
        is_valid = is_nodes_order_consecutive(the_map, route)

        # Then
        self.assertEqual(is_valid, True)

    def test_is_nodes_order_consecutive_t2(self):
        # Given
        the_map = MapFactory.create_map_from_file('../resources/map_2_pets.in')
        route_node_names = ['Cat', 'Dog_House', 'Dog', 'Cat_House']
        route = list(map(lambda x: the_map.get_node_by_name(x), route_node_names))

        # When
        is_valid = is_nodes_order_consecutive(the_map, route)

        # Then
        self.assertEqual(is_valid, False)

    def test_is_nodes_order_consecutive_t3(self):
        # Given
        the_map = MapFactory.create_map_from_file('../resources/map_2_pets.in')
        route_node_names = ['Cat_House', 'Cat', 'Dog', 'Dog_House']
        route = list(map(lambda x: the_map.get_node_by_name(x), route_node_names))

        # When
        is_valid = is_nodes_order_consecutive(the_map, route)

        # Then
        self.assertEqual(is_valid, False)

    def test_get_distance_for_route(self):
        # Given
        the_map = MapFactory.create_map_from_file('../resources/map_2_pets.in')
        route_node_names = ['Car', 'Cat', 'Dog', 'Cat_House', 'Dog_House']
        route = list(map(lambda x: the_map.get_node_by_name(x), route_node_names))

        # When
        distance = get_distance_for_route(route)

        # Then
        self.assertEqual(distance, 7)
