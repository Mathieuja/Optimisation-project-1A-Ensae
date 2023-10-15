import sys 
sys.path.append("delivery_network/")

import unittest 
from graph import camions_from_file

class Test_GraphLoading(unittest.TestCase):
    def test_network0(self):
        camions = camions_from_file("input/trucks.0.in")
        self.assertEqual(len(camions), 2)
        self.assertEqual(camions[0][0], 2000000)
        self.assertEqual(camions[1][1], 900000)

    def test_network1(self):
        camions = camions_from_file("input/trucks.1.in")
        self.assertEqual(len(camions), 20)
        self.assertEqual(camions[5][0], 3000000)
        self.assertEqual(camions[19][1], 2000000)
    
    def test_network2(self):
        camions = camions_from_file("input/trucks.2.in")
        self.assertEqual(len(camions), 10000)
        self.assertEqual(camions[313][1], 21940)
        self.assertEqual(camions[9999][0], 10000000)

if __name__ == '__main__':
    unittest.main()