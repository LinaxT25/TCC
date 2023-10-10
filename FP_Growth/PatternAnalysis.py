from FP_Growth import ActivitiesExtract
from Export import FileWrite
from Export import DataExport
from FP_Growth.fpgrowth_algorithm.fpgrowth import fpgrowth


def fp_growth():
    activity_list = ActivitiesExtract.data_pattern()

    freq_item_set, association_rules = fpgrowth(activity_list, min_sup_ratio=0.05, min_conf=0)

    FileWrite.write_association_rules(association_rules)

    # DataExport.freq_item_export_csv(freq_item_set)
    # DataExport.association_rules_export_csv(association_rules)

    # Graphs.graph_pattern(patterns, 2)
    # Graphs.graph_rule(rules)
