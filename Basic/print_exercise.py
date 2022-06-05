# exploring print - explore padding formatting

import csv

heading = ["Name", "Cities", "Age", "Hobbies"]
cities = [
    "Bangalore",
    "Delhi",
    "Mumbai",
    "Ahmedabad",
    "Shimla",
    "Udaipur",
    "Agra",
    "Delhi",
]
names = ["Raj", "Simran", "Ajay", "Vijay", "Varun", "Arjun", "Rani", "Anu"]
age = [14, 12, 15, 20, 21, 13, 21, 11]
likes = [
    "Hiking, Swimming",
    "Walking",
    "Coding",
    "Singing, Dancing",
    "Programming",
    "Dancing",
    "Hiking",
    "Coding",
]
file_data = list(zip(names, cities, age, likes))

csv_file_handle = open("student.csv", "w")
writer = csv.writer(csv_file_handle)
writer.writerow(heading)

print(
    f"{heading[0].ljust(10)}\t{heading[1].ljust(20)}\t{heading[2].ljust(3)}\t{heading[3]}"
)
for row in zip(names, cities, age, likes):
    print(f"{row[0].ljust(10)}\t{row[1].ljust(20)}\t{str(row[2]).ljust(3)}\t{row[3]}")
    writer.writerow(row)

csv_file_handle.close()
