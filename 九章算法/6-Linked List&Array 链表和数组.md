链表与数组 Linked List & Array
课程版本 v4.2 主讲 令狐冲 扫描二维码关注微信/微博
获取最新面试题及权威解答
微信: ninechapter
微博: http://www.weibo.com/ninechapter 知乎: http://zhuanlan.zhihu.com/jiuzhang 官网: http://www.jiuzhang.com

第1页

大纲 Outline
• Linked List
• Dummy Node
• High Frequency • Array
• Subarray
• Sorted Array

第2页

Basic Knowledge Test
• What’s the output of the following code?

第3页

Reverse Nodes in k-Groups
http://www.lintcode.com/en/problem/reverse-nodes-in-k-group/
http://www.jiuzhang.com/solutions/reverse-nodes-in-k-group/

第4页

独孤九剑 —— 破索式 链表结构发生变化时
就需要 Dummy Node

第5页

Dummy Node 哨兵节点八问八答
如何使用 Dummy Node
head = dummy 这句话总是需要么?
什么时候使用 Dummy Node?
Dummy Node 是否需要删除?
使用 Dummy Node 算面试官会说我耗费了额外空间么? Dummy Node 非用不可么?
Dummy Node 初始化的值重要么? 链表的问题都需要用到 Dummy Node 么?

第6页

用到了 Dummy Node 的值得一做的题目
http://www.lintcode.com/en/problem/partition-list/
http://www.lintcode.com/en/problem/merge-two-sorted-lists/ http://www.lintcode.com/en/problem/reverse-linked-list-ii/ http://www.lintcode.com/en/problem/swap-two-nodes-in-linked-list/ http://www.lintcode.com/en/problem/reorder-list/ http://www.lintcode.com/en/problem/rotate-list/

第7页

Copy List with Random Pointer
http://www.lintcode.com/problem/copy-list-with-random-pointer/
http://www.jiuzhang.com/solutions/copy-list-with-random-pointer/

第8页

Linked List Cycle
http://www.lintcode.com/en/problem/linked-list-cycle/
http://www.jiuzhang.com/solutions/linked-list-cycle/
follow up:
http://www.lintcode.com/en/problem/linked-list-cycle-ii/ http://www.jiuzhang.com/solutions/intersection-of-two-linked-lists/

第9页

Sort List
http://www.lintcode.com/en/problem/sort-list/
http://www.jiuzhang.com/solutions/sort-list/
问:哪些排序算法时间复杂度是 O(nlogn) 的? 问:哪些排序算法空间复杂度是 O(1) 的?

第10页

Related Questions
• http://www.lintcode.com/problem/convert-sorted-list-to-balanced-bst/
• http://www.lintcode.com/problem/delete-node-in-the-middle-of-singly-linked-list/
• http://www.lintcode.com/problem/convert-binary-search-tree-to-doubly-linked-list/

第11页

休息5分钟 Take a break

第12页

Sorted Array
排序数组

第13页

Merge Two Sorted Arrays
http://www.lintcode.com/problem/merge-two-sorted-arrays
http://www.jiuzhang.com/solutions/merge-two-sorted-arrays/
Copyright © www.jiuzhang.com
第14页

Related Questions
• 将小数组归并到大数组里
• http://www.lintcode.com/problem/merge-sorted-array/ • http://www.jiuzhang.com/solutions/merge-sorted-array/
• 两个数组的交
• http://www.lintcode.com/problem/intersection-of-two-arrays/
• 数组内积(点乘)
• Example [1,3] · [2,4] = 1*2 + 3*4 = 14
• Follow up: 两个数组都非常大，但是其中都包含很多0
• Example [1,0,0,0,0 ..., 0, 2, 0,..., 0, 3] · [0,..., 0, 4, 0,..., 0, 5]
Copyright © www.jiuzhang.com
第15页

Median of Two Sorted Arrays
http://www.lintcode.com/problem/median-of-two-sorted-arrays/
http://www.jiuzhang.com/solutions/median-of-two-sorted-arrays/
Copyright © www.jiuzhang.com
第16页

子数组 Subarray
令 PrefixSum[i] = A[0] + A[1] + ... A[i - 1], PrefixSum[0] = 0 易知构造 PrefixSum 耗费 O(n) 时间和 O(n) 空间 如需计算子数组从下标i到下标j之间的所有数之和 则有 Sum(i~j) = PrefixSum[j + 1] - PrefixSum[i]

第17页
Maximum Subarray
http://www.lintcode.com/en/problem/maximum-subarray/
http://www.jiuzhang.com/solutions/maximum-subarray/

Subarray Sum
http://www.lintcode.com/en/problem/subarray-sum/
http://www.jiuzhang.com/solutions/subarray-sum/

第19页

Subarray Sum Closest
http://www.lintcode.com/en/problem/subarray-sum-closest/
http://www.jiuzhang.com/solutions/subarray-sum-closest/

第20页
