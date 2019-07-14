#!/usr/bin/python
#-*- coding: utf-8 -*-
import math


"""
def isPalindrome(x):
    if x < 0:
        return False
    elif x < 10:
        return True
    else:
        return isStrPalindrome(str(x))


def isStrPalindrome(s):
    if len(s) < 2:
        return True
    else:
        return s[0] == s[-1] and isStrPalindrome(s[1:-1])
"""

"""
def isPalindrome(x):
    if x < 0:
        return False
    elif x < 10:
        return True
    else:
        s = str(x)
        rev_s = s[::-1]
        if rev_s == s:
            return True
        else:
            return False
"""

def isPalindrome(x):
    """
    Input: x, an integer
    Return: bool
    """
    if not x:
        return True
    if x < 0:
        return False
    num_digits = math.floor(math.log10(x)) + 1
    while num_digits > 1:
        left_num = x//pow(10, num_digits-1)
        right_num = x%10
        if left_num != right_num:
            return False
        x -= left_num*pow(10, num_digits-1)
        x -= right_num
        x /= 10
        num_digits -=2

    return True

def testIsPalindrome():
    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(10))


testIsPalindrome()
