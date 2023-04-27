class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    
def find(node, key):
    if key == node.key:
        return node.key
    elif key < node.key:
        return find(node.left)
    elif key > node.key:
        return find(node.right)

def make_balenced(list_nums, hi= None, lo = 0, parent= None):
    if hi is None:
        hi = len(list_nums) - 1
    if lo > hi:
        return None 

    mid = (lo + hi) // 2

    root = Node(list_nums[mid])
    root.parent = parent
    root.left = make_balenced(list_nums, mid - 1, lo, root)
    root.right = make_balenced(list_nums, hi, mid + 1, root)

    return root

def in_order_traversal(node):
    if node is None:
        return []
    else: 
        return in_order_traversal(node.left) + [node.key] + in_order_traversal(node.right)

def pre_order_traversal(node):
    if node is None:
        return []
    else: 
        return [node.key] + pre_order_traversal(node.left)  + pre_order_traversal(node.right)

def post_order_traversal(node):
    if node is None:
        return []
    else: 
        return post_order_traversal(node.right) + post_order_traversal(node.left) + [node.key]

def display_keys(node, space='\t', level=0):
    
    # If the node is empty
    if node is None:
        print(space*level + 'none')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)    

def find(node, key):
    if node is None:
        return None
    elif node.key == key:
        return node
    elif node.key < key:
        return find(node.right, key)
    elif node.key > key:
        return find(node.left, key)

def insert(node, key):
    if node is None:
        node = Node(key)
    elif node.key < key:
        node.right = insert(node.right, key)
        node.right.parent = node
    elif node.key > key:
        node.left = insert(node.left, key)
        node.left.parent = node
    return node
    

def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
    height = 1 + max(height_l, height_r)
    return balanced, height

node_list = [1,2,3,4,5,6,7, 8]

root_node = make_balenced(node_list)

# display_keys(root_node)

insert(root_node, 100)
root_node = make_balenced(pre_order_traversal(root_node))
insert(root_node, 10)

insert(root_node, 9)

root_node = make_balenced(pre_order_traversal(root_node))

print(is_balanced(root_node))

# display_keys(root_node)





# display_keys(root_node)


# print(in_order_traversal(root_node))

