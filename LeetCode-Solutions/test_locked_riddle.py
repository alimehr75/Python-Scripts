import unittest 
from locked_riddle import check_nums

class Test_locked_riddle(unittest.TestCase):

    def test1(self):
        """two character in common , But not in write places"""
        self.assertEquals(check_nums("123","142"),(1,1),"it should be (1,1)")
    def test2(self):
        """one character in common"""
        self.assertEquals(check_nums("123","146"),(1,0),"it should be (1,0)")
    def test3(self):
        """Three character in common and in same places"""
        self.assertEquals(check_nums("456","456"),(3,0),"it should be (3,0)")
        

if __name__ == "__main__":
    unittest.main()
