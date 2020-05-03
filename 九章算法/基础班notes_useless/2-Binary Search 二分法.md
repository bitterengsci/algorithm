# 二分法

## Outline
• 第一境界: 二分法模板
• 时间复杂度小练习
• 递归与非递归的权衡
• 二分的三大痛点
• 通用的二分法模板

• 第二境界: 二分位置 之 圈圈叉叉 Binary Search on Index - OOXX 
• 找到满足某个条件的第一个位置或者最后一个位置

• 第三境界: 二分位置 之 保留一半 Binary Search on Index - Half half 
• 保留有解的一半，或者去掉无解的一半


Binary Search
Given an sorted integer array - nums, and an integer - target.
Find the any/first/last position of target in nums Return -1 if target does not exist.

T(n) = T(n/2) + O(1) = O(logn) 
通过O(1)的时间，把规模为n的问题变为n/2 
思考:通过O(n)的时间，把规模为n的问题变为n/2?

Time Complexity in Coding Interview
• O(1) 极少
• O(logn) 几乎都是二分法
• O(√n) 几乎是分解质因数
• O(n) 高频
• O(nlogn) 一般都可能要排序 • O(n2) 数组，枚举，动态规划 • O(n3) 数组，枚举，动态规划 • O(2n) 与组合有关的搜索
• O(n!) 与排列有关的搜索

独孤九剑 —— 破剑式 比O(n)更优的时间复杂度
几乎只能是O(logn)的二分法 经验之谈:根据时间复杂度倒推算法是面试中的常用策略


Recursion or While Loop? R: Recursion
W: While loop B: Both work


Recursion or Non-Recursion
• 面试中是否使用 Recursion 的几个判断条件
1. 面试官是否要求了不使用 Recursion (如果你不确定，就向面试官询问)
2. 不用 Recursion 是否会造成实现变得很复杂
3. Recursion 的深度是否会很深
4. 题目的考点是 Recursion vs Non-Recursion 还是就是考你是否会Recursion?
• 记住:不要自己下判断，要跟面试官讨论!

二分法常见痛点
• 又死循环了! what are you 弄撒捏!
• 循环结束条件到底是哪个?
• start <= end
• start < end
• start + 1 < end
• 指针变化到底是哪个?
• start = mid
• start = mid + 1
• start = mid - 1

## 第一境界 二分法模板
http://www.jiuzhang.com/solutions/binary-search/
start + 1 < end start + (end - start) / 2 A[mid] ==, <, > A[start] A[end] ? target

令狐大师兄手把手教你写代码 http://www.lintcode.com/problem/classical-binary-search/ http://www.lintcode.com/problem/first-position-of-target/ http://www.lintcode.com/problem/last-position-of-target/

## 第二境界
二分位置 之 OOXX 一般会给你一个数组
让你找数组中第一个/最后一个满足某个条件的位置 OOOOOOO...OOXX....XXXXXX

First Bad Version
http://www.lintcode.com/problem/first-bad-version/ http://www.jiuzhang.com/solutions/first-bad-version/ First version that is bad version


Search In a Big Sorted Array
http://www.lintcode.com/problem/search-in-a-big-sorted-array/ http://www.jiuzhang.com/solutions/search-in-a-big-sorted-array/

Find Minimum in Rotated Sorted Array
http://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/ http://www.jiuzhang.com/solutions/find-minimum-in-rotated-sorted-array/ First position <= Last Number
(WRONG: First position <= or < First Number)


相关练习
• Search a 2D Matrix
• http://www.lintcode.com/en/problem/search-a-2d-matrix/
• http://www.lintcode.com/en/problem/search-a-2d-matrix-ii/
• 不是二分法，但是是常考题
• Search for a Range
• http://www.lintcode.com/en/problem/search-for-a-range/
• http://www.lintcode.com/en/problem/total-occurrence-of-target/
• Maximum Number in Mountain Sequence
• http://www.lintcode.com/en/problem/maximum-number-in-mountain-sequence/
• Smallest Rectangle Enclosing black Pixels
• http://www.lintcode.com/problem/smallest-rectangle-enclosing-black-pixels/ •
• 以上题目的答案请在 http://www.jiuzhang.com/solutions 中搜索  


## 第三境界 二分位置 之 Half half
并无法找到一个条件，形成 OOXX 的模型 但可以根据判断，保留下有解的那一半或者去掉无解的一半


Maximum Number in Mountain Sequence
http://www.lintcode.com/problem/maximum-number-in-mountain-sequence/ http://www.jiuzhang.com/solutions/maximum-number-in-mountain-sequence/ 在先增后减的序列中找最大值


Find Peak Element
http://www.lintcode.com/problem/find-peak-element/ http://www.jiuzhang.com/solutions/find-peak-element/ follow up: Find Peak Element II (by 算法强化班)

Search in Rotated Sorted Array
http://www.lintcode.com/problem/search-in-rotated-sorted-array/ http://www.jiuzhang.com/solutions/search-in-rotated-sorted-array/ 会了这道题，才敢说自己会二分法

## 总结 —— 我们今天学到了什么
• 使用递归与非递归的权衡方法
• 使用T函数的时间复杂度计算方式
• 二分法模板的四点要素
• start + 1 < end
• start + (end - start) / 2
• A[mid] ==, <, >
• A[start] A[end] ? target
• 三个境界
• 二分法模板
• OOXX
• Half half

## Related Questions
• Search in a 2D Matrix II
• 小视频:http://www.jiuzhang.com/video/search-a-2d-matrix-ii/ • 不是二分法，但是是常考题
• Binary Search:
• http://www.lintcode.com/en/tag/binary-search/
• Rotate Array
• 小视频:http://www.jiuzhang.com/video/3-step-reverse/
• http://www.lintcode.com/problem/recover-rotated-sorted-array/ • http://www.lintcode.com/problem/rotate-string/
• 三步翻转法:
• [4,5,1,2,3] → [5,4,1,2,3] → [5,4,3,2,1] → [1,2,3,4,5]
• 点题时间:
• http://www.jiuzhang.com/qa/974/

想学习更难的二分法?
《九章算法强化班》 http://www.jiuzhang.com/course/5/ 

## 第四境界(至高境界):二分答案 例题:http://www.lintcode.com/problem/copy-books/

二分法相关题目的解题报告 参考程序+详细的思路描述
http://www.jiuzhang.com/article/?tags=binary-search

