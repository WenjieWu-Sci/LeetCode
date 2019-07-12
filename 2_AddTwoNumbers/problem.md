You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example:**

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

**Note**
* 这道题在理解了链表这种数据结构后就比较容易了
* 链表中的每个节点都包含两个元素，一个是当前节点存储的值，另一个是下一个节点的地址，通过access该节点的next属性即可访问下一个节点
* 反向存储的数字正好和加法的运算顺序是相符的，从低位开始将同位的两个数字相加，与10做除法，余数为结果在该位的数字，商为进位需要额外加的数字
