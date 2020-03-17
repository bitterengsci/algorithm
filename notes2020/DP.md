
<!-- TOC -->

- [1. Dynamic Programming](#1-dynamic-programming)
        - [1.1. Pattern 1. Minimum/Maximum Path to Reach a Target](#11-pattern-1-minimummaximum-path-to-reach-a-target)
        - [1.2. Pattern 2. Distinct Ways](#12-pattern-2-distinct-ways)
        - [1.3. Pattern 3.Merging Intervals](#13-pattern-3merging-intervals)
        - [1.4. Pattern 4.DP on Strings](#14-pattern-4dp-on-strings)
        - [1.5. Pattern 5.Decision Making](#15-pattern-5decision-making)
        - [1.6. Pattern 1. 0/1 Knapsack, 0/1背包，6个题](#16-pattern-1-01-knapsack-01背包6个题)
        - [1.7. Pattern 2. Unbounded Knapsack，无限背包，5个题](#17-pattern-2-unbounded-knapsack无限背包5个题)
        - [1.8. Pattern 3. Fibonacci Numbers，斐波那契数列，6个题](#18-pattern-3-fibonacci-numbers斐波那契数列6个题)
        - [1.9. Pattern 4. Palindromic Subsequence，回文子系列，5个题](#19-pattern-4-palindromic-subsequence回文子系列5个题)
        - [1.10. Pattern 5. Longest Common Substring，最长子字符串系列，13个题](#110-pattern-5-longest-common-substring最长子字符串系列13个题)

<!-- /TOC -->

# 1. Dynamic Programming

动态规划 = 递归加缓存

用DP来解斐波那契数列。通过空间换时间，通过开销额外的空间，去降维时间复杂度

[Reference](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)

### 1.1. Pattern 1. Minimum/Maximum Path to Reach a Target
* **Statement**: Given a target find minimum (maximum) cost/path/sum to reach the target.
* **Approach**: Choose minimum/maximum path among all possible paths before the current state, then add value for the current state.
  ```python
  routes[i] = min(routes[i-1], routes[i-2], ... , routes[i-k]) + cost[i]
  ```
  Generate optimal solutions for all values in the target and return the value for the target.
  ```cpp
  for (int i = 1; i <= target; ++i) {
    for (int j = 0; j < ways.size(); ++j) {
        if (ways[j] <= i) {
            dp[i] = min(dp[i], dp[i - ways[j]]) + cost / path / sum;
        }
    }
  }
  return dp[target]
  ```
* 746. Min Cost Climbing Stairs Easy
  ```cpp
  for (int i = 2; i <= n; ++i) {
    dp[i] = min(dp[i-1], dp[i-2]) + (i == n ? 0 : cost[i]);
  }
  return dp[n]
  ```
* 64. Minimum Path Sum Medium
  ```cpp
  for (int i = 1; i < n; ++i) {
    for (int j = 1; j < m; ++j) {
        grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j];
    }
  }
  return grid[n-1][m-1]
  ```
* 322. Coin Change Medium
  ```cpp
  for (int j = 1; j <= amount; ++j) {
    for (int i = 0; i < coins.size(); ++i) {
        if (coins[i] <= j) {
            dp[j] = min(dp[j], dp[j - coins[i]] + 1);
        }
    }
  }
  ```
```list
931. Minimum Falling Path Sum Medium
983. Minimum Cost For Tickets Medium
650. 2 Keys Keyboard Medium
279. Perfect Squares Medium
1049. Last Stone Weight II Medium
120. Triangle Medium
474. Ones and Zeroes Medium
221. Maximal Square Medium
322. Coin Change Medium
1240. Tiling a Rectangle with the Fewest Squares Hard
174. Dungeon Game Hard
871. Minimum Number of Refueling Stops Hard
```

### 1.2. Pattern 2. Distinct Ways
* **Statement**: Given a target find a number of distinct ways to reach the target.
* **Approach**: Sum all possible ways to reach the current state.
  ```cpp
  routes[i] = routes[i-1] + routes[i-2], ... , + routes[i-k]
  ```
  Generate sum for all values in the target and return the value for the target.
  ```cpp
  for (int i = 1; i <= target; ++i) {
    for (int j = 0; j < ways.size(); ++j) {
        if (ways[j] <= i) {
            dp[i] += dp[i - ways[j]];
        }
    }
  }
  return dp[target]
  ```
* 70. Climbing Stairs easy
  ```cpp
  for (int stair = 2; stair <= n; ++stair) {
    for (int step = 1; step <= 2; ++step) {
        dp[stair] += dp[stair-step];
    }
  }
  ```
* 62. Unique Paths Medium
  ```cpp
  for (int i = 1; i < m; ++i) {
    for (int j = 1; j < n; ++j) {
        dp[i][j] = dp[i][j-1] + dp[i-1][j];
    }
  }
  ```
* 1155. Number of Dice Rolls With Target Sum Medium
  ```cpp
  for (int rep = 1; rep <= d; ++rep) {
    vector<int> new_ways(target+1);
    for (int already = 0; already <= target; ++already) {
        for (int pipe = 1; pipe <= f; ++pipe) {
            if (already - pipe >= 0) {
                new_ways[already] += ways[already - pipe];
                new_ways[already] %= mod;
            }
        }
    }
    ways = new_ways;
  }
  ```
  Note: Some questions point out the number of repetitions, in that case, add one more loop to simulate every repetition.
```list
688. Knight Probability in Chessboard Medium
494. Target Sum Medium
377. Combination Sum IV Medium
935. Knight Dialer Medium
1223. Dice Roll Simulation Medium
416. Partition Equal Subset Sum Medium
808. Soup Servings Medium
790. Domino and Tromino Tiling Medium
801. Minimum Swaps To Make Sequences Increasing
673. Number of Longest Increasing Subsequence Medium
63. Unique Paths II Medium
576. Out of Boundary Paths Medium
1269. Number of Ways to Stay in the Same Place After Some Steps Hard
1220. Count Vowels Permutation Hard
```

### 1.3. Pattern 3.Merging Intervals
* **Statement**: Given a set of numbers find an optimal solution for a problem considering the current number and the best you can get from the left and right sides.
* **Approach**: Find all optimal solutions for every interval and return the best possible answer.
  ```cpp
  // from i to j
  dp[i][j] = dp[i][k] + result[k] + dp[k+1][j]
  ```
  Get the best from the left and right sides and add a solution for the current position.
  ```cpp
  for(int l = 1; l<n; l++) {
    for(int i = 0; i<n-l; i++) {
        int j = i+l;
        for(int k = i; k<j; k++) {
            dp[i][j] = max(dp[i][j], dp[i][k] + result[k] + dp[k+1][j]);
        }
    }
  }
  return dp[0][n-1]
  ```
* 1130. Minimum Cost Tree From Leaf Values Medium
  ```cpp
  for (int l = 1; l < n; ++l) {
    for (int i = 0; i < n - l; ++i) {
        int j = i + l;
        dp[i][j] = INT_MAX;
        for (int k = i; k < j; ++k) {
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + maxs[i][k] * maxs[k+1][j]);
        }
    }
  }
  ```

```list
96. Unique Binary Search Trees Medium
1039. Minimum Score Triangulation of Polygon Medium
546. Remove Boxes Medium
1000. Minimum Cost to Merge Stones Medium
312. Burst Balloons Hard
375. Guess Number Higher or Lower II Medium
```

### 1.4. Pattern 4.DP on Strings
* General problem statement for this pattern can vary but most of the time you are given two strings where lengths of those strings are not big
* **Statement**: Given two strings s1 and s2, return some result.
* **Approach**: Most of the problems on this pattern requires a solution that can be accepted in O(n^2) complexity.
  ```cpp
  // i - indexing string s1
  // j - indexing string s2
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j) {
        if (s1[i-1] == s2[j-1]) {
            dp[i][j] = /*code*/;
        } else {
            dp[i][j] = /*code*/;
        }
    }
  }
  ```
  If you are given one string s the approach may little vary
  ```cpp
  for (int l = 1; l < n; ++l) {
    for (int i = 0; i < n-l; ++i) {
        int j = i + l;
        if (s[i] == s[j]) {
            dp[i][j] = /*code*/;
        } else {
            dp[i][j] = /*code*/;
        }
    }
  }
  ```
1143. Longest Common Subsequence Medium
  ```cpp
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j) {
        if (text1[i-1] == text2[j-1]) {
            dp[i][j] = dp[i-1][j-1] + 1;
        } else {
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
        }
    }
  }
  ```
* 647. Palindromic Substrings Medium
  ```cpp
  for (int l = 1; l < n; ++l) {
    for (int i = 0; i < n-l; ++i) {
        int j = i + l;
        if (s[i] == s[j] && dp[i+1][j-1] == j-i-1) {
            dp[i][j] = dp[i+1][j-1] + 2;
        } else {
            dp[i][j] = 0;
        }
    }
  }
  ```
```list
516. Longest Palindromic Subsequence Medium
1092. Shortest Common Supersequence Medium
72. Edit Distance Hard
115. Distinct Subsequences Hard
712. Minimum ASCII Delete Sum for Two Strings Medium
5. Longest Palindromic Substring Medium
```

### 1.5. Pattern 5.Decision Making
* The general problem statement for this pattern is forgiven situation decide whether to use or not to use the current state. So, the problem requires you to make a decision at a current state.
* **Statement**: Given a set of values find an answer with an option to choose or ignore the current value.
* **Approach**: If you decide to choose the current value use the previous result where the value was ignored; vice-versa, if you decide to ignore the current value use previous result where value was used.
  ```cpp
  // i - indexing a set of values
  // j - options to ignore j values
  for (int i = 1; i < n; ++i) {
    for (int j = 1; j <= k; ++j) {
        dp[i][j] = max({dp[i][j], dp[i-1][j] + arr[i], dp[i-1][j-1]});
        dp[i][j-1] = max({dp[i][j-1], dp[i-1][j-1] + arr[i], arr[i]});
    }
  }
  ```
* 198. House Robber Easy
  ```cpp
  for (int i = 1; i < n; ++i) {
    dp[i][1] = max(dp[i-1][0] + nums[i], dp[i-1][1]);
    dp[i][0] = dp[i-1][1];
  }
  ```
```list
121. Best Time to Buy and Sell Stock Easy
714. Best Time to Buy and Sell Stock with Transaction Fee Medium
309. Best Time to Buy and Sell Stock with Cooldown Medium
123. Best Time to Buy and Sell Stock III Hard
188. Best Time to Buy and Sell Stock IV Hard
```


[Reference](https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews?aff=K7qB)

### 1.6. Pattern 1. 0/1 Knapsack, 0/1背包，6个题
0/1 Knapsack，0/1背包问题
Equal Subset Sum Partition，相等子集划分问题
Subset Sum，子集和问题
Minimum Subset Sum Difference，子集和的最小差问题
Count of Subset Sum，相等子集和的个数问题
Target Sum，寻找目标和的问题

### 1.7. Pattern 2. Unbounded Knapsack，无限背包，5个题
Unbounded Knapsack，无限背包
Rod Cutting，切钢条问题
Coin Change，换硬币问题
Minimum Coin Change，凑齐每个数需要的最少硬币问题
Maximum Ribbon Cut，丝带的最大值切法

### 1.8. Pattern 3. Fibonacci Numbers，斐波那契数列，6个题
Fibonacci numbers，斐波那契数列问题
Staircase，爬楼梯问题
Number factors，分解因子问题
Minimum jumps to reach the end，蛙跳最小步数问题
Minimum jumps with fee，蛙跳带有代价的问题House thief，偷房子问题

### 1.9. Pattern 4. Palindromic Subsequence，回文子系列，5个题
Longest Palindromic Subsequence，最长回文子序列
Longest Palindromic Substring，最长回文子字符串
Count of Palindromic Substrings，最长子字符串的个数问题
Minimum Deletions in a String to make it a Palindrome，
怎么删掉最少字符构成回文Palindromic Partitioning，怎么分配字符，形成回文

### 1.10. Pattern 5. Longest Common Substring，最长子字符串系列，13个题
Longest Common Substring，最长相同子串
Longest Common Subsequence，最长相同子序列
Minimum Deletions & Insertions to Transform a String into another，字符串变换
Longest Increasing Subsequence，最长上升子序列
Maximum Sum Increasing Subsequence，最长上升子序列和
Shortest Common Super-sequence，最短超级子序列
Minimum Deletions to Make a Sequence Sorted，最少删除变换出子序列
Longest Repeating Subsequence，最长重复子序列
Subsequence Pattern Matching，子序列匹配
Longest Bitonic Subsequence，最长字节子序列
Longest Alternating Subsequence，最长交差变换子序列
Edit Distance，编辑距离
Strings Interleaving，交织字符串