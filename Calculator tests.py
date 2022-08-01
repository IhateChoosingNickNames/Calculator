import Calculator as cl

# Тесты через unittest

import unittest

class TestSmth(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(cl.main('5 + 5', 0), 10)
    
    def test_2(self):
        self.assertEqual(cl.main('15 + 14 // 2 + 4 ** (4 - 2) - 16', 0), 22)

    def test_3(self):
        self.assertEqual(cl.main('5! % 2 + 4', 0), 4)
    
    def test_4(self):
        self.assertEqual(cl.main('(5 * (2 + 2)) // 2', 0), 10)

    def test_5(self):
        self.assertEqual(cl.main('-(-5 + 4) ** 2 % 5', 0), -1)
    
    def test_5(self):
        self.assertEqual(cl.main('-(-5 + 4) ** (2 % (((5))))', 0), -1)

    # Тест на выпадение ошибки при некорретных данных
    #def test_exceptions_1(self):
        #with self.assertRaises(ValueError):
            #cl.is_valid('))(', 'sb')


#unittest.main()

# Тесты через pytest
def test_1():
    assert cl.main('5 + 5', 0) == 10
    
def test_2():
    assert cl.main('15 + 14 // 2 + 4 ** (4 - 2) - 16', 0) == 22

def test_3():
    assert cl.main('5! % 2 + 4', 0) == 4
    
def test_4():
    assert cl.main('(5 * (2 + 2)) // 2', 0) == 10

def test_5():
    assert cl.main('-(-5 + 4) ** 2 % 5', 0) == -1
    
def test_5():
    assert cl.main('-(-5 + 4) ** (2 % (((5))))', 0) == -1
    
test_1(), test_2(), test_3(), test_4(), test_5()

assert [1, 2, 3, 4] == [1, 2, 3]