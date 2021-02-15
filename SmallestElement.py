def first_n_smallest(elements, limit):
    if limit == 0:
        return []
    smallest_elements = elements[:limit:]
    for element in elements[limit::]:
        if max(smallest_elements) > element:
            remove_biggest_elem(smallest_elements)
            add_element_to(smallest_elements, element)

    return smallest_elements


def add_element_to(smallest_elements, element):
    smallest_elements.append(element)


def remove_biggest_elem(smallest_elements):
    smallest_elements.reverse()
    smallest_elements.pop(get_biggest_elem_index(smallest_elements))
    smallest_elements.reverse()


def get_biggest_elem_index(smallest_elements):
    return smallest_elements.index(max(smallest_elements))

