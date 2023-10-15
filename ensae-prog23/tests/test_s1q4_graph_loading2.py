# À compléter
import sys 
sys.path.append("delivery_network")

import unittest

from graph import Graph, graph_from_file



class Test_Reachability(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.min_power(1, 4), ([1, 2, 3, 4], 11))
        self.assertEqual(g.min_power(1, 7), ([1, 2, 5, 7], 14))

    def test_network2(self):
        g = graph_from_file("input/network.02.in")
        self.assertEqual(g.min_power(1, 2), ([1, 4, 3, 2], 4))
        self.assertEqual(g.min_power(3, 4), ([3, 4], 4))

    def test_network4(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.min_power(1, 3), ([1, 2, 3], 4))
        self.assertEqual(g.min_power(1, 4), ([1, 2, 3, 4], 4))
        self.assertEqual(g.min_power(1, 7), ([], float("inf")))

if __name__ == '__main__':
    unittest.main()