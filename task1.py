class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_min(root):
    """Повертає найменше значення в дереві або None, якщо дерево порожнє."""
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left

    return current.value


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

print(find_min(root))  # 5
print(find_min(None))  # None