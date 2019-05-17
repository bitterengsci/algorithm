
```Python

```
库函数实现题
C strstr() Java indexOf() Python find()


#### Coding Style 代码风格
1. 变量命名 meaningful (循环变量可以用i,j,k, 参数命名要meaningful)
2. 括号问题  
	C++ for-loop 和 if-clause的statement 哪怕只有一行也要加括号(便于代码之后扩展)
3. 单元运算符不加空格 (i++; return -1; 此处-1是取反)
   双元运算符两边加空格 (+ - == = < > || && ; ,)

4. * bug-free * 想清楚在写
	参数不符合要求， 非法   (Object == None, null ...)
	数值访问越界, 检查下标
5. 嵌套很多层(超过3个缩进)， 考虑使用子函数    

New Grad一般问两道题, Experience问一道

#### 面试官眼中的求职者
- 你可能是他未来的同事!!!
- 你的代码看起来舒服么?TA需要多少时间来Review你的代码?
	- 程序风格 Coding Style
	- 变量名命名，缩紧，括号
- 你的Coding习惯好么?你会不会动不动就搞挂网站，􏰀成损失?
	- Coding习惯，Bug Free
	- 异常检测，边界处理
	- 测试自己代码的意识(提供测试数据)
- 和你交流舒服么?
	- 是不是很难和你合作
	- 闷头就开始写 VS 每写一句话就BB半天(容易时间不够。一般题写不完肯定过不了。)
		(要先交流, 到底要求实现到什么程度。“这个题, 暴力的方法是XX” 先问问行不行。不是说暴力算法一定不行。)
		(先问问想的方法行不行, 可以的话再写，不要闷头开始写。) -> 和coworker达成共识在开始做

#### 算法，永远的痛
- 题做了很多，但就是记不住解法
- 从来就没有弄明白过动态规划是怎么回事
- 这题好像见过，不过还是不知道怎么做
- lintcode, cc150都刷了，新题还是跪
- 网上的解答那么多，到底哪个是对的?
- 一定要答出O(n)的方法么?O(nlogn)的可以么? 
- 到底刷到什么程度去面试才够?   (submission per problem 3以内就还行) 刷题,也需要总结!

#### 面试算法，其实很简单
- 某位商学院转行的小伙伴在我们的帮助下
	- 花了30天从0基础算法搞定常见算法
	- 最后拿到Google Facebook等一流公司Offer
- 主要经验
	- 在刷题时，总结、归类相似题目 (很多算法都不考，知识点范围很窄)
	- 找出适合同一类题目的模板程序

Ladder 180


#### 全子集问题 Subsets
17. Subsets
Description: Given a set of distinct integers, return all possible subsets.
- Elements in a subset must be in non-descending order.
- The solution set must not contain duplicate subsets.

Example
Example 1:
Input: [0]
Output:
[
  [],
  [0]
]
Example 2:
Input: [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
Challenge: Can you do it in both recursively and iteratively?
算法: DFS (深度优先搜索)

recursion = 递归 (两种理解: 算法-- DFS; 程序的实现方式--函数自己调用了自己)
backtracking = 回溯法


#### ~
1. 别做难题,不要花时间攻关难题 (把时间花在如何做到 BUG FREE和如何提高编程􏰀度上 多做 LintCode 上 Medium 难度的题
2. 是面试不是考试 和面试官愉快交流，一起合作解决面试问题 (证明自己牛逼，但别去证明面试官傻逼
3. 理解而不是单纯的背诵 (在课程中主要学习的是思维方式和分析技巧而不是某个题的解法)
4. 刀要用在刀刃上 不要把时间浪费在那些基本不会考你又很心虚的内容 (比如KMP，红黑树，AVL，ACM竞赛题


Reference:
[Draw Diagram](https://support.typora.io/Draw-Diagrams-With-Markdown/)