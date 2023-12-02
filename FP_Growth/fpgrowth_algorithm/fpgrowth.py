from FP_Growth.fpgrowth_algorithm.utils import *
from Export.DataExport import association_rules_export_csv


def fpgrowth(item_set_list, min_sup_ratio, min_conf):
    frequency = get_frequency_from_list(item_set_list)
    min_sup = len(item_set_list) * min_sup_ratio
    fp_tree, header_table = construct_tree(item_set_list, frequency, min_sup)
    print("Total of activities: " + str(len(item_set_list)))
    print("Min_Support: " + str(min_sup))
    if fp_tree is None:
        print('No frequent item set')
    else:
        freq_items = []
        mine_tree(header_table, min_sup, set(), freq_items)
        rules = association_rule(freq_items, item_set_list, min_conf)
        association_rules_export_csv(rules)
        return freq_items, rules
