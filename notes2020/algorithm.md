<!-- TOC -->

- [1. 算法之美](#1-算法之美)
- [2. 九章算法班](#2-九章算法班)
    - [2.1.](#21)
- [3. 九章算法提高班](#3-九章算法提高班)
- [4. Interview Preparation](#4-interview-preparation)
    - [4.1. several sentences self-introduction](#41-several-sentences-self-introduction)
    - [4.2. Question for interviewer:](#42-question-for-interviewer)
    - [4.3. Coding Interview](#43-coding-interview)
        - [4.3.1. Example: How to: Work at Google — Example Coding/Engineering Interview](#431-example-how-to-work-at-google--example-codingengineering-interview)
    - [4.4. Research Interview](#44-research-interview)

<!-- /TOC -->

# 1. 算法之美
```list
## 1.1. (3, 4) Complexity (Time & Space)
## 1.2. (5) Array
## 1.3. (6, 7) Linked List
## 1.4. (8) Stack
## 1.5. (9) Queue
## 1.6. (10) Recursion
## 1.7. (11, 12) Sorting
## 1.8. (13) Linear Sort??
## 1.9. (14) Sorting Optimization
## 1.10. (15, 16) Binary Search
## 1.11. (17) Jump
## 1.12. (18, 19, 20) Hash Table
## 1.13. (21, 22) Hash Algorithm
## 1.14. (23, 24) Binary Tree
## 1.15. (25, 26) Red Black Tree
## 1.16. (27) Recursion Tree
## 1.17. (28, 29) Heap & heap Sort & Heap application
## 1.18. (30) Graph
## 1.19. (31) BFS & DFS
## 1.20. (32, 33, 34) String Matching: Brute Force & Rabin-Karp Algorithm
http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html

https://www.cnblogs.com/gaochundong/p/string_matching.html

## 1.21. (35) Trie
## 1.22. (36) AC
## 1.23. (37) Greedy Algorithm
## 1.24. (38) Divide-Conquer
## 1.25. (39) Back-Tracking
## 1.26. (40, 41, 42) Dynamic Programming
## 1.27. (43) Topology Sorting
## 1.28. (44) Minimum Distance
## 1.29. (45) Bitmap
## 1.30. (46) Probablistic Statistics
## 1.31. (47) Vector Space
## 1.32. (48) B+ tree
## 1.33. (49) Searching
## 1.34. (50) Indexing
## 1.35. (51) Parallel Algorithm
## 1.36. (52) ...
```

# 2. 九章算法班

考察列表
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


## 2.1.  




# 3. 九章算法提高班

---

*The above is for Coding (DS & Alg) interview. DS & Alg & performance, complexity, memory consumption.*

---

# 4. Interview Preparation

## 4.1. several sentences self-introduction

## 4.2. Question for interviewer:


## 4.3. Coding Interview
- DS & Alg & performance, complexity, memory consumption
- medium-level, no much time on hard level
- also machine learning theory (what is SVM, assumption for Naive Baye classifiers)

### 4.3.1. Example: [How to: Work at Google — Example Coding/Engineering Interview](https://www.youtube.com/watch?v=wwIysnVmAUg&feature=youtu.be)
* rephrase the question, clarify the expected return (type..)
* how inputs are given? (in memory? array? sorted? empty/null?)
    - repeating elements?
    - numbers (integer/float? positive/negative?)
* Solution 1: Brute Force solution (quadrative solution $n^2$, time-consuming, not efficient)
* Solution 2: faster one ($nlogn$) binary search in a sorted list
* Solution 3: unidirectional --> bidirational Two Pointers (linear solution $n$)
* Write Code
    - return? (Discuss..)
    - name the function meaningfully, Python use ... style ()
    - becare underflow/overflow (when subtraction/addition)
* Wrench/Follow-Ups: sorted --> unsorted
    - sort it first ($nlogn$)
    - hashset/hashtable
    - becare with repeating elements
* Test: go through code to test
    - test edge cases (empty/null/negative/repeating/unsorted/reverse sorted...)
    - test given examples (if none, make one yourself)
* Large input
    - fit in memory? range/type of value limited?
    - process in chunks
    - could assume some hashset inside the function can be fit into memory (ask interviewer..)
* Summary:
    - Ask for clarification (write down what you discussed)
    - Think out Loud constantly, before write down solution
    - Think anything before writing down
    - Test it with examples or make one yourself
    - Think about edge cases

## 4.4. Research Interview
- introduce 1-2 past projects
- creativiity, problem-solving skills.
- experience & goal
- discuss about CV, previous experience
- For research interview you just need to know YOUR previous research works and your plans/ideas for future
- similar to research internship
- personality questions: how to solve conflict
- google the interviewer first


---
