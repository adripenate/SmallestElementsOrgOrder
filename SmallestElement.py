class SmallestElement:

    def first_n_smallest(self, elements, limit):
        if limit == 0:
            return []
        smallest_elements = []
        for element in elements:
            if element <= limit and len(smallest_elements) < limit:
                smallest_elements.append(element)
            elif element <= limit and max(smallest_elements) > element:
                smallest_elements.pop(smallest_elements.index(max(smallest_elements)))
                smallest_elements.append(element)

        return smallest_elements

