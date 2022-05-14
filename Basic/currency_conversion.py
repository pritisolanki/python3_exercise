import locale
loc = locale.getlocale()
locale.setlocale(locale.LC_ALL, loc)
lst = [2.54, 4.0, 3, 9.95, 5.4]
print([locale.currency(i, grouping=True, symbol=True) for i in lst])