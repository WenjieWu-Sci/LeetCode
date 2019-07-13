**Problem:**

Given an array `nums` of *n* integers, are there elements *a, b, c* in `nums` such that *a + b + c* = 0? Find all unique triplets in the array which gives the sum of zero.

**Note:**

The solution set must not contain duplicate triplets.

**Example:**
```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

**思路1**
* 将list中的元素按照负数、正数、零分为三类，并按序排列好
* 利用set清除掉非零list中重复的元素
* 按照零零零、正零负、正负负、正正负四类进行遍历

**思路2** `(time limit exceeded)` 
1. 不重复地遍历list找到和为0的三个数
2. 按从小到大的顺序排好
3. 比较是否有重复，没有重复就添加到结果中
4. 重复1->2->3，直到遍历所有可能的组合
