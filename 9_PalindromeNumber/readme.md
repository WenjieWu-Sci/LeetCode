**Problem:**

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

**Example 1:**
```
Input: 121
Output: true
```
**Example 2:**
```
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```
**Example 3:**
```
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```
**Follow up:**

Coud you solve it without converting the integer to a string?

**思路1**
* 使用递归
* 负数返回False，0~9返回True，只对>9的正数做判断
* 将integer转换为string，base case是当len(s)<2时返回True，recursive case是判断首尾字符是否相同以及去掉首尾后剩下的是否是palindrome number

**结果1**
* Runtime: 68 ms, faster than 80.83% of Python3 online submissions for Palindrome Number
* Memory Usage: 13.4 MB, less than 7.92% of Python3 online submissions for Palindrome Number

**思路2**
* 将integer转换为string后，reverse这个string，然后比较reverse前后的string是否相等

**结果2**
* Runtime: 64 ms, faster than 89.31% of Python3 online submissions for Palindrome Number
* Memory Usage: 13.5 MB, less than 5.32% of Python3 online submissions for Palindrome Number

**思路3**
* 利用log函数得到整数的位数
* 循环比较首尾两个数字是否相等
