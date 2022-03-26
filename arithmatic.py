import unittest

def Add(x,y):
    return x+y
def Add3num(x,y,z):
    return x+y+z
def Sub(x,y):
    return x-y
def Mul(x,y):
    return x*y
def Div(x,y):
    return x/y

class Myapp1(unittest.TestCase):
    def test_Add(self):
        a=12
        b=23
        c=Add(a,b)
        self.assertEqual(a+b,c)

class Myapp2(unittest.TestCase):
    def test_Add(self):
        a=12
        b=23
        c=5
        d=Add3num(a,b,c)
        self.assertEqual(a+b+c,d)

class Myapp3(unittest.TestCase):
    def test_Sub(self):
        a=23
        b=12
        c=Sub(a,b)
        self.assertEqual(a-b,c)

class Myapp4(unittest.TestCase):
    def test_Mul(self):
        a=12
        b=23
        c=Mul(a,b)
        self.assertEqual(a*b,c)

class Myapp5(unittest.TestCase):
    def test_Div(self):
        a=12
        b=2
        c=Div(a,b)
        self.assertEqual(a/b,c)

if __name__ == "__main__":
        unittest.main()