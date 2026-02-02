import unittest
from Calculator_prjt import addition, subtraction, multiplication, division
class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(10,2),12)
    def test_subtraction(self):
        self.assertEqual(subtraction(10,2),8)
    def test_multiplication(self):
        self.assertEqual(multiplication(10,2),20)
    def test_division(self):
        self.assertEqual(division(10,2),5)
    def test_division_by_zero(self):
        self.assertEqual(division(10,0),"Division by zero is not valid,try with non zero number!")
if __name__=="__main__":
    unittest.main()  
