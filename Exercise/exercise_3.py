def is_leap(year):
    leap = False
    print(year)
    print(year % 4, year % 100, year % 400)

    if year % 4 == 0:
        if (year % 100 == 0) and not (year % 400 == 0):
            leap = False
        else:
            leap = True
    return leap


year = 1900
print(is_leap(year))
year = 2000
print(is_leap(year))
