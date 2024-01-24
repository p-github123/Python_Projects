#I am using GIT Hub
import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_my_stuff(self):
        test_param = 10
        result = main.do_my_stuff(test_param)
        self.assertEqual(result, 80)

    def test_do_my_stuff2(self):
        test_param = 'jjjjjjj'
        result = main.do_my_stuff(test_param)
        #self.assertEqual(result, ValueError)
        #self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)

    def test_do_my_stuff3(self):
        test_param = None
        result = main.do_my_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')
        #self.assertTrue(isinstance(result, ValueError))
        #self.assertIsInstance(result, ValueError)
    def test_do_my_stuff4(self):
        test_param = ''
        result = main.do_my_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')
    def test_do_my_stuff5(self):
        test_param = 0
        result = main.do_my_stuff(test_param)
        self.assertEqual(result, 'the answer is 0')

if __name__ == '__main__':
    unittest.main()
