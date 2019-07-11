class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def root_sum(head):
    # time complexity O(V)
    if not head:
        return [0]
    l = root_sum(head.left)
    r = root_sum(head.right)
    return list(map(lambda x:x+head.val, l+r))

def find_max(head):
    # time complexity between O(V*V) and O(V)
    if not head:
        return 0
    return max(max(root_sum(head)), find_max(head.left), find_max(head.right))


if __name__=="__main__":
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    assert find_max(head) == 4, "output {}".format(find_max(head))
    head = Node(-1)
    head.left = Node(2)
    head.right = Node(3)
    assert find_max(head) == 3, "output {}".format(find_max(head))
    head = Node(1)
    head.right = Node(3)
    assert find_max(head) == 4, "output {}".format(find_max(head))
    head = Node(1)
    assert find_max(head) == 1, "output {}".format(find_max(head))

        
