<!-- TOC -->

- [1. Data Structure](#1-data-structure)
- [2. Algorithm](#2-algorithm)
- [3. 动态规划 Dynamic Programming](#3-%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92-dynamic-programming)
- [4. Debug的基本步骤](#4-debug%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%AD%A5%E9%AA%A4)
- [5. 面试](#5-%E9%9D%A2%E8%AF%95)
    - [5.1. 电话面试](#51-%E7%94%B5%E8%AF%9D%E9%9D%A2%E8%AF%95)
    - [5.2. onsite 现场面授](#52-onsite-%E7%8E%B0%E5%9C%BA%E9%9D%A2%E6%8E%88)
    - [5.3. onsite 后](#53-onsite-%E5%90%8E)

<!-- /TOC -->

九章算法基础班+强化班+树状数组线段树+递归+背包+动态规划

# 1. Data Structure
- 数据结构 Heap (双堆)
- 数据结构 Stack (单调栈)
- 数据结构 Array
- 数据结构 Linked List
- 数据结构 Deque
- 数据结构 并查集Union Find   Done
- 数据结构 字典树Trie   Done
- 数据结构 树状数组 
- 数据结构 线段树

# 2. Algorithm
- Binary Search 二分法 (二分, 二分答案)
- Search搜索, BFS, DFS
- 扫描线 Sweep Line
- 递归 Recursion
- 贪心 Greedy
- 分治 Divide & Conquer
- 位运算 bit manipulation

- Follow Up 问题

# 3. 动态规划 Dynamic Programming
    * 背包问题
    * Sliding Array 滚动数组


* 做题的常见误区: 做题获得Accepted就可以了? 看答案抄一遍然后就会了?
* 导致的结果: 做过的题面试中居然还不会; 觉得新题越来越多

* 一题三省: 有哪些类似的题, 他们之间的共通点是什么? 这个题主要考察的是算法思想还是实践能力? 我做题的过程顺利吗, 是否需要再联系一次?
* 如何准备 Follow Up: 定期整理做过的题目, 归类相似问题
    - 题目中哪些条件可以看出这是同类题?
    - 同类题目在思维方式上有什么相似之处?
    - 同类题目在代码实现上有什么相似之处?




# 4. [Debug的基本步骤](http://www.jiuzhang.com/qa/3815/)
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

# 5. 面试

## 5.1. 电话面试
难度 < onsite
- 自我介绍
- 要和面试官保持一个沟通的状态 (Think Loud)
    说出现在的想法和思路
    用例子来clarify题目
- 提前熟悉CodePad, GoogleDoc 等
- 问面试官的问题

## 5.2. onsite 现场面授
1轮一小时, 一天4-7轮, 无轮间休息时间 (上午2-3轮, 午饭, 下午2-3轮, 最后一轮有时是manager, 问问软实力和past expirence)
whiteboard coding, laptop coding, 有时需要编译,运行,通过测试 (实在做不出来, 可以要提示)

- 保持交流
    - 面试者如何表达想法
    - 面试者遇到困难怎么办


## 5.3. onsite 后
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