import unittest
from main import is_route_valid
from MapFactory import MapFactory


class RouteTests(unittest.TestCase):
    def test_is_route_valid(self):
        # Given
        the_map = MapFactory.create_map_from_node_names(
            'Car',
            ['Cat', 'Dog'],
            ['Cat_House', 'Dog_House']
        )

        route_node_names = ['Cat', 'Dog_House', 'Dog', 'Cat_House']
        route = list(map(lambda x: the_map.get_node_by_name(x), route_node_names))

        # When
        result = is_route_valid(the_map, route, 10)

        # Then
        self.assertEqual(result, False)

