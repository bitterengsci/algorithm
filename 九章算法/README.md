<!-- TOC -->

- [1. Data Structure](#1-data-structure)
- [2. Algorithm](#2-algorithm)
- [3. 动态规划 Dynamic Programming](#3-%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92-dynamic-programming)
- [4. 位运算 Bit Manipulation](#4-%E4%BD%8D%E8%BF%90%E7%AE%97-bit-manipulation)
- [5. Coding Questions](#5-coding-questions)
    - [5.1. 重点/经典题型](#51-%E9%87%8D%E7%82%B9%E7%BB%8F%E5%85%B8%E9%A2%98%E5%9E%8B)
- [6. Coding Style 代码风格](#6-coding-style-%E4%BB%A3%E7%A0%81%E9%A3%8E%E6%A0%BC)
- [7. 算法, 永远的痛](#7-%E7%AE%97%E6%B3%95-%E6%B0%B8%E8%BF%9C%E7%9A%84%E7%97%9B)
- [8. Debug的基本步骤](#8-debug%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4)
- [9. 面试](#9-%E9%9D%A2%E8%AF%95)
    - [9.1. 电话面试](#91-%E7%94%B5%E8%AF%9D%E9%9D%A2%E8%AF%95)
    - [9.2. onsite 现场面授](#92-onsite-%E7%8E%B0%E5%9C%BA%E9%9D%A2%E6%8E%88)
    - [9.3. onsite 后](#93-onsite-%E5%90%8E)

<!-- /TOC -->

九章算法基础班+强化班+树状数组线段树+递归+背包+动态规划+位运算

TODO:
基础 1 intro
    3 binary tree & divide conquer (重要)
    4 5 BFS DFS   (重要)
    6 linked list, array (重要)
    7 two pointer
    8 heap, stack (重要)

提高 1 7 follow-up
    堆, 单调栈

https://blog.usejournal.com/top-50-dynamic-programming-practice-problems-4208fed71aa3

# 1. [Data Structure](https://github.com/bitterengsci/algorithm/blob/master/九章算法/Data%20Structure.md)
- 数据结构 Heap (双堆)
- 数据结构 Stack (单调栈)
- 数据结构 Array
- 数据结构 Linked List
- 数据结构 Deque             Done
- 数据结构 并查集Union Find   Done
- 数据结构 字典树Trie         Done
- 数据结构 树状数组           Done
- 数据结构 线段树            Done

# 2. [Algorithm](https://github.com/bitterengsci/algorithm/blob/master/九章算法/Algorithm.md)
- Binary Search 二分法 (二分, 二分答案)     Done
- Search搜索, BFS, DFS, dijkstra's algorithm
- 扫描线 Sweep Line             Done
- 递归 Recursion
- 贪心 Greedy
- 分治 Divide & Conquer
- String问题

- Follow Up 问题

# 3. [动态规划 Dynamic Programming](https://github.com/bitterengsci/algorithm/blob/master/九章算法/动态规划.md)
* 坐标型(矩阵)动态规划 10%    (f[x][y], 有坐标信息)
* 接龙型动态规划 20%  
* 划分型动态规划      
* 匹配型动态规划      
* 背包型动态规划      
* 区间型动态规划      
* 树图型动态规划  
* 博弈型动态规划 (游戏, 2人博弈 90%都是DP)

* Sliding Array 滚动数组

# 4. [位运算 Bit Manipulation](https://github.com/bitterengsci/algorithm/blob/master/九章算法/Bit.md)

--- 

# 5. Coding Questions
Lintcode questions associated with .. in .. folder 
    Algorithm.md            基础班LintCode or 强化班LintCode or 递归 or String问题
    Data Structure.md       基础班LintCode or 强化班LintCode or 线段树和树状数组
    动态规划.md              动态规划
    Bit.md                  位运算

Note: Whose name starting with C{num}. in 基础班LintCode are archived. (2019.5一刷九章算法v4.2做的题)

## 5.1. 重点/经典题型
=== 九章算法基础班 ===
- Search a 2D Matrix II

- Median of two Sorted Arrays
- LRU Cache
- Copy List with Random Pointer

=== 九章算法提高班 ===
Need Redo:
- QuickSelect
- K-th largest element in an Array leetcode 215
- Lintcode1396: set union
- Accounts merge
- Lintcode 390. Find Peak Element II
- Find Median from Data Stream
- Sliding Window Median
- Trapping Rain Water II
- Max Tree

再看看:
- LintCode 634: [Word Squares](Done) 
- LintCode 132: [Word Search II](Done)
- Skyline problem

经典题目:
- find peak element

- Count of Smaller Number before itself


--- 

* 做题的常见误区: 做题获得Accepted就可以了? 看答案抄一遍然后就会了?
* 导致的结果: 做过的题面试中居然还不会; 觉得新题越来越多

* 一题三省: 有哪些类似的题, 他们之间的共通点是什么? 这个题主要考察的是算法思想还是实践能力? 我做题的过程顺利吗, 是否需要再联系一次?
* 如何准备 Follow Up: 定期整理做过的题目, 归类相似问题
    - 题目中哪些条件可以看出这是同类题?
    - 同类题目在思维方式上有什么相似之处?
    - 同类题目在代码实现上有什么相似之处?


# 6. Coding Style 代码风格
1. 变量命名 meaningful (循环变量可以用i, j, k, 参数命名要meaningful) 变量命名注意单复数!!!
2. 括号问题  
	C++ for-loop 和 if-clause的statement 哪怕只有一行也要加括号(便于代码之后扩展)
3. 单元运算符不加空格 (i++; return -1; 此处-1是取反)
   双元运算符两边加空格 (+ - == = < > || && ; ,)

4. * bug-free * 想清楚在写
	参数不符合要求,  非法   (Object == None, null ...)
	数值访问越界, 检查下标
5. 嵌套很多层(超过3个缩进),  考虑使用子函数    

New Grad一般问两道题, Experience问一道

面试官眼中的求职者
- 你可能是他未来的同事!!!
- 你的代码看起来舒服么? TA需要多少时间来Review你的代码?
	- 程序风格 Coding Style
	- 变量名命名(注意单复数区别), 缩进, 括号
- 你的Coding习惯好么? 你会不会动不动就搞挂网站, 􏰀成损失?
	- Coding习惯, Bug Free
	- 异常检测, 边界处理
	- 测试自己代码的意识(提供测试数据)
- 和你交流舒服么?
	- 是不是很难和你合作
	- 闷头就开始写 VS 每写一句话就BB半天(容易时间不够。一般题写不完肯定过不了。)
	     (要先交流, 到底要求实现到什么程度。“这个题, 暴力的方法是XX” 先问问行不行。不是说暴力算法一定不行)
	      (先问问想的方法行不行, 可以的话再写, 不要闷头开始写。) -> 和coworker达成共识在开始做

# 7. 算法, 永远的痛
- 题做了很多, 但就是记不住解法
- 从来就没有弄明白过动态规划是怎么回事
- 这题好像见过, 不过还是不知道怎么做
- lintcode, cc150都刷了, 新题还是跪
- 网上的解答那么多, 到底哪个是对的?
- 一定要答出O(n)的方法么? O(nlogn)的可以么? 
- 到底刷到什么程度去面试才够?   (submission per problem 3以内就还行) 刷题,也需要总结!

面试算法, 其实很简单
- 某位商学院转行的小伙伴在我们的帮助下, 花了30天从0基础算法搞定常见算法, 最后拿到Google Facebook等一流公司Offer
- 主要经验: 在刷题时, 总结、归类相似题目 (很多算法都不考, 知识点范围很窄), 找出适合同一类题目的模板程序

Ladder 180题

1. 别做难题,不要花时间攻关难题 (把时间花在如何做到 BUG FREE和如何提高编程程度上, 多做LintCode上 Medium 难度的题
2. 是面试不是考试 和面试官愉快交流, 一起合作解决面试问题 (证明自己牛逼, 但别去证明面试官傻逼)
3. 理解而不是单纯的背诵 (在课程中主要学习的是思维方式和分析技巧而不是某个题的解法)
4. 刀要用在刀刃上 不要把时间浪费在那些基本不会考你又很心虚的内容 (比如KMP, 红黑树, AVL, ACM竞赛题)


# 8. [Debug的基本步骤](http://www.jiuzhang.com/qa/3815/)
为什么Debug一定要靠自己？
- 如果是别人给你指出你的程序哪儿错了, 你自己不会有任何收获, 你下一次依旧会犯同样的错误
- 经过长时间努力Debug获得的错误, 印象更深刻
- Debug能力是面试的考察范围
- 锻炼Debug能力能够提高自己的Bug Free的能力

Debug的基本步骤
- 重新读一遍程序。按照自己当初想的思路, 走一遍程序, 看看程序是不是按照自己的思路在走。（因为很多时候, 你写着写着就忘了很多事儿）这种方式是最有效最快速的Debug方式
- 找到一个非常小非常小的可以让你的程序出错的数据。比如空数组, 空串, 1-5个数的数组, 一个字符的字符串
- 在程序的若干位置输出一些中间结果。比如排序之后输出一下, 看看是不是真的按照你所想的顺序排序的。这样可以定位到程序出错的部分
- 定位了出错的部分之后, 查看自己的程序该部分的逻辑是否有错
- 在第4步中, 如果无法通过肉眼看出错误的部分, 就一步步“模拟执行”程序, 找出错误

实在Debug不出来怎么办？
- 如果你已经Debug了一整天, 可以考虑向他人求助

# 9. 面试

## 9.1. 电话面试
难度 < onsite
- 自我介绍
- 要和面试官保持一个沟通的状态 (Think Loud)
    说出现在的想法和思路
    用例子来clarify题目
- 提前熟悉CodePad, GoogleDoc 等
- 问面试官的问题

## 9.2. onsite 现场面授
1轮一小时, 一天4-7轮, 无轮间休息时间 (上午2-3轮, 午饭, 下午2-3轮, 最后一轮有时是manager, 问问软实力和past expirence)
whiteboard coding, laptop coding, 有时需要编译,运行,通过测试 (实在做不出来, 可以要提示)

- 保持交流
    - 面试者如何表达想法
    - 面试者遇到困难怎么办


## 9.3. onsite 后
- 没offer (问原因)

- 有offer
    - 约时间谈包裹 (谈判不要超过2轮)
        - 准备其他包裹细节 (以及现在工作的待遇)
            - 基本工资
            - bonus (target 15%..)
            - signon bonus 签字费
            - stock/option (vest细节)
            - relocation fee 搬家费

        - match (competing offer)
    - background check

Reference: Draw Diagram https://support.typora.io/Draw-Diagrams-With-Markdown/


# 考察列表
| Data Structure & alg | big company freq | other company freq | difficulty | # QNs to master | return/cost |
|--------|------------------|--------------------|------------|-----------------------|-------------|
| String, Simulation   | `high` | high | low | 20~50 | medium |
| Binary Search        | `high` | high | Medium | 10~20 | `high` |
| Binary Tree, BST     | `high` | high | low | 20~30 | `high` |
| Linked List          | `high` | high | low | 20~30 | `high` |
| Recursion, DFS       | `high` | High | High | 20~40 | Medium |
| BFS                  | `high` | High | Medium | 5~10 | Super `high` |
| Heap (Priority Queue)| Low | Low | Medium | 5~10 | Medium |
| Hash Table           | `high` | high | Medium | 10~30 | `high` |
| Binary Indexed Tree  | Low | Never | Medium | 2~3 | Medium |
| Two Pointers         | `high` | High | Medium | 10~20 | `high` |
| Dynamic Programming  | Medium | Low | High | 40~60 | Low |
| Trie                 | Medium | Low  | Low | 2~5 | `high` |
| Union & Find         | Low | Never | Low | 2~5 | `high` |

String, Simulation: self-learn, more practice, focus on simplifying one question gradually
* Important Algorithms:
  * Super High: Topological Sorting, Simulation
  * High: Dynamic Programming
  * Medium: Trie, Union Find, External Sorting (外排序, 多路归并), Greedy, Binary Index Tree, Heap
  * Low: Dijkstra/Floyd/SPFA (最短路算法), Morris算法 (O(1)额外空间前序遍历), Manacher算法 (求最长回文子串), KMP算法 (strstr/indexOf), Minimum Spanning tree(最小生成树 Prim, Kruskal), Network Flow (网络流), Shell Sort, Segment Tree, BST (平衡排序二叉树 e.g. Red-Black Tree), KD Tree, B-Tree/B+ Tree

* Important Data Structures:
  * High: Binary Tree, Linked List, Array, Stack
  * Medium: Heap (Priority Queue), Union Find, Trie
  * Low: Binary Index Trie, Hash Map, Deque, Monotone Stack

