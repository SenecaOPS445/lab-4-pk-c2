#!/usr/bin/env python3

def join_lists(l1, l2):
    """
    Combine two lists and return a list with all unique values.
    """
    return list(set(l1) | set(l2))

def match_lists(l1, l2):
    """
    Return a list that contains all values found in both lists (intersection).
    """
    return list(set(l1) & set(l2))

def diff_lists(l1, l2):
    """
    Return a list that contains all values unique to either list (symmetric difference).
    """
    return list(set(l1) ^ set(l2))

if __name__ == '__main__':
    list1 = list(range(1, 10))  # Creates a list [1, 2, 3, ..., 9]
    list2 = list(range(5, 15))  # Creates a list [5, 6, 7, ..., 14]

    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))

