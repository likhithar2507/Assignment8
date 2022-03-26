import unittest

def check_even_odd(x):
    if x%2==0:
        return "even"
    else:
        return "odd"

def Divisible_or_not(x):
    if x%7==0:
        return True
    else:
        return False

def Prime_or_not(x):
    flag = False

    if x> 1:
        for i in range(2,x):
            if (x% i) == 0:
                flag = True
                break
    if flag:
        return True
    else:
        return False

class My_Even_or_odd_app(unittest.TestCase):
    def test_case_even(self):
        result = check_even_odd(2)
        self.assertEqual("even",result)

    def test_case_odd(self):
        result = check_even_odd(5)
        self.assertNotEqual("even",result)

class CheckDivisible(unittest.TestCase):
    def test_Divisible(self):
        result=Divisible_or_not(14)
        self.assertTrue(result)

    def test_Divisible1(self):
        result=Divisible_or_not(13)
        self.assertFalse(result)

class CheckPrimeNumber(unittest.TestCase):
    def test_prime(self):
        result=Prime_or_not(3)
        self.assertTrue(True)

    def test_prime_not(self):
        result=Prime_or_not(10)
        self.assertFalse(False)

if __name__ == "__main__":
        unittest.main()