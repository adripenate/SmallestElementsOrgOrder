import unittest


class SmallestElement:
    @classmethod
    def first_n_smallest(cls, elements, limit):
        return []


class FindPairsTest(unittest.TestCase):

    def test_should_skip_search(self):
        self.assertEqual([], SmallestElement.first_n_smallest([1, 2, 3, 4, 5], 0))

    def test_should_give_one_number(self):
        self.assertEqual([1], SmallestElement.first_n_smallest([1], 1))



if __name__ == '__main__':
    unittest.main()