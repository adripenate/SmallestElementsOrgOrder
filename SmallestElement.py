def first_n_smallest(elements, limit):
    if limit == 0:
        return []
    smallest_elements = []
    for element in elements:
        if len(smallest_elements) < limit:
            add_element_to(smallest_elements, element)
        elif max(smallest_elements) > element:
            remove_biggest_elem(smallest_elements)
            add_element_to(smallest_elements, element)

    return smallest_elements


def add_element_to(smallest_elements, element):
    smallest_elements.append(element)


def remove_biggest_elem(smallest_elements):
    if smallest_elements.count(max(smallest_elements)) > 1:
        smallest_elements.reverse()
        smallest_elements.pop(get_biggest_elem_index(smallest_elements))
        smallest_elements.reverse()
    else:
        smallest_elements.pop(get_biggest_elem_index(smallest_elements))


def get_biggest_elem_index(smallest_elements):
    return smallest_elements.index(max(smallest_elements))

