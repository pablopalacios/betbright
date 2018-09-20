class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    @classmethod
    def make_head(cls):
        head = cls(None, None)
        head.next = head
        head.prev = head
        return head

    def _insert(self, node):
        node.next = self
        node.prev = self.prev
        node.prev.next = node
        self.prev = node

    def push(self, key, value):
        new = Node(key, value)
        self._insert(new)
        return new

    def pop(self):
        last = self.next
        self.next = self.next.next
        self.next.prev = self
        return last

    def move_node_to_start(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._insert(node)

    def __repr__(self):
        return 'Node(%s, %s)' % (self.key, self.value)
