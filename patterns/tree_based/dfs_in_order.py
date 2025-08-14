from tree_node import build_sample_tree

tree = build_sample_tree()

def in_order(tree):
    stack = []
    node = tree

    while stack or node:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        print(node.val)
        node = node.right


def in_order_rec(tree):

    node = tree
    if node is not None:
        in_order_rec(node.left)
        print(node.val)
        in_order_rec(node.right)


def main():
        tree = build_sample_tree()

        print(f"in_order - ")
        in_order(tree)
        print(f"\nin_order_rec(tree) -")
        in_order_rec(tree)


if __name__ == '__main__':
        main()