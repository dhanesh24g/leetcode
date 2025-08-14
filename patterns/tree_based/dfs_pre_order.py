from tree_node import build_sample_tree

def pre_order(tree):

    stack = []

    stack.append(tree)

    while stack:
        node = stack.pop()

        if node is not None:
            print(node.val)
            stack.append(node.right)
            stack.append(node.left)


def pre_order_rec(tree):

    if tree is not None:
        print(tree.val)
        pre_order_rec(tree.left)
        pre_order_rec(tree.right)


def main():
    tree = build_sample_tree()

    print(f"pre_order - ")
    pre_order(tree)
    print(f"\npre_order_rec(tree) -")
    pre_order_rec(tree)


if __name__ == '__main__':
    main()