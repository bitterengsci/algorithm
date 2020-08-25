import random
MAX_DEPTH = 5

class SkipNode:
    def __init__(self, height = 0, elem = None):
        self.elem = elem
        self.next = [None]*height

    def __repr__(self):
        return str(self.elem)

class SkipList:
    def __init__(self):
        self.head = SkipNode()

    def updateList(self, elem):
        update = [None] * len(self.head.next)
        x = self.head

        for i in reversed(range(len(self.head.next))):
            while x.next[i] != None and \
                    x.next[i].elem < elem:
                x = x.next[i]
            update[i] = x

        return update

    def find(self, elem, update=None):
        if update == None:
            update = self.updateList(elem)
        if len(update) > 0:
            candidate = update[0].next[0]
            if candidate != None and candidate.elem == elem:
                return candidate
        return None

    def insert(self, elem):
        node = SkipNode(self.randomHeight(), elem)
        
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.updateList(elem)
        if self.find(elem, update) == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node

    def randomHeight(self):
        k = 1
        while random.randint(0, 1):
            k = k + 1
            if k == MAX_DEPTH:
                break
        return k

    def remove(self, elem):
        update = self.updateList(elem)
        x = self.find(elem, update)
        if x != None:
            for i in range(len(x.next)):
                update[i].next[i] = x.next[i]
                if self.head.next[i] == None:
                    self.head.next = self.head.next[:i]
                    return

    def show(self):
        for i in reversed(range(len(self.head.next))):
            x = self.head
            line = []
            while x.next[i] != None:
                line.append(str(x.next[i].elem))
                x = x.next[i]
            print('line{}: '.format(i+1) + '->'.join(line))


sl = SkipList()
sl.insert(1)
sl.insert(2)
sl.insert(3)
sl.insert(4)
sl.insert(5)
sl.insert(6)
sl.insert(7)
sl.insert(8)
sl.show()