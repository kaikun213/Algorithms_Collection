# unfinished

# Problem: How can we compress a message, such that we use least bits to transfer but still can decode it uniquely
# Approach: Given a list of frequencies we can construct a binary tree which gives a non-fixed length, optimal binary representation for each frequency
#           Such that the sum of all bit-representation*frequency is minimal in total.

# Solution: Construct a binary tree in a greedy fashion, given a list of frequencies:
#                  1)  Use the smallest two frequencies of the list and build a tree component, add the sum of them to the list (root).
#                  2)  Continue until no element is left in the list (last constructed is the root of largest elements)
# => The leafes of the tree correspond to the given frequencies and the paths are the encoded binary representation

def huffman_encoding(frequency_list):
    # sort frequencies
    heap_freq_list = Heap()
    heap_freq_list.insert_array(frequency_list)

    # build frequency tree
    tree = build_tree(heap_freq_list)
    # traverse tree to give back frequency representation

    return



def build_tree(heap):
    tree = Tree()
    subtrees = list()
    while(heap.length() > 1):
        first = heap_freq_list.extract_min()
        second = heap_freq_list.extract_min()
        # merge both to new root
        root = first + second
        heap.insert(root)
        subtree = Tree()
        subtree.insert_node(root)
        subtree.insert(first)
        subtree.insert(second)
        subtrees.
        subtrees.append(subtree)



# merge two given trees by taking the sum of their roots and combining them. Only for huffman encoding purpose
def merge(tree1, tree2):
    # merge empty tree
    if tree1.root() is None or tree2.root() is None:
        return None
    # merge two trees
    else:
        root = Node(tree1.root().data + tree2.root().data)
        if (tree1.root().data < tree2.root().data):
            root.left = tree1.root()
            root.right = tree2.root()
        else:
            root.left = tree2.root()
            root.right = tree1.root()
    return BinaryTree(root)
