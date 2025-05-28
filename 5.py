import unittest
from two import f4, f5

class TestMyFunctions(unittest.TestCase):

    def test_f4_even(self):
        result = f4([2, 4, 1, 3])
        self.assertEqual(result, True)

    def test_f4_odd(self):
        result = f4([1, 5, 2, 0])
        self.assertEqual(result, False)

    def test_f5_1(self):
        result = f5(1)
        self.assertEqual(result, True)

    def test_f5_0(self):
        result = f5(0)
        self.assertEqual(result, True)

    def test_f5_not1_not0(self):
        result = f5(5000)
        self.assertEqual(result, False) #будет ошибка, так как условие в f5 всегда выполняется

if __name__ == '__main__':
    unittest.main()
