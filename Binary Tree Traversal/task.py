# Pre-order traversal
def pre_order(node):
    lst = []
    def recurse(node):
        lst.append(node.data)
        if node.left is not None:
            recurse(node.left)
        if node.right is not None:
            recurse(node.right)
    if node is None:
        return []
    recurse(node)
    return lst

# In-order traversal
def in_order(node):
    lst = []
    def recurse(node):
        if node.left is not None:
            recurse(node.left)
        lst.append(node.data)
        if node.right is not None:
            recurse(node.right)
    if node is None:
        return []
    recurse(node)
    return lst

# Post-order traversal
def post_order(node):
    lst = []
    def recurse(node):
        if node.left is not None:
            recurse(node.left)
        if node.right is not None:
            recurse(node.right)
        lst.append(node.data)
    if node is None:
        return []
    recurse(node)
    return lst
