from collections import deque
from tree_node import build_sample_tree

def bfs(tree):

    if tree is None:
        return

    q = deque()
    q.append(tree)

    while q:
        node = q.popleft()
        print(node.val)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)



def main():
    tree = build_sample_tree()

    print(f"bfs implementation - ")
    bfs(tree)


if __name__ == '__main__':
    main()