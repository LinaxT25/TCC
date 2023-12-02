from FP_Growth import ActivitiesExtract
from Export import DataExport
from FP_Growth.fpgrowth_algorithm.fpgrowth import fpgrowth


def fp_growth():
    activity_list = ActivitiesExtract.data_pattern()

    # For 50% of total actors(4263) and total of activities in list(4109): 2131,5 / 4109
    # freq_item_set, association_rules = fpgrowth(activity_list, min_sup_ratio=0.5187, min_conf=0.1)

    # For 25% of total actors(4263) and total of activities in list(4109): 1065,75 / 4109
    # freq_item_set, association_rules = fpgrowth(activity_list, min_sup_ratio=0.2593, min_conf=0.1)

    # For 10% of total actors(4263) and total of activities in list(4109): 426,3 / 4109
    # freq_item_set, association_rules = fpgrowth(activity_list, min_sup_ratio=0.1037, min_conf=0.1)

    # For 5% of total actors(4263) and total of activities in list(4109): 205,45 / 4109
    # freq_item_set, association_rules = fpgrowth(activity_list, min_sup_ratio=0.05, min_conf=0.1)

    # For 2% of total actors(4263) and total of activities in list(4109): 85,26 / 4109
    # freq_item_set, association_rules = fpgrowth(activity_list, min_sup_ratio=0.0207, min_conf=0.1)

    # For 1% of total actors(4263) and total of activities in list(4109): 42,63 / 4109
    freq_item_set, association_rules = fpgrowth(activity_list, min_sup_ratio=0.0103, min_conf=0.1)

    # Graphs.graph_pattern(patterns, 2)
    # Graphs.graph_rule(rules)
