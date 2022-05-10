#map function
#title case the names
names = ['alfred', 'tabitha', 'william', 'arla']
names_corrected_case = map(lambda x: x.title(), names)
print(list(names_corrected_case))

#other way
names_corrected_case = map(str.title, names)
print(list(names_corrected_case))

#format currency based on country
lst = [2.54, 4.0, 3, 9.95, 5.4]
country="India"
if(country == "India"):
    print(list(map("₹ {:,.2f}".format, map(lambda x: x,lst))))
else:
    print(list(map("$ {:,.2f}".format, map(lambda x: x,lst))))

#Using map() function and lambda and count() function create a list which consists of the number of occurence of letter: a.
lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
print(list(map(lambda x: x.count('a') ,lst1)))
