import unittest


class SmallestElement:
    @classmethod
    def first_n_smallest(cls, elements, limit):
        if limit == 0:
            return []
        smallest_elements = []
        for element in elements:
            if element <= limit:
                smallest_elements.append(element)
        return smallest_elements


class FindPairsTest(unittest.TestCase):

    def test_should_skip_search(self):
        self.assertEqual([], SmallestElement.first_n_smallest([1, 2, 3, 4, 5], 0))

    def test_should_give_one_number(self):
        self.assertEqual([1], SmallestElement.first_n_smallest([1], 1))

    def test_should_give_first_number(self):
        self.assertEqual([1], SmallestElement.first_n_smallest([1, 2], 1))

    def test_should_find_second_number(self):
        self.assertEqual([1], SmallestElement.first_n_smallest([2, 1], 1))


if __name__ == '__main__':
    unittest.main()