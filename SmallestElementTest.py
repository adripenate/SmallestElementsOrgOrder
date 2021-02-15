import unittest
from SmallestElement import first_n_smallest


class FindPairsTest(unittest.TestCase):

    def test_should_skip_search(self):
        self.assertEqual([], first_n_smallest([1, 2, 3, 4, 5], 0))

    def test_should_give_one_number(self):
        self.assertEqual([1], first_n_smallest([1], 1))

    def test_should_give_first_number(self):
        self.assertEqual([1], first_n_smallest([1, 2], 1))

    def test_should_find_second_number(self):
        self.assertEqual([1], first_n_smallest([2, 1], 1))

    def test_should_give_two_numbers(self):
        self.assertEqual([1, 1], first_n_smallest([1, 1, 1, 1], 2))

    def test_should_give_smallest_numbers(self):
        self.assertEqual([1, 1], first_n_smallest([4, 1, 2, 1], 2))


if __name__ == '__main__':
    unittest.main()