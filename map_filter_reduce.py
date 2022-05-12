#map function
#title case the names
names = ['alfred', 'tabitha', 'william', 'arla']
names_corrected_case = map(lambda x: x.title(), names)
print(list(names_corrected_case))

#other way
names_corrected_case = map(str.title, names)
print(list(names_corrected_case))

#format currency based on country - By Priti
lst = [2.54, 4.0, 3, 9.95, 5.4]
country="India"
if(country == "India"):
    print(list(map("₹ {:,.2f}".format, map(lambda x: x,lst))))
else:
    print(list(map("$ {:,.2f}".format, map(lambda x: x,lst))))

#Using map() function and lambda and count() function create a list which consists of the number of occurence of letter: a.
lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
print(list(map(lambda x: x.count('a') ,lst1)))

#simple use cas to filter items
scores =[20,30,40,10,5,4]
print(list(filter(lambda score: score > 20,scores)))

#To get all the countries whose populations are greater than 300 million
countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

print(list(filter(lambda country: country[1]>300000000,countries)))