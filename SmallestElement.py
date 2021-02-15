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

