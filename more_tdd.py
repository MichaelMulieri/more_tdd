import unittest

def reversedList(someList):
    for i in range(len(someList)// 2):
        someList[i], someList[-i-1] = someList[-i-1], someList[i] 
    return someList

"""print(reversedList([1,2,3,4,5,6,7]))"""

def isPalindrome(word):
    for i in range(0, int(len(word)//2)):
        if word[i] != word[len(word)-i-1]:
            return False
        return True

"""print(isPalindrome('racecar'))
print(isPalindrome('cat'))"""

def coins(num):
    coinTypes = {'quarters': 0, 
                'dimes': 0, 
                'nickels': 0, 
                'pennies': 0
            }
    coinTypes['quarters'] = num // 25
    num = num - (coinTypes['quarters'] * 25)
    coinTypes['dimes'] = num // 10
    num = num - (coinTypes['dimes'] * 10)
    coinTypes['nickels'] = num // 5
    num = num - (coinTypes['nickels'] * 5 )
    coinTypes['pennies'] = num // 1

    print(f'Your change is {coinTypes}')

coins(87)
coins(90)
coins(55)
coins(99)
        
def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)


print(factorial(5))   
print(factorial(8))


class reverseListTest(unittest.TestCase):
    def testListOne(self):
        self.assertEqual(reversedList([1,3,5]), [5,3,1])

    def testListTwo(self):
        self.assertEqual(reversedList([5,7,8,9,1]), [1,9,8,7,5])

    def testListThree(self):
        self.assertEqual(reversedList([100,76,34,56,890,3]), [3,890,56,34,76,100])

class isPalindromeTest(unittest.TestCase):
    def testWordOne(self):
        self.assertEqual(isPalindrome('racecar'), True)

    def testWordTwo(self):
        self.assertEqual(isPalindrome('lionoil'), True)

    def testWordThree(self):
        self.assertNotEqual(isPalindrome('rabcr'), False)

class coinsTest(unittest.TestCase):
    def coinsTestOne(self):
        self.assertEqual(coins(87), {'quarters': 3, 'dimes': 1, 'nickels': 0, 'pennies': 2})

    def coinsTestTwo(self):
        self.assertDictEqual(coins(90), {'quarters': 3, 'dimes': 1, 'nickels': 1, 'pennies': 0})

class factorialTest(unittest.TestCase):
    def factorialTestOne(self):
        self.assertEqual(factorial(5), 120)

    def factorialTestTwo(self):
        self.assertNotEqual(factorial(8), 40000)

if __name__ == "__main__":
    unittest.main()