import unittest


class SmallestElement:
    @classmethod
    def first_n_smallest(self, elements, limit):
        if limit == 0:
            return []
        smallest_elements = []
        for element in elements:
            if self.pass_limit(self, element, limit) and len(smallest_elements) < limit:
                smallest_elements.append(element)
            elif self.pass_limit(self, element, limit) and max(smallest_elements) > element:
                smallest_elements.pop(SmallestElement.get_biggest_elem_index(smallest_elements))
                smallest_elements.append(element)

        return smallest_elements

    @classmethod
    def get_biggest_elem_index(cls, smallest_elements):
        return smallest_elements.index(max(smallest_elements))

    def pass_limit(self, element, limit):
        return element <= limit


class FindPairsTest(unittest.TestCase):

    def test_should_skip_search(self):
        self.assertEqual([], SmallestElement.first_n_smallest([1, 2, 3, 4, 5], 0))

    def test_should_give_one_number(self):
        self.assertEqual([1], SmallestElement.first_n_smallest([1], 1))

    def test_should_give_first_number(self):
        self.assertEqual([1], SmallestElement.first_n_smallest([1, 2], 1))

    def test_should_find_second_number(self):
        self.assertEqual([1], SmallestElement.first_n_smallest([2, 1], 1))

    def test_should_give_two_numbers(self):
        self.assertEqual([1, 1], SmallestElement.first_n_smallest([1, 1, 1, 1], 2))

    def test_should_give_smallest_numbers(self):
        self.assertEqual([1, 1], SmallestElement.first_n_smallest([4, 1, 2, 1], 2))


if __name__ == '__main__':
    unittest.main()