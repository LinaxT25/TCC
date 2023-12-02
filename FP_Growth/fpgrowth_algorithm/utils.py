from collections import defaultdict
from itertools import chain, combinations
from Export.DataExport import freq_item_export_csv


class Node:
    def __init__(self, item_name, frequency, parent_node):
        self.item_name = item_name
        self.count = frequency
        self.parent = parent_node
        self.children = {}
        self.next = None

    def increment(self, frequency):
        self.count += frequency

    def display(self, ind=1):
        print('  ' * ind, self.item_name, ' ', self.count)
        for child in list(self.children.values()):
            child.display(ind + 1)


def construct_tree(item_set_list, frequency, min_sup):
    header_table = defaultdict(int)
    # Counting frequency and create header table
    for idx, item_set in enumerate(item_set_list):
        for item in item_set:
            header_table[item] += frequency[idx]

    # Deleting items below minSup
    header_table = dict((item, sup) for item, sup in header_table.items() if sup >= min_sup)
    if len(header_table) == 0:
        return None, None

    # HeaderTable column [Item: [frequency, headNode]]
    for item in header_table:
        header_table[item] = [header_table[item], None]

    # Init Null head node
    fp_tree = Node('Null', 1, None)
    # Update FP tree for each cleaned and sorted item_set
    for idx, item_set in enumerate(item_set_list):
        item_set = [item for item in item_set if item in header_table]
        item_set.sort(key=lambda item: header_table[item][0], reverse=True)
        # Traverse from root to leaf, update tree with given item
        current_node = fp_tree
        for item in item_set:
            current_node = update_tree(item, current_node, header_table, frequency[idx])

    return fp_tree, header_table


def update_header_table(item, target_node, header_table):
    if header_table[item][1] is None:
        header_table[item][1] = target_node
    else:
        current_node = header_table[item][1]
        # Traverse to the last node then link it to the target
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = target_node


def update_tree(item, tree_node, header_table, frequency):
    if item in tree_node.children:
        # If the item already exists, increment the count
        tree_node.children[item].increment(frequency)
    else:
        # Create a new branch
        new_item_node = Node(item, frequency, tree_node)
        tree_node.children[item] = new_item_node
        # Link the new branch to header table
        update_header_table(item, new_item_node, header_table)

    return tree_node.children[item]


def ascend_fptree(node, prefix_path):
    if node.parent is not None:
        prefix_path.append(node.item_name)
        ascend_fptree(node.parent, prefix_path)


def find_prefix_path(base_pat, header_table):
    # First node in linked list
    tree_node = header_table[base_pat][1]
    cond_pats = []
    frequency = []
    while tree_node is not None:
        prefix_path = []
        # From leaf node all the way to root
        ascend_fptree(tree_node, prefix_path)
        if len(prefix_path) > 1:
            # Storing the prefix path and it's corresponding count
            cond_pats.append(prefix_path[1:])
            frequency.append(tree_node.count)

        # Go to next node
        tree_node = tree_node.next
    return cond_pats, frequency


def mine_tree(header_table, min_sup, prefix, freq_item_list):
    # Sort the items with frequency and create a list
    sorted_item_list = [item[0] for item in sorted(list(header_table.items()), key=lambda p: p[1][0])]
    # Start with the lowest frequency
    for item in sorted_item_list:
        # Pattern growth is achieved by the concatenation of suffix pattern with frequent patterns generated from 
        # conditional FP-tree
        new_freq_set = prefix.copy()
        new_freq_set.add(item)
        freq_item_list.append(new_freq_set)
        # Find all prefix path, construct conditional pattern base
        conditional_patt_base, frequency = find_prefix_path(item, header_table)
        # Construct conditional FP Tree with conditional pattern base
        conditional_tree, new_header_table = construct_tree(conditional_patt_base, frequency, min_sup)
        if new_header_table is not None:
            # Mining recursively on the tree
            mine_tree(new_header_table, min_sup,
                      new_freq_set, freq_item_list)


def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)))


def get_support(test_set, item_set_list):
    count = 0
    for item_set in item_set_list:
        if set(test_set).issubset(item_set):
            count += 1
    return count


def association_rule(freq_item_set, item_set_list, min_conf):
    rules = []
    for item_set in freq_item_set:
        subsets = powerset(item_set)
        item_set_sup = get_support(item_set, item_set_list)
        # Writing freq_item_set.csv
        freq_item_export_csv(item_set, item_set_sup, len(freq_item_set), item_set_list)
        for s in subsets:
            confidence = float(item_set_sup / get_support(s, item_set_list))
            if confidence > min_conf:
                rules.append([set(s), set(item_set.difference(s)), confidence])
    return rules


def get_frequency_from_list(item_set_list):
    frequency = [1 for i in range(len(item_set_list))]
    return frequency
