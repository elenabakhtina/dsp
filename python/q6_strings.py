# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count < 10:
        print("Number of donuts: %d" % count)
    elif count >= 10:
        print("Number of donuts: many")

    #raise NotImplementedError


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s) < 2:
        ss = ''
    else:
        ss = s[0:2] + s[-2:]
    print(ss)

    #raise NotImplementedError


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    first_char = s[0]
    ss = ''
    ss = ss + first_char
    i = 1
    while i < len(s):
        if s[i] == first_char:
            ss = ss + '*'
        else:
            ss = ss + s[i]
        i = i + 1
    print(ss)

    #raise NotImplementedError


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    a1 = b[:2] + a[2:]
    b1 = a[:2] + b[2:]
    print(a1 + ' ' + b1)
    #raise NotImplementedError


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) < 3:
        print(s)
    elif s[-3:] == 'ing':
        print(s + 'ly')
    else:
        print(s + 'ing')

    #raise NotImplementedError


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    #the code works only if there is no more than one instances of 'not'...'bad' in the string.
    if 'not' and 'bad' in s:
        p1 = s.find('not')
        p2 = s.find('bad',p1)
        if p2 == -1:
            print(s)
        else:
            ss = s[:p1] + 'good' + s[p2+3:]
            print(ss)
    else:
        print(s)

    #raise NotImplementedError


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    a_half = len(a) // 2 + len(a) % 2
    b_half = len(b) // 2 + len(b) % 2
    ab = a[:a_half] + b[:b_half] + a[a_half:] + b[b_half:]
    print(ab)

    #raise NotImplementedError

print("There are 7 functions to test:")
print("1. donuts(count), \n2. both_ends(s), \n3. fix_start(s), \n4. mix_up(a, b)")
print("5. verbing(s), \n6. not_bad(s), \n7. front_back(a, b)")
fun = int(input("Enter a number of a function you want to test or 0 to quit: "))
while fun in range(1,8):
    if fun == 1:
        print('-'*10)
        print("Returns a string of the form 'Number of donuts: <count>' or 'many'")
        count = int(input("Enter a number of donuts: "))
        while count < 0:
            count = int(input("Please enter a positive number: "))
        donuts(count)
    elif fun == 2:
        print('-'*10)
        print("Returns a string made of the first 2 and the last 2 chars of the original string.")
        s = input("Enter a string: ")
        both_ends(s)
    elif fun == 3:
        print('-'*10)
        print("Returns a string where all occurences of its first char have been changed to '*'.")
        s = input("Enter a string of at least 1 char: ")
        fix_start(s)
    elif fun == 4:
        print('-'*10)
        print("Returns a single string'<a> <b>', where the first 2 chars of each string are swapped.")
        a = input("Enter a string with 2 or more chars: ")
        b = input("Enter another string with 2 or more chars: ")
        mix_up(a, b)
    elif fun == 5:
        print('-'*10)
        print("Adds 'ing' or 'ly' to a word of 3 chars or more, else leaves it w/t a change.")
        s = input("Enter a string with at least 3 chars: ")
        verbing(s)
    elif fun == 6:
        print('-'*10)
        print("Changes 'not'...'bad' to 'good'.")
        s = input("Enter a string: ")
        not_bad(s)
    elif fun == 7:
        print('-'*10)
        print("Returns a string of the form a-front + b-front + a-back + b-back.")
        a = input("Enter a string: ")
        b = input("Enter another string: ")
        front_back(a, b)
    fun = int(input("To continue, enter a number from 1 to 7 or 0 to quit: "))
