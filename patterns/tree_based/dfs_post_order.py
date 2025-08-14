from tree_node import build_sample_tree


def post_order_rec(tree):

    if tree is not None:
        post_order_rec(tree.left)
        post_order_rec(tree.right)
        print(tree.val)


def main():
    tree = build_sample_tree()

    print(f"\npost_order_rec(tree) -")
    post_order_rec(tree)


if __name__ == '__main__':
    main()