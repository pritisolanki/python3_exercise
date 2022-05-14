#List comprehensions provide a concise way to create lists
numbers = [ x for x in range(1,31)]
print(numbers)
string = "Practice Problems to Drill List Comprehension in Your Head."

#Find all of the numbers from 1–1000 that are divisible by 8
list_8divisible = [ x for x in numbers if x%8 == 0]
print(list_8divisible)

#Find all of the numbers from numbers that have a 6 in them
list_contains6 = [ x for x in numbers if '6' in str(x)]
print(list_contains6)

#Find all of the words in a string that are less than 5 letters (use string above)
words = string.split(" ")
words_with5letters = [ word for word in words if len(word) <= 5]
print(words_with5letters)

#Use a nested list comprehension to find all of the numbers from number that are divisible by any single digit besides 1 (2-9)
result = [number for number in numbers if True in [True for x in range(3,10) if number % x == 0]]
print(result)

prairie_pirates = [
['Tractor Jack', 1000, True],
['Plowshare Pete', 950, False],
['Prairie Lily', 245, True],
['Red River Rosie', 350, True],
['Mad Athabasca McArthur', 842, False],
['Assiniboine Sally', 620, True],
['Thresher Tom', 150, True],
['Cranky Canola Carl', 499, False]
]

#Use a single list comprehension to create a list of the pirate names who plundered more than 400 sacks of assorted grains.
pirate_400sack = [ pirate for pirate in prairie_pirates if pirate[1] >= 400 ]
print(pirate_400sack)

#Suppose that the average market value of a sack of grain is $42. Use a single list comprehension to create a list of the market values of each pirate's grain.
pirate_marketval = [ [pirate[0] ,pirate[1]*42] for pirate in prairie_pirates ]
print(pirate_marketval)
