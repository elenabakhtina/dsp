# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
import ast

def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.
    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    n = 0
    for i in range(0,len(words)):
        if len(words[i]) >= 2:
            if words[i][0] == words[i][-1]:
                n = n + 1
    print("For the given list ",words," the answer is ",n)

    #raise NotImplementedError

def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    words_x = []
    words_not_x = []
    for i in range(len(words)):
        if words[i][0] == 'x':
            words_x.append(words[i])
        else:
            words_not_x.append(words[i])
    words_result = sorted(words_x) + sorted(words_not_x)
    print("Original string: ",words)
    print("Resulting string: ",words_result)

    #raise NotImplementedError

def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].
    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    tuples_result = sorted(tuples, key=lambda last_el: last_el[-1])
    print("Origianl list of tuples: ",tuples)
    print("Resulting list of tuples: ",tuples_result)

    #raise NotImplementedError

def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    temp = nums[0]
    nums_result = []
    nums_result.append(nums[0])
    for i in range(1,len(nums)):
        if nums[i] != temp:
            nums_result.append(nums[i])
            temp = nums[i]
    print(nums_result)

    #raise NotImplementedError


def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.
    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    # Version 1 works with the input in the following format:
    # aa,xx,zz and bb,cc
    # aa,xx and bb,cc,zz
    # aa,aa and aa,bb,bb
    # l1 = input("Enter a list of strings, separated by comma: ")
    # l2 = input("Enter another list of strings, separated by comma: ")
    # l = l1 + ',' + l2
    # ll = list(l.split(','))
    # print(sorted(ll))

    # Version 2 works with the input in the following format:
    # ['aa', 'xx', 'zz'] and ['bb', 'cc']
    # ['aa', 'xx'] and ['bb', 'cc', 'zz']
    # ['aa', 'aa'] and ['aa', 'bb', 'bb']
    l = list1 + list2
    print(sorted(l))

    #raise NotImplementedError

print("There are 5 functions to test:")
print("1. match_ends(words), \n2. front_x(words), \n3. sort_last(tuples)")
print("4. remove_adjacent(nums), \n5. linear_merge(list1, list2)")
fun = int(input("Enter a number of a function you want to test or 0 to quit: "))
while fun in range(1,6):
    if fun == 1:
        print('-'*10)
        print("Returns the count of the number of strings where")
        print("the string length is at least 2 and the first and last chars")
        print("of the string are the same.")
        # 'aba','xyz','aa','x','bbb' -> a quote mark "'" is considered
        #               a part of the string, thus the answer is 5
        # aba,xyz,aa,x,bbb -> answer is 3
        # ,x,xy,xyx,xx -> answer is 2
        # aaa,be,abc,hello -> answer is 1
        words_str = input("Enter a list of strings, separated by comma: ")
        words = list(words_str.split(','))
        match_ends(words)
    elif fun == 2:
        print('-'*10)
        print("Returns a list where strings begining with 'x' go first,")
        print("then the rest of the entered strings in the alphabetical order.")
        # The function works with the input in the following format:
        # mix,xyz,apple,xanadu,aardvark
        # bbb,ccc,axx,xzz,xaa
        # ccc,bbb,aaa,xcc,xaa
        words_str = input("Enter a list of strings, separated by comma, with no quote mark or spaces: ")
        words = list(words_str.split(','))
        front_x(words)
    elif fun == 3:
        print('-'*10)
        print("Returns a list sorted in increasing order by the last element in each tuple.")
        tuples = ast.literal_eval(input("Enter a list of non-empty tuples in parentheses, separated by comma: "))
        # Safely evaluates an expression node or a Unicode or Latin-1 encoded string
        # containing a Python literal or container display.
        # The string or node provided may only consist of
        # the following Python literal structures:
        # strings, numbers, tuples, lists, dicts, booleans, and None.
        sort_last(tuples)
    elif fun == 4:
        print('-'*10)
        print("Returns a list where all adjacent equal elements have been reduced to a single element.")
        a = ast.literal_eval(input("Enter a list of integers, separated by comma: "))
        nums = list(a)
        remove_adjacent(nums)
    elif fun == 5:
        print('-'*10)
        print("Returns a merged list of all the elements in sorted order.")
        list1 = ast.literal_eval(input("Enter a list of strings, separated by comma: "))
        list2 = ast.literal_eval(input("Enter another list of strings, separated by comma: "))
        linear_merge(list1, list2)
    fun = int(input("To continue, enter a number from 1 to 5 or 0 to quit: "))
