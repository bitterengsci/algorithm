<!-- TOC -->

- [1. Deque 双端队列](#1-deque-%E5%8F%8C%E7%AB%AF%E9%98%9F%E5%88%97)
- [2. 并查集 Union Find 集合的合并查找操作,并查集](#2-%E5%B9%B6%E6%9F%A5%E9%9B%86-union-find-%E9%9B%86%E5%90%88%E7%9A%84%E5%90%88%E5%B9%B6%E6%9F%A5%E6%89%BE%E6%93%8D%E4%BD%9C%E5%B9%B6%E6%9F%A5%E9%9B%86)
- [3. 字典树Trie, Prefix Tree 前缀树](#3-%E5%AD%97%E5%85%B8%E6%A0%91trie-prefix-tree-%E5%89%8D%E7%BC%80%E6%A0%91)
    - [3.1. Trie用于剪枝](#31-trie%E7%94%A8%E4%BA%8E%E5%89%AA%E6%9E%9D)
    - [3.2. Typeahead Trie 在系统设计中的运用 (实际运用)](#32-typeahead-trie-%E5%9C%A8%E7%B3%BB%E7%BB%9F%E8%AE%BE%E8%AE%A1%E4%B8%AD%E7%9A%84%E8%BF%90%E7%94%A8-%E5%AE%9E%E9%99%85%E8%BF%90%E7%94%A8)

<!-- /TOC -->
- 数据结构 Heap (双堆)
- 数据结构 Stack (单调栈)
- 数据结构 Array
- 数据结构 Linked List
- 数据结构 Deque
- 数据结构 并查集Union Find   Done
- 数据结构 字典树Trie   Done
- 数据结构 树状数组 
- 数据结构 线段树

数据结构的适用范围(可以解决什么问题), 没有一个DS/Alg是万能的, 都有使用范围



# 1. Deque 双端队列
维护一个候选可能(窗口)的最大值集合 (队首pop, 队尾insert)
类似单调栈, 但两端都有操作 (两端都会有push和pop)

LintCode 362: [Sliding Window Maximum]() 滑动窗口经典题型
给定一个数组A, 找到其中每个大小为k的窗口中最大值   
输入: [1, 2, 7, 7, 8], k = 3  输出: [7, 7, 8]
* Soln 1: O(nk)
* Soln 2: 堆/优先队列 (通过将新元素加入堆, 将旧元素从堆中删除, 可以使用堆达成nlogk的复杂度的算法, 但由于priority queue无法在O(logk)的时间复杂度内删除一个特定元素, 因此需要自己实现一个堆)
    - 基本思想: 如果A[i]<=A[j], 且i < j, A[i]永远不会成为之后的窗口最大值
    - 窗口向右移动, 左端元素移出队首(如果仍在队列中), 右端元素A[j]移进队尾, 并删除所有小于等于A[j]的A[i]
    TC=O(N), 每个元素只会进一次deque



# 2. 并查集 Union Find 集合的合并查找操作,并查集
一种用于支持集合(一堆元素形成的整体)快速合并和查找操作的数据结构
* Union 合并(两个集合取并)两个集合 O(1)
* Find 查询元素所属集合 O(1)  给定单个元素, 求所属集合
 
* 应用:
    公司并购 —— 合并两个集合
    查询子公司所在集团 —— 查询所在集合 判断两个子公司是否在同一家集团
* Union Find 是一棵多叉树
    - 根节点
    - 子节点指向父节点
    - 合并: 让一个并查集的根节点指向另一个并查集的根节点
 
实现 Union Find 
* 底层数据结构
    - 父亲表示法, 用一个数组/哈希表记录每个节点的父亲是谁。
    - father[“Nokia”] = “Microsoft”
    - father[“Instagram”] = “Facebook”
* 查询所在集合
    - 用所在集合最顶层的根节点来代表这个集合 
* 合并两个集合
    - 找到两个集合中最顶层的两个根节点 A 和 B
    - father[A] = B OR father[B] = A (如果无所谓谁合并谁的话)
   
初始化
* 使用哈希表或者数组来存储每个节点的父亲节点 
* 如果节点不是连续整数的话,就最好用哈希表来存储 
* 最开始所有的父亲节点都指向自己 (或者指向None/-1)

查找根 
* 沿着父亲节点一路往上走就能找到根
* path compression路径压缩: 在找到根以后,还需要把一路上经过的点都指向根
```
    A -> B -> C -> D    路径压缩后: E -> B -> D     (没有经过E, 故E仍指向B)
    E -> B                              A -> D
                                        C -> D  
```

假设有n个元素,每个元素分别属于某个集合,并且使用并查集来存储这些信息。不带路径压缩的并查集和带路径压缩的并查集,合并两个集合的平均时间复杂度? O(n), O(1)
使用路径压缩的并查集会在find()时将所有经过的元素全部指向根节点, 因此平均时间复杂度可以优化至O(1)

集合合并 
* 找到两个元素所在集合的两个根 A 和 B
* 将其中一个根的父指针指向另外一个根
```python
def __init__():
    f = {}
    for n in nodes:
        f[n] = n  # f[i]: parent/fater of i

def find(x: int, f: dict):
    while f[x] != x: # while不会死循环, UF中没有cycle
        x = f[x]
    return x
# Problem: 高度H, 最差为n TC=O(n) --> path compression

# path compression I
def find(x: int, f: dict):
    root = x
    while f[root] != root: 
        root = f[root]

    # 重走这条路
    while x != root:
        temp = f[root] # 缓存之前的父亲
        f[x] = root  # 指向根节点
        x = temp
        # 或者 x, f[x] = f[x], root

    return root     # return 根节点

# path compression II
def find(node, father):
    path = []
    while node != father[node]:
        path.append(node)
        node = father[node]
    
    for n in path:
        father[n] = node
    return node

def union(x, y, f):
    fx = find(x, f)
    fy = find(y, f)
    if fx != fy:
        f[fx] = fy  # OR f[fy] = fx
```
* 时间复杂度都是O(log* n) 约等于O(1)    O(n) --路径压缩-->> ≈O(1)
    - log* n --> log2log2log2...n until log*n <=1
    -   | x                    | $ log^{*}n $ |
        |----------------------|--------------|
        | (-∞, 1]              | 0            |
        | (1, 2]               | 1            |
        | (2, 4]               | 2            |
        | (4, 16]              | 3            |
        | (16, 65536]          | 4            |
        | (65536, $2^{65536}$] | 5            |
    - Proof of O(log*n) time complexity of union–find: https://en.wikipedia.org/wiki/Proof_of_O(log*n)_time_complexity_of_union–find
    - Iterated Logarithm: https://en.wikipedia.org/wiki/Iterated_logarithm

* Compression by Rank 按照集合大小压缩? 始终让小集合的根节点指向大集合 TC=O(logn)
    - 一条边的存在 = 父亲的子树大小至少为当前子树大小2倍
    - 高度最多logn

将多叉树的大小存在并查集的哪个节点比较方便? 只有根节点的信息容易查询, 因为当合集合并后,我们只能找到这个合集的根节点。因此最好将集合的信息存在根节点中。
 
LintCode 589: [Connecting Graph]()=实现并查集, 联通分量 skipped this question. No lintcode permission
给定n个图中的节点,一开始节点之间没有边。需要支持操作: connect(a,b) 连接a点和b点       query(a,b) 询问a点和b点是否在图中连通
Example:
    n=5
    query(1, 2) 输出 false 
    connect(1, 2) 
    query(1, 3) 输出 false 
    connect(2, 4) 
    query(1, 4) 输出 true

使用并查集,每次对于a和b,找到各自的根节点A和B,其中需要路径压缩
如果A不等于B,将A树指向B树

LintCode 590: [Connecting Graph II]() skipped this question. No lintcode permission
给定n个图中的节点,一开始节点之间没有边。需要支持操作: connect(a,b), 连接a点和b点     query(a), 询问a点所在连通块的节点个数 (一个集合多大)
Example:
    n=5
    query(1) 输出 1 
    connect(1, 2) query(1) 输出 2 
    connect(2, 4) query(1) 输出 3
使用并查集,每次对于a和b,找到各自的根节点A和B,其中进行路径压缩
根节点记录下自己的子树的节点个数 如果A不等于B,将A树指向B树。B树根节点更新节点个数 
FollowUp: 每个点有权值,问A点所在连通块的权值总和/最大权值  (更新时, sum or max)

在求集合所有元素平均值时, 哪个信息是必须存入根节点的? 集合内元素个数。若只存集合内平均值,两个元素合并时,并不能求出新集合的平均值。只存所有元素之和同样无法求出平均值。但是如果存了集合内平均值以及集合内元素个数,则可以通过计算出两个集合所有元素之和,再除以两个集合元素个数来求两个集合合并后的平均值。存集合所有元素之和以及集合内元素个数同理。因此,无论是存集合内元素之和还是平均值,都需要存集合内元素个数。

LintCode 591: [Connecting Graph III](https://github.com/bitterengsci/algorithm/blob/master/九章算法/强化班LintCode/Connecting%20Graph%20III.py)
给定n个图中的节点,一开始节点之间没有边。需要支持操作: connect(a,b), 连接a点和b点 query() 询问连通块数目 (集合数目, 有几个根节点)
使用并查集,每次对于a和b,找到各自的根节点A和B,其中进行路径压缩
如果A不等于B,将A树指向B树。连通块数目减1 FollowUp:每个点有权值,问当前所有连通块的最大平均权值

LintCode 434: [Number of Islands II](https://github.com/bitterengsci/algorithm/blob/master/九章算法/强化班LintCode/Number%20of%20Islands%20II.py)
给定一个mxn矩阵,一开始每个格子都是大海(一开始岛屿=0)
给定一些格子要依次改成岛屿,需要返回每次一个格子改成岛屿后,当前连通岛屿的个数 (上下左右联通)
并查集在二维中的拓展(矩阵其实也是图),每个格子作为一个节点。当一个格子变成岛屿,和它的四个邻居依次连接,相当于在图中加四条边

给定n*m的矩阵, 要将k个格子改成岛屿, 那么时间复杂度是多少? O(k) = k log*n。每次将格子变成岛屿时, 只需要做四次加边的操作, 每次加边的复杂度是O(1)。因为只需要将k个格子变成岛屿,因此总时间复杂度是O(k)

LintCode 178: [Graph Valid Tree](https://github.com/bitterengsci/algorithm/blob/master/九章算法/强化班LintCode/Graph%20Valid%20Tree.py)
给定n个节点和一些无向边,判断是否形成一棵树。
树的边数一定是n-1, 并且形成一个连通块(无环)。但边数为n-1不一定为树
使用并查集,将所有边加入
形成树的两个条件: n-1条边, 最后只有一个连通块 
   
LintCode 1070: [Accounts Merge]() 不会!! 需要再看看！！ skipped this question.
给定一些账户,每个账户有一个用户名和一些关联邮箱。如果两个账户含有相同的关联邮箱,则这两个账户同属于一个人。不同的人可能有相同的用户名。输出合并后的账户,一个人一个账户。
输入: accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
输出: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
* Soln 1: 将每个原始账户作为一个node,但是两个账户可以连接取决于它们共享至少一个邮箱,处理起来比较麻烦
    - 两两处理, 但 可能叫John的人很多; 可能一个John有很多邮箱
* Soln 2: 将每个邮箱作为一个node(用hashset储存; 每个节点存储parent和account name信息), 同一个原始账户中的邮箱之间连边。用根节点存储用户名  TC=O(n), n个邮箱
* 灵活定义并查集的节点

LintCode 1396: [Set Union]()  不会!! 需要再看看！！ skipped this question.

LintCode 805: [Maximum Association Set](https://github.com/bitterengsci/algorithm/blob/master/九章算法/强化班LintCode/Maximum%20Association%20Set.py)
类似 Accounts Merge, 只是少了用户名
需要输出最大的连通块。可以在并查集合并过程中打擂台,也可以在最后每个点找一次根节点。
     
跟连通性有关的问题, 都可以使用 BFS(静态连通性) 和 Union Find (动态联通性, i.e. 加边 -> 查询 -> 加边 -> 查询)
什么时候无法使用 Union Find? 需要拆开两个集合的时候无法使用Union Find (UF无法删除边, i.e.集合拆分)
 
并查集总结
- 合并两个集合 + 查询某个元素所在集合 (路径压缩寻找根节点)
- 动态合并集合与查询节点所在集合, 但不能分拆集合
- 判断两个元素是否在同一个集合 
- 获得某个集合的元素个数
- 统计当前集合个数
- 关键操作:快速寻找根节点

# 3. 字典树Trie, Prefix Tree 前缀树
来自单词Retrieval,发音与Tree相同, 用于处理字符串
Trie的考点: 实现一个Trie; 比较Trie和Hash的优劣 (字符矩阵类问题使用Trie更高效)

LintCode 442: [Implement Trie (Prefix Tree)](https://github.com/bitterengsci/algorithm/blob/master/九章算法/强化班LintCode/Implement%20Trie%20(Prefix%20Tree).py)
假设有[b,abc,abd,bcd,abcd,efg,hii]这7个单词 , 查找abc在不在字典里面
- 若放入hashset, 空间浪费
- Trie一旦分开不在合并 -> 保证trie是一棵树
- Trie树的高度 = 最长字符串 (最长单词的长度)
- 边代表字母; 节点代表从根节点一路走下来形成的字符串 (node存储boolean变量isword)
需要一个新的类TrieNode代表Trie中的节点
Insert 插入一个单词 TC=单词的长度
   
LintCode 473: [Add and Search Word](https://github.com/bitterengsci/algorithm/blob/master/九章算法/强化班LintCode/Add%20and%20Search%20Word.py)
支持两种字符串操作: 
addWord(word): 加入一个词 
search(word): 搜索一个词,其中可能有".", 代表任何单个字符 ("." -> 所有子节点都要尝试 = Recursion)
addWord使用Trie
searchWord在Trie中DFS,一旦需要”.”字符就遍历所有儿子节点: 走到死胡同or找到了到isword=False, return False
 
## 3.1. Trie用于剪枝
LintCode 634: [Word Squares](https://github.com/bitterengsci/algorithm/blob/master/九章算法/强化班LintCode/Word%20Squares.py) 
给出一系列不重复的单词,找出所有用这些单词能构成的单词平方。单词平方是一个k×k的单词方阵: 第k行的单词和第k列的单词相同
输入: ["area", "lead", "wall", "lady", "ball"]
输出:[["wall", "area", "lead", "lady"],["ball", "area", "lead", "lady"]]
限定: 单词个数<=1000, 单词长度在1到5之间
直接搜索,时间复杂度TC=n×(n-1)×(n-2)×(n-3)×(n-4)=n^5, 最高1000^5 
查找冗余/可以剪枝的部分

剪枝一: 第一个词填了ball后, 第二个词必须以a开头; 第二个词填了area后, 第三个词必须以le开头, 以其他开头的就没必要搜下去了
- 用Hash or Trie树记录下以某个前缀开头的有哪些单词
- 比如以l开头的有lead lady, 以le开头的有lead, 以lea开头的有lead
- 每次只用从特定开头的单词中继续往后搜
剪枝二: 第一个词填了ball, 第二个词想填area的话, 字典中必须有以le和la开头的单词, 否则没有的话就不能填area

递归+剪枝的时间复杂度很难分析, TC=n^5, 但在实际中大大快于n^5

LintCode 132: [Word Search II](https://github.com/bitterengsci/algorithm/blob/master/九章算法/强化班LintCode/Word%20Search%20II.py)
给定一个小写字母矩阵和一个字典。找到字典中所有在矩阵中出现的词。一个词可以在矩阵中任意位置开始,然后向上下左右一个方向走一步。一个格子在一个 词里只能用一次。
输入:[“doaf”, “agai”, “dcan”] {"dog", "dad", "dgdg", "can", "again"}
输出: {"dog", "dad", "can", "again"}
用Trie存储字典里所有词
在矩阵中DFS时,在Trie里对应节点向下走
Trie可以帮助剪枝
  
## 3.2. Typeahead Trie 在系统设计中的运用 (实际运用)
字典树Trie
- 合并所有公共的前缀
- 动态插入与查询单词
- 不能查询非前缀(如字符串一部分)

假设共有n只动物, 每次输入[x, y]代表x与y是同种生物。若n=10, 再输入[[1, 2], [3, 4], [6, 8], [4, 6]]后, 在这n只动物中最多有多少种不同生物? 1与2必然是一种生物, 3468必为同种生物, 而5,7,9,10号动物可能互不相同,因此最多有6种生物

有n个平均长度为k的字符串, 若要构造一个字典树trie并将这些字符串依次插入字典树, 总时间复杂度是多少? 每次将长度为k的字符插入trie中的复杂度是O(k), 将n个平均长度为k的字符插入字典树的复杂度为O(nk)

字典树的节点总数代表? 
从根节点到某一节点。路径上经过的字符串连接起来,就是该节点对应的子串,由于这样获得的每个子串都是不同的,且每个子串都是某个原字符串的前缀。因此,字典树的节点总数即所有字符串本质不同的前缀个数

"ab" "abc" "adc" "cad" "bad" "bd"中有多少不同的前缀? 可以自己构建一棵Trie, 将所有字符串插入字典树, 数其中有多少节点即可。共有a, ab, abc, ad, adc, b, ba, bad, bd, c, ca, cad 共12个本质不同的前缀。

