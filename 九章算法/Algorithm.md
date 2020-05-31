
# 二分法 Binary Search
## 第2节课: Binary Search 二分法
Outline
1.第一境界: 二分法模板
时间复杂度小练习
递归与非递归的权衡
二分的三大痛点	while < 还是 while <=;  超出time limit
通用的二分法模板
2.第二境界: 二分位置 之 圈圈叉叉 Binary Search on Index - OOXX  (抽象化满足条件)
找到满足某个条件的第一个位置或者最后一个位置
3.第三境界: 二分位置 之 保留一半 Binary Search on Index - Half Half (log(n)的思想来源, 如何做到二分)
保留有解的一半, 或者去掉无解的一半

Binary Search
Given a sorted integer array - nums, and an integer - target.
Find the any/first/last position of target in nums, Return -1 if target does not exist.
(问last时, 容易出现死循环, 超时)
两个指针一头一尾(left/right) 和target比较, 后将left/right移到中间,直到left/right并到一起
if (nums[mid] < target)   O(1)的if语句

时间复杂度 Time Complexity (面试必问)
不要说 O(2n), O(n+10), O(n3+n2), 时间复杂度不论系数, 不论常数项, 只看最高项, 只关心数量级。
n = 数据规模  O(2n)=O(n) 		O(n+10)=O(n) 		O(n3+n2)=O(n3)	 O(n2+nlogn)=O(n2)

T(n) = T(n/2) + O(1) = O(logn) 		通过O(1) 把n→n/2 规模的问题
通过O(1)的时间, 把规模为n的问题变为n/2
T(n) = T(n/2) + O(1) = T(n/4) + O(1) + O(1) = T(n/8) + 3O(1) =.. = T(n/n) + log2(n)×O(1) = T(1) + log2(n)×O(1)
T(n) = 规模为n的算法的时间复杂度  T(1)=输入规模为1时, 算法的时间复杂度

O(log2n)=O(log4n) = 2O(log2n)   O(logn)=O(logn2) = 2O(logn)	时间复杂度不管系数, log以什么为底无所谓。

通过O(n)的时间, 把规模为n的问题变为n/2  (不是O(nlogn)!!!)
T(n) = T(n/2) + O(n) = T(n/4) + O(n/2) + O(n)  = T(n/8) + O(n/4) +  O(n/2) + O(n) =..  	 先不约去O(n/4)和O(n/2), 展开到最后再约去
= T(1) + O(n) + O(n/2) + O(n/4) +.. O(1) = O(n+n/2+n/4+…+2+1)  ≈ O(2n-1) = O(2n)= O(n)

空间复杂度 Space Complexity (很少问) —> 程序开了几个数组, 每个数组长度多少, 相加即可

Time Complexity in Coding Interview
O(1) 极少			return 一个公式即可, 不用写程序
O(logn) 几乎都是二分法	
O(√n) 几乎是分解质因数	e.g 6=2×3 枚举至√n
O(n) 高频				→ 暴力 for 循环, O(n)之下只有O(logn)
O(nlogn) 一般都可能要排序 	先将数组排序, 解法豁然开朗~
O(n2) 数组, 枚举, 动态规划
O(n3) 数组, 枚举, 动态规划
O(2n) 与组合有关的搜索		subset题目
O(n!) 与排列有关的搜索
考察如何计算时间复杂度, 面试中常考O(n), O(nlogn), O(n2)

独孤九剑——破剑式 比O(n)更优的时间复杂度
几乎只能是O(logn)的二分法 经验之谈:根据时间复杂度倒推算法是面试中的常用策略
	若一眼看就是O(n), 就要考虑O(logn)的实现方式了 → 两个指针一头一尾, 中间取点, 去一半

哪种方法实现二分法 Recursion or While Loop? 		R: Recursion W: While loop B: Both work 
(建议, 能不用recursion就不用, recursion是一个不好的coding pattern, 递归易造成stack overflow 栈溢出, 程序crash)
面试中是否使用 Recursion 的几个判断条件
①面试官是否要求了不使用 Recursion (如果你不确定, 就向面试官询问)
②不用 Recursion 是否会造成实现变得很复杂 (二分法一般不会很复杂)
③Recursion 的深度是否会很深
④题目的考点是 Recursion vs Non-Recursion, 还是就是考你是否会Recursion?
记住: 不要自己下判断, 要跟面试官讨论!

二分法常见痛点
①又死循环了! what are you 弄撒捏!
②循环结束条件到底是哪个?
start <= end
start < end	    两根指针指向同一个数时, 才会结束 (容易死循环)
start + 1 < end    两个指针相邻即可结束 (避免死循环)
③指针变化到底是哪个?
start = mid
start = mid + 1
start = mid - 1

第一境界 二分法模板
http://www.jiuzhang.com/solutions/binary-search/
start + 1 < end    		    中间隔着一个时即可结束, 避免死循环
mid = start + (end - start) / 2      等于mid=(start+end)/2 但避免s和e过大时造成越界   
A[mid] ==, <, >     		    三种情况分开讨论
A[start] A[end] ? target              出了while循环后, 寻找结果。 二分法→不断缩小区间, 不一定直接return答案

*  Lintcode 457-Classical Binary Search
*  Lintcode 14-First Position of Target
*  Lintcode 458-Last Position of Target


第二境界 二分位置 之 OOXX 一般会给你一个数组
让你找数组中第一个/最后一个满足某个条件的位置 OOOOOOO…OOXX....XXXXXX
		O = '< target的数' X='≥ target的数'   找第一个X 或者最后一个O

*** Lintcode 74-First Bad Version
*** Lintcode 447-Search in a Big Sorted Array   (答案仅对学员开放)
排序数组二分法 → 二分, 起点+终点, 取中点
现在没有终点怎么办? 找终点, 令点≥target (终点要在k的级别上)
Vector/ArrayList: 动态数组实现方式, 不用声明多大多长, 倍增思想, 和网络访问的exponential backoff类似
	Note: 一道题问完用什么数据结构, 还会追问数据结构的实现方式。
要求复杂度O(log k) 	k是数所在位置
以2倍递增 1→2→4→8 直到 ≥target, 共递增logk次  (可以确定数在 [k, 2k]范围里)

*** Lintcode 159-Find Minimum in Rotated Sorted Array
First position <= Last Number
(WRONG: First position <= or < First Number)

Sorted Array⊆Rotated Sorted Array (在做RSA的题时, 需要考虑没有rotated的情况)

相关练习
*** Lintcode 28-Search a 2D Matrix (不是二分法, 但是是常考题)  
*** Lintcode 38-Search a 2D Matrix II   (不是二分法, 但是是常考题)

*** Lintcode 61-Search for a Range
*** Lintcode 600-Smallest Rectangle Enclosing black Pixels
→ 在列中需要找出第一个'1'出现的最左侧坐标和最右侧坐标, 在行中需要找出第一个'1'出现的最上面坐标和最下面坐标。采用二分的方法在区间查找即可。最后返回(right - left + 1) * (down - up + 1)即可。

第三境界 二分位置 之 Half Half
无法找到一个条件, 形成 OOXX 的模型; 但可以根据判断, 保留下有解的那一半或者去掉无解的一半

*** Lintcode 585-Maximum Number in Mountain Sequence (在先增后减的序列中找最大值)
*** Lintcode 75-Find Peak Element
先增后减数组, 一定有peak(局部最大); 找所有peak→for循环, O(n) 		找一个peak→非排序数组如何二分?
四种情况  
    mid-1 < mid < mid+1 (递减区间, 左半部分一定有峰)   mid-1>mid>mid+1 (有半部分一定有峰) 
    mid > mid-1 & mid+1 (mid就是峰, return it)      mid < mid-1 & mid+1 (左右两边都至少存在一个解)

有时选算法, 看要求的答案个数(为下限)

*** Lintcode Find Peak Element II (by 算法强化班)    
TODO

*** Lintcode 62-Search in Rotated Sorted Array
4 5 6 7 0 1 2   target=6
o o x x o o o      (not ooxx)
→找最小的数(找到o) O(logn), 然后还原成 ooxx, 但还原操作为O(n), 不行
→用两次二分的方法: 
第一次二分找到最小数的位置, 参考 find minimum number in rotated sorted array 第二次二分确定 target 在左侧区间还是右侧 (start ≤ target ≤ mid 答案在左边,  target > mid && target < start 答案在右边) 再用一个普通的二分法即可找到
→用一次二分法

二分思想要求, 去掉一半后, 剩下的一半必须还是刚开始的构型。→ 二分之后必须还是RSA (SA⊆RSA)

总结
  使用递归与非递归的权衡方法
  使用T函数的时间复杂度计算方式
  二分法模板的四点要素 
  start + 1 < end
  start + (end - start) / 2
  A[mid] ==, <, >
  A[start] A[end] ? target
  三个境界: 二分法模板, OOXX, Half half
Binary Search: http://www.lintcode.com/en/tag/binary-search/

三步翻转法:http://www.jiuzhang.com/video/3-step-reverse/
*** Lintcode 39-Recover Rotated Sorted Array
*** Lintcode 8-Rotate String
三步翻转法: [4,5,1,2,3] → [5,4,1,2,3] → [5,4,3,2,1] → [1,2,3,4,5]

点题时间: http://www.jiuzhang.com/qa/974/

想学习更难的二分法? 第四境界(至高境界):二分答案
*** Lintcode 437-Copy Books

二分法相关题目的解题报告 参考程序+详细的思路描述 http://www.jiuzhang.com/article/?tags=binary-search

*** Lintcode not answered or marked: 159, 38, 61, 437

k closest number:  oooxxxx 先找到x 然后左右两个指针分别往两边移动  O(logn + k)  因为不知道logn和k哪个大


## 3.2. 二分法难题 (Hard) 第四境界(至高境界): 二分答案
按值二分, 找到单调的地方

二分查找某个元素在数组中的位置的时间复杂度 O(logn). 每次操作都选择当前数组的中位数与目标元素值比较, 若比目标值更大, 则在中位数前继续寻找, 反之在中位数后寻找, 这样每次可以将搜索范围缩小一半

哪种写法会出现死循环? A 若left=0, right=1, mid=0, 且nums[mid] < target的条件下, 出现死循环
```python
while left < right:
    mid = left + (right - left) // 2
    if nums[mid] < target:
        left = mid
    else:
        right = mid

while left + 1 < right:
    mid = left + (right - left) // 2
    if nums[mid] < target:
        left = mid
    else:
        right = mid 

while left < right:
    mid = left + (right - left) // 2
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```
LintCode 75: [Find Peak Element]()
https://www.lintcode.com/problem/find-peak-element/ 
https://www.jiuzhang.com/solutions/find-peak-element/
给定A[0..n-1], 其中没有相邻元素相同, 并且A[0] < A[1], A[n-2] > A[n-1], 找到任意一个P, 满足A[P-1] < A[P] > A[P+1]
输入: [1, 5, 6, 8, 7, 9, 4]  输出: 3
- 首先, 这样的P肯定存在
- 因为A[0] < A[1], 如果A[1]不是要找的元素, A[1] < A[2]; A[2] < A[3]; ...
- 但是A[n-2] > A[n-1]
- 二分查找, 对于mid位置, 如果A[mid] < A[mid+1], 继续向右找; 否则向左
   
二分答案 Binary Search on Result
往往没有给你一个数组让你二分, 同样是找到满足某个条件的最大或者最小值

解题方法 通过猜值判断是否满足题意不对去搜索可能解 
1.找到可行解范围 2.猜答案 3.检验条件 4.调整搜索范围

[Sqrt(x)]()
https://www.lintcode.com/problem/sqrtx/ 
https://www.jiuzhang.com/solutions/sqrt-x 
Last number that number^2 <= x
follow up: what if return a double, not an integer?

[Sqrt(x) II]()
https://www.lintcode.com/problem/sqrtx-ii/ 
https://www.jiuzhang.com/solution/sqrtx-ii/
一直二分直到 |number^2 - x| <= 1e-10

LintCode 183: [Wood Cut]()
https://www.lintcode.com/problem/wood-cut/ 
https://www.jiuzhang.com/solutions/wood-cut/
给定n块木头, 长度分别是L[0]..L[n-1]. 要求找到最长的长度s, 使得这些木头可以切出至少k块长度为s的木头
输入: L=[232, 124, 456], k=7 输出:114
- 首先, 我们发现, 对于一个长度s, 如果可以切出t段;而对于另一个长度S>s,可 以切出T段, 则一定有t>=T
- 所以如果长度s切出的段数不够k, 答案肯定比s小è二分答案!
- 同理, 如果长度s切出的段数>=k, 答案肯定>=s
- 时间复杂度:O(nlogL)

LintCode 437: [Copy Books]()
https://www.lintcode.com/problem/copy-books/ 
https://www.jiuzhang.com/solutions/copy-books/
有N本书需要被抄写, 第i本书有A, i=0, 1, ..., N-1; 有K个抄写员, 每个抄写员可以抄写连续的若干本书(例如:第3~5本书, 或者第10本书); 每个抄写员的抄写速度都一样, 最少需要多少时间抄写完所有的书
输入: A = [3, 2, 4], K=2  输出: 5 (第一个抄写员抄写第1本和第2本书, 第二个抄写员抄写第3本书) 
- 题目要求K个抄写员抄完最少需要的时间
- 反过来想, 如果我们限定时间不超过T, 最少需要的抄写员
- 这个问题比较好做, 贪心法
- 从第一本书开始, 第一个人一直抄到时间即将超过T 
- 第二个人, ...
- 如果需要的抄写员>K, 说明答案一定>T; 反之答案<=Tè二分答案
  
LintCode 633: [Find The Duplicate Number]()
https://www.lintcode.com/problem/find-the-duplicate-number/ 
https://www.jiuzhang.com/solutions/find-the-duplicate-number/
给定一个长度为n+1的数组, 其中均为1到n之间的整数; 保证只有一个数字重复了多次; 找到这个数字 (辅助空间只能O(1))
输入: [5,5,5,1,2,3] 输出: 5

- 假设答案是S, 数组一定是(假设排好序):[1,3,...,S,...,S,S+1,...,n], 那么其中<=S的数大于S
- 而且对于所有T >= S, <=T的个数大于T
- 而对于所有T < S, <=T的个数小于等于T
- 二分法 O(nlog2n) 

LintCode 617: [Maximum Average Subarray II]() 二分答案的典型题目
https://www.lintcode.com/problem/maximum-average-subarray-ii/ 
https://www.jiuzhang.com/solutions/maximum-average-subarray-ii/
给定一个数组A, 找到其中平均值最大的子数组, 要求长度>=k
输入: [1, 12, -5, -6, 50, 3], k = 3  输出: 15.667   (-6+50+3)/3=15.667

- 如果要求和最大, 可以用前缀和数组。但是平均值最大不好求
- 那么如果最大平均值是T, 那么我们的目标是找到
- (A[left] + ... + A[right]) / (right - left + 1) >= T, 且right - left + 1 >= k - 即(A[left]-T) + ... + (A[right]-T) >= 0
- 换句话说, 对于一个T, 把每个元素A[i]减去T得到B[i]
- 希望找到最大的B[left] + ... + B[right] >= 0, 且right - left + 1>= k
- 这可以通过前缀和实现
- 如果找不到这样的(left, right), 说明答案小于Tè二分答案