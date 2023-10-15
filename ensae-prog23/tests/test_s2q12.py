import sys 
sys.path.append("delivery_network")
import unittest 
from graph import Graph, graph_from_file, kruskal

class Test_Kruskal(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(kruskal(g).nb_edges, 9)

    def test_network3(self):
        g = graph_from_file("input/network.03.in")
        g2 = kruskal(g)
        self.assertEqual(g2.nb_edges, 3)
        self.assertEqual(g2.graph[4][0], (3, 4, 1))
        self.assertEqual(g2.graph[1][0], (2, 10, 1))
    
    def test_network4(self):
        g = graph_from_file("input/network.04.in")
        g2 = kruskal(g)
        self.assertEqual(g2.nb_edges, 3)
        self.assertEqual(g2.graph[1][0], (2, 4, 1))
        self.assertEqual(g2.graph[4][0], (3, 4, 1))

if __name__ == '__main__':
    unittest.main()