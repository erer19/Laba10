class QNode:
    def __init__(self, value, next=None):
        self.node = value
        self.next = next

def tree_by_levels(node):
    if node is None:
        return []
    lst = []
    cur = QNode(node)
    last = cur
    while True:
        lst.append(cur.node.value)
        if cur.node.left is not None:
            last.next = QNode(cur.node.left)
            last = last.next
        if cur.node.right is not None:
            last.next = QNode(cur.node.right)
            last = last.next
        if cur.next is None:
            break
        cur = cur.next
    return lst
