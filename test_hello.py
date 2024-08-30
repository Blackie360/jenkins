import unittest
from hello import greet

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("jack"), "Hello, jack!")
        self.assertEqual(greet("world"), "Hello, world!")
        self.assertNotEqual(greet("jack"), "Hello, world!")

if __name__ == "__main__":
    unittest.main()
