import unittest

class check_info(unittest.TestCase):

    def test_normal(self):
       print("test passed")
    def tearDown(self):
        print("some text")
if __name__=='__main__':
    unittest.main()
