from calculadora import Calculator
import unittest

a = 'sus'
b = 'sus'
c = [1,2]
d = [1,2]
x = 1.0
y = 1.8

class Test(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_soma(self):
        self.assertEqual(self.calc.add(2,2),4)

    def test_not_soma(self):
        self.assertNotEqual(self.calc.add(4,5),10)
    
    @unittest.expectedFailure
    def test_divisao(self):
        self.assertEqual(self.calc.division(2,0), 0)
    
    def test_string(self):
        self.assertMultiLineEqual(a,b)

    def test_lista(self):
        self.assertListEqual(c,d)

    def test_almost_equal(self):
        self.assertNotAlmostEqual(y-x,7)

if __name__ == '__main__':
    unittest.main()