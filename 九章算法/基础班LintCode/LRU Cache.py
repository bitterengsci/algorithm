'''
    a linear search TC=O(n)
'''
class LRUCache:

    def __init__(self, capacity):
        self.cache = {}
        self.lru = {}
        self.time = 0
        self.capacity = capacity
        
    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.time
            self.time += 1
            return self.cache[key]
        return -1

    def set(self, key, value):  #  a linear search TC=O(n)
        # if the key is not in current cache
        # remove the oldest key if the capacity is reached
        if key not in self.cache and len(self.cache) >= self.capacity:
            oldest_key = min(self.lru, key=lambda k: self.lru[k])
            self.cache.pop(oldest_key)
            self.lru.pop(oldest_key)
            
        self.cache[key] = value
        self.lru[key] = self.time
        self.time += 1

'''
    use collections.OrderedDict() and try-except
'''
import collections
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value
        
'''
    use collections.OrderedDict() and if-else
    TC=O(1), SC=O(capacity)
'''
from collections import OrderedDict 
class LRUCache: 
    def __init__(self, capacity: int): 
        self.cache = OrderedDict() 
        self.capacity = capacity 
  
    # return the value of the key that is queried in O(1) and return -1 
    # if we don't find the key in out dict / cache. 
    # And also move the key to the end to show that it was recently used. 
    def get(self, key: int) -> int: 
        if key not in self.cache: 
            return -1
        else: 
            self.cache.move_to_end(key) 
            return self.cache[key] 
  
    # Add / update the key by conventional methods. 
    # Move the key to the end to show that it was recently used. 
    # Check whether the length of ordered dictionary has exceeded capacity, 
    # If so remove the first key (least recently used) 
    def set(self, key: int, value: int) -> None: 
        self.cache[key] = value 
        self.cache.move_to_end(key) 
        if len(self.cache) > self.capacity: 
            self.cache.popitem(last = False)

'''
    use collections.OrderedDict() and if-else (more compactß)
    TC=O(1), SC=O(capacity)
'''
from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)

'''
    Hashmap + DoubleLinkedList

    * One advantage of double linked list is that the node can remove itself without other reference. 
    * In addition, it takes constant time to add and remove nodes from the head or tail.
'''
class DLinkedNode(): 
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
            
class LRUCache():
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    def set(self, key, value):
        node = self.cache.get(key)

        if not node: 
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)