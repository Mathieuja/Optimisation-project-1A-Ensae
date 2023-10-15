import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_Reachability(unittest.TestCase):
    def test_network03(self):
        g = graph_from_file("input/network.03.in")
        self.assertEqual(g.get_path_with_powerbonus(1, 4, 11), [1, 4])
        self.assertEqual(g.get_path_with_powerbonus(1, 4, 9), None)
        self.assertEqual(g.get_path_with_powerbonus(1, 4, 10), [1, 2, 3, 4])

    def test_network04(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.get_path_with_powerbonus(1, 2, 11), [1, 4, 3, 2])
        self.assertEqual(g.get_path_with_powerbonus(1, 2, 5), [1, 2])

if __name__ == '__main__':
    unittest.main()