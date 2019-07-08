#-*-coding:utf-8-*-
import collections
'''
Description
    Given an directed graph, a topological order of the graph nodes is defined as follow:

    For each directed edge A -> B in graph, A must before B in the order list.
    The first node in the order can be any node in the graph with no nodes direct to it.
    Find any topological order for the given graph.
Challenge
    Can you do it in both BFS and DFS?
'''
# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        start_node = self.startNode(graph)
        if start_node is None:
            return []

        queue = [start_node]

        topologicalOrder = list()
        order = list()

        order.append(start_node)
        topologicalOrder.append(start_node.label)

        while queue:
            n = queue.pop(0)               # BFS
            # n = queue.pop(-1)            # DFS

            if n.label not in topologicalOrder:
                topologicalOrder.append(n.label)
            if n not in order:
                order.append(n)
            queue += n.neighbors

        print(topologicalOrder)
        return order

    def startNode(self, graph):

        queue = [graph[0]]
        inDegreeZeroNode = [graph[0]]
        while queue:
            node = queue.pop(0)
            queue += node.neighbors
            for item in node.neighbors:
                if item in inDegreeZeroNode:
                    inDegreeZeroNode.remove(item)

        if inDegreeZeroNode == []:
            return None
        else:
            return inDegreeZeroNode[0]

    '''''''''''''''
        BFS 
    '''''''''''''''
    def topSort2(self, graph):
        node_to_indegree = self.get_indegree(graph)

        order = []
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        queue = collections.deque(start_nodes)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order

    def get_indegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}        # create a dict[node] = its indegree

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1

        return node_to_indegree


n0 = DirectedGraphNode(0)
n1 = DirectedGraphNode(1)
n2 = DirectedGraphNode(2)
n3 = DirectedGraphNode(3)
n4 = DirectedGraphNode(4)
n5 = DirectedGraphNode(5)
n0.neighbors = [n1, n2, n3]
n1.neighbors = [n4]
n2.neighbors = [n4, n5]
n3.neighbors = [n4, n5]


s = Solution()
print(s.topSort([n0, n1, n2, n3, n4, n5]))
print(s.topSort2([n0, n1, n2, n3, n4, n5]))
