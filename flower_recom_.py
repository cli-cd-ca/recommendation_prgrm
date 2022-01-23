
from linkedlist import LinkedList
from flower_data import *
from string import capwords

def flowerlinkedlist(lst):
    ll = LinkedList()
    for el in lst:
        ll.insert_beginning(el)
    return ll

typell = flowerlinkedlist(flower_types)
datall = flowerlinkedlist(flower_data)

def get_ll_values(ll, value_to_get):
    result = []
    current_node = ll.get_head_node()
    while current_node.get_value() != None:
        if current_node.get_value()[0] == value_to_get:
            result.append(current_node.get_value())
        elif current_node.get_value()[0][0] == value_to_get:
            result.append(current_node.get_value()[0])
        current_node = current_node.get_next_node()
    return result