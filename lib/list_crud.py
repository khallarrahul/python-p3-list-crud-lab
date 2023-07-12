def create_an_empty_list():
    return []


def create_a_list():
    return ["element1", "element2", "element3", "element4"]


def add_element_to_end_of_list(l, element):
    l.append(element)
    return l


my_list = create_a_list()
add_element_to_end_of_list(my_list, "banana")


def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l


my_list = create_a_list()
add_element_to_start_of_list(my_list, "orange")


def remove_element_from_end_of_list(l):
    l.pop(len(l) - 1)
    return l


my_list = create_a_list()
remove_element_from_end_of_list(my_list)


def remove_element_from_start_of_list(l):
    del l[0]
    return l


my_list = create_a_list()
remove_element_from_end_of_list(my_list)


def retrieve_first_element_from_list(l):
    first_element = l[0]
    return first_element


my_list = create_a_list()
retrieve_first_element_from_list(my_list)


def retrieve_element_from_index(l, index):
    any_element = l[index]
    return any_element


my_list = create_a_list()
retrieve_element_from_index(my_list, 0)


def retrieve_last_element_from_list(l):
    last_element = l[len(l) - 1]
    return last_element


my_list = create_a_list()
retrieve_last_element_from_list(my_list)
