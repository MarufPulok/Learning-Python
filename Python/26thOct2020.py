#Matrix

matrix=[
  [1,2,3],
  [2,4,6],
  [7,8,9],
]
print(matrix[2][2])

#List Methods

basket=[1,2,3,4,5]
#adding
print(basket.append(33)) #prints 'None',but 33 is    added successfully.

basket.append(9)
print(basket)        #prints updated basket with 33 & 9

#assigning to a new list
items=['toy','car','phone','camera']
items.append('shoes')
new_items=items  #first append,then assign
print(items)
print(new_items)

#inserting(adding to a certain index)

groceries=['onion','potatoes','rice','sugar']
groceries.insert(1,'salt')
print(groceries)
#assigning to a new list is same as appending(first insert,then assign)

#extend(iterable data)

items1=['toy','car','phone','camera']
items1.extend(['ps4','gpu','ram'])
print(items1) #can add multiple items

#removing(pop,remove)

groceries1=['onion','potatoes','rice','sugar']
groceries1.pop()  #removes last item
print(groceries1)
groceries1.pop(2) #removes item in index 2
print(groceries1)

items2=['toy','car','phone','camera']
items2.remove('phone') #removes given value
print(items2)
print(items2.pop(0)) #returns whatever I've just removed

basket1=[1,2,3,4,5]
basket1.clear() #cleares whole list
print(basket1)

#every method till now except pop returns None



#List Methods 2

atom=['proton','electron','neutron','meson','positron']
print(atom.index('meson',0,4)) #index(value,search_start,search_end)
#prints index of the given value

#in keyword

string=['a','b','c','d','e']
print('x' in string) #whether x is in the list or not
print('f' in 'My name is Maruf')

#count
cnt=[1,2,3,3,5,5,7,8,6,6,6,10]
print(cnt.count(6))  #counts how many times the value occurs
