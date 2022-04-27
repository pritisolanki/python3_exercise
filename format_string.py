import csv

with open('cars.csv') as carsFile:
    reader = csv.DictReader(carsFile)
    for row in reader:
        print(row)