from prettytable import PrettyTable
import json

classes = r"D:\BUV university\Software Development\SDAM\w09\lab10\char_classes.json"

with open(classes, 'r') as file:
    classes = json.load(file)

def make_stat_sheat(stats):
    stat_sheat = PrettyTable()
    if stats:
        first_class = next(iter(stats))
        stat_sheat.field_names = ["Class"] + list(stats[first_class].keys())

    for Class, Stats in stats.items():
        stat_sheat.add_row([Class] + list(Stats.values()))

    return stat_sheat

print(make_stat_sheat(classes))