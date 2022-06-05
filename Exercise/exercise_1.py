# list, prettytables - By Priti

from doctest import OutputChecker
from prettytable import PrettyTable
import itertools

data_table = PrettyTable()
data_table.field_names = ["Source_IP", "count", "Dest_IP", "Destionation_count"]
list1 = [
    ["168.212. 226.204", "2345"],
    ["168.212. 226.205", "222"],
    ["168.212. 226.206", "504"],
]
list2 = [
    ["215.212. 226.204", "233"],
    ["215.212. 226.205", "1298"],
    ["215.212. 226.206", "5045"],
]

list3 = [
    {"168.212. 226.204", "2345"},
    {"168.212. 226.205", "222"},
    {"168.212. 226.206", "504"},
]
list4 = [
    {"215.212. 226.204", "233"},
    {"215.212. 226.205", "1298"},
    {"215.212. 226.206", "5045"},
]

for k, v in enumerate(zip(list1, list2)):
    row = v[0] + v[1]
    data_table.add_row(row)
print(data_table)
