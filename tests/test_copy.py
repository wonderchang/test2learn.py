import copy

import pytest


def test_collection_assignment_statement_is_reference_binding():
    '''
    Assignment statements of compound object in Python do not copy objects,
    they create bindings between a target and an object.
    '''
    data = {'name': 'Foo'}
    clone = data
    assert clone is data

@pytest.mark.parametrize('copy,shallow_compare,deep_compare', [
    (dict,          False, True),   # shallow copy
    (copy.copy,     False, True),   # shallow copy
    (dict.copy,     False, True),   # shallow copy
    (copy.deepcopy, False, False),  # deep copy
])
def test_dictionary_shallow_and_deep_copy(copy, shallow_compare, deep_compare):
    '''
    Demonstrate both shallow copy and deep copy in dictionary data.
    '''
    data = {
        'name': 'Foo',
        'cards': ['abc123', 'def456']
    }
    clone = copy(data)
    assert clone is not data

    # shallow change
    clone['name'] = 'Foo Bar'
    assert (clone['name'] == data['name']) is shallow_compare

    # deep change
    clone['cards'].append('ghi789')
    assert (clone['cards'] is data['cards']) is deep_compare

@pytest.mark.parametrize('copy,shallow_compare,deep_compare', [
    (list,           False, True),   # shallow copy
    (copy.copy,      False, True),   # shallow copy
    (list.copy,      False, True),   # shallow copy
    (lambda x: x[:], False, True),   # shallow copy
    (copy.deepcopy,  False, False),  # deep copy
])
def test_copy_list_copy(copy, shallow_compare, deep_compare):
    '''
    Demonstrate both shallow copy and deep copy in list data.
    '''
    seq = [['a', 'b', 'c'], 1, 2, 3, 4]
    clone = copy(seq)

    # shallow change
    clone.append(5)
    assert (seq == clone) is shallow_compare

    # deep change
    clone[0].append('d')
    assert (seq[0] is clone[0]) is deep_compare

@pytest.mark.parametrize('copy,shallow_compare,deep_compare', [
    (copy.copy,      False, True),   # shallow copy
    (copy.deepcopy,  False, False),  # deep copy
])
def test_copy_object_copy(copy, shallow_compare, deep_compare):
    '''
    Demonstrate both shallow copy and deep copy in object.
    '''
    class Node:

        def __init__(self, value):
            self.value = value
            self.children = []

    node = Node(1)
    clone = copy(node)

    # shallow change
    clone.value += 1
    assert (node.value == clone.value) is shallow_compare

    # deep change
    clone.children.append(Node(2))
    assert (node.children is clone.children) is deep_compare

def test_deepcopy_memo():
    '''
    The deepcopy() function avoids "recursive loop copy" and "over copy" by
    keeping a memo dictionary of objects already copied during the current.

    This test shows how deepcopy at first decompose the compound object into
    multiple objects and write the memo for a shared copy of each divided
    object.

      seq = [[0, 0], [0, 0], 0]               clone = [[0, 0], [0, 0], 0]
       ^       ^       ^                        ^        ^       ^
       |       |       |       - deepcopy ->    |        |       |
      id1     id2     id3                      id4      id5     id6

    For example, `seq` is composed by three list objects:
      1. [0, 0]
      2. [0, 0]
      3. [_, _, 0]

    memo = {
        id1: *id4, (shared_copy_for_seq)
        id2: *id5, (shared_copy_for_seq_1st_list)
        id3: *id6, (shared_copy_for_seq_2nd_list)
        ref: [*id2, *id3, *id1],
    }
    '''
    seq, memo = [[0, 0], [0, 0], 0], {}
    clone = copy.deepcopy(seq, memo)
    seq[0][0] = 1
    clone[0][0] = 100

    id1, id2, id3 = id(seq),   id(seq[0]),   id(seq[1])
    id4, id5, id6 = id(clone), id(clone[0]), id(clone[1])

    shared_copy_for_seq = memo[id1]
    shared_copy_for_seq_1st_list = memo[id2]
    shared_copy_for_seq_2nd_list = memo[id3]

    assert shared_copy_for_seq is clone
    assert shared_copy_for_seq_1st_list is clone[0]
    assert shared_copy_for_seq_2nd_list is clone[1]

    memo_other_ids = list(set(memo.keys()) - set([id1, id2, id3]))
    assert len(memo_other_ids) == 1

    ref = memo_other_ids[0]
    assert memo[ref][0] is seq[0]
    assert memo[ref][1] is seq[1]
    assert memo[ref][2] is seq


# vi:et:ts=4:sw=4:cc=80
