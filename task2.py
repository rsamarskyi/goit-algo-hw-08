class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sum_tree(root):
    """Повертає суму всіх значень у дереві."""
    if root is None:
        return 0

    return root.value + sum_tree(root.left) + sum_tree(root.right)


# Двійкове дерево пошуку:
#        20
#       /  \
#      10   30
#     /  \
#    5   15

root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)

print(sum_tree(root))  # 80
print(sum_tree(None))  # 0