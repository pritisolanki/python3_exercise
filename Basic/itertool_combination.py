import itertools

team_member = ["Priti", "Priya", "Shreya", "Siya"]

possible_teamof2 = list(itertools.combinations(team_member, 2))
print(f"There are total {len(possible_teamof2)} teams of 2 memeber")
print(possible_teamof2)

possible_teamof3 = list(itertools.combinations(team_member, 3))
print(f"There are total {len(possible_teamof3)} teams of 3 memeber")
print(possible_teamof3)
