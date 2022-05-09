#exploring print - explore padding formatting
'''
Name            Cities                  Age     Hobbies
Raj             Bangalore               14      Hiking, Swimming
Simran          Delhi                   12      Walking
Ajay            Mumbai                  15      Coding
Vijay           Ahmedabad               20      Singing, Dancing
Varun           Shimla                  21      Programming
'''

heading=['Name','Cities','Age','Hobbies']
cities = ['Bangalore','Delhi','Mumbai','Ahmedabad','Shimla','Udaipur']
names = ['Raj','Simran','Ajay','Vijay','Varun','Arjun']
age = [14,12,15,20,21,13]
likes = ['Hiking, Swimming', 'Walking','Coding','Singing, Dancing','Programming']
file_data = list(zip(names,cities,age,likes))

print(f'{heading[0].ljust(10)}\t{heading[1].ljust(20)}\t{heading[2].ljust(3)}\t{heading[3]}')
for row in file_data: 
    print(f'{row[0].ljust(10)}\t{row[1].ljust(20)}\t{str(row[2]).ljust(3)}\t{row[3]}')

