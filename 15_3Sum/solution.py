#!/usr/bin/python
# -*- coding: utf-8 -*-

# credit: https://leetcode.com/problems/3sum/discuss/261764/Python-Solution-faster-than-97
def threeSum(nums):
    ans = set([])
    plus = sorted([n for n in nums if n>0])
    plus_c = set(plus)
    zero = [n for n in nums if n == 0]
    minus = sorted([n for n in nums if n<0])
    minus_c = set(minus)
    # all zero
    if len(zero)>2:
        ans.add((0,0,0))
    # plus zero minus
    if len(zero)>0:
        for n in minus:
            if -n in plus_c:
                ans.add((n,0,-n))
    # plus minus minus
    n = len(minus)
    for i in range(n):
        for j in range(i+1,n):
            diff = -(minus[i]+minus[j])
            if diff in plus_c:
                ans.add((minus[i],minus[j],diff))
    # plus plus minus
    n = len(plus)
    for i in range(n):
        for j in range(i+1,n):
            diff = -(plus[i]+plus[j])
            if diff in minus_c:
                ans.add((diff,plus[i],plus[j]))
    return list(ans)


# time limit exceeded
#def threeSum(nums):
#    result = []
#    for i in range(len(nums)):
#        a = nums[i]
#        for j in range(i+1,len(nums)):
#            b = nums[j]
#            twoSum = a + b
#            for c in nums[j+1::]:
#                if c + twoSum == 0:
#                    ans = [a, b, c]
#                    ans.sort()
#                    if len(result) == 0:
#                        result.append(ans)
#                    else:
#                        tag = False
#                        for searched in result:
#                            if ans == searched:
#                                tag = True
#                        if not tag:
#                            result.append(ans)
#    return result


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))


if __name__=='__main__':
    main()
