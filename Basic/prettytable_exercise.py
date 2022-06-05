# Exploreing prettytables - By Priti

import csv
from prettytable import PrettyTable
from itertools import islice

data_table = PrettyTable()
with open("techcrunch.csv") as data_csv:
    csv_reader = csv.reader(data_csv, delimiter=",")
    headers = next(csv_reader, None)

    data_table.field_names = map(lambda x: x.title(), headers)
    data_table.align = "l"
    data_table.sortby = "Company"
    for row in islice(csv_reader, 10):
        data_table.add_row(row)

print(data_table)
