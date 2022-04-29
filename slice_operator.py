# Having fun with - slicing operator
fruits = ["Banana", "Apple", "Pineapple", "Grapes","Custard apple","Orange", "Watermelon"]
fav_fruit = ','.join(fruits[0:3])

print(f'My three favorite fruits {fav_fruit}')
#My three favorite fruits Banana,Apple,Pineapple

print(fruits[0:len(fruits):2])
#['Banana', 'Pineapple', 'Custard apple', 'Watermelon']

print(fruits[len(fruits):0:-2])
#['Watermelon', 'Custard apple', 'Pineapple']

print(fruits[100:100:])
#[]

sample_text='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been'
#Show first 25 chracters
print(f'{sample_text[0:25]}')
#Lorem Ipsum is simply dum