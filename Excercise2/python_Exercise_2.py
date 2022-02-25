#Q1 : Print the item 'Orange' from the list of fruits given below.
fruits = ['Apple', 'Grapes', 'Orange', 'Pineapple', 'Watermelon']
print(fruits[2])

#Q2 :We have a list of fruits and a string given below. Since the string contains fruit, add that string to the given list and print that new list.
fruit_list = ['Apple', 'Grapes', 'Orange', 'Pineapple', 'Watermelon']
fruit_string = 'Mango'
fruit_list.append(fruit_string)
print(fruit_list)

#Q3 : There is a list given below which contains the name of cities. Repeat this list of cities three times, and print the old list and the new list.
cityList = ['London', 'New York', 'Delhi']
print('Old City List: ', cityList)
print('New City List: ', cityList*3)

#Q4 : Check if the city 'Delhi' is present in the list of cities given below.
cityList = ['London', 'New York', 'Delhi', 'Mumbai', 'Paris']
print('Delhi' in cityList)

#Q5 : Reverse the string given below.
name = 'Bridgelabz Organisation'
print(name[::-1])

#Q6 : There is a string object given below. Print the word 'sunny' from string 'msg.'
msg = 'A bright sunny day'
print(msg[9:14])

#Q7 : Check if the cities 'New York' and 'Delhi' are present in the list of cities given below.
cityList = ['London', 'New York', 'Delhi', 'Mumbai', 'Paris']
if 'New York' in cityList:
    print('New York' in cityList)
if 'Delhi' in cityList:
    print('Delhi' in cityList)

#Q8 : Using the slicing operation, remove the whitespaces between the letters and print the string once again.
name = 'P y t h o n'
print("".join(name.split()))

#Q9 : Print the index of the letter 'h' from the string given below.
name = 'Python'
print(name.index('h'))

#Q9 : Print the odd indexed elements from the list of colors given below.
myList = ['Red', 'Blue', 'Orange', 'White', 'Black', 'Yellow']
empty_list = []
for i in range(0, len(myList)):
    if i%2 != 0:
        #print(myList[i])
        empty_list.append(myList[i])

print(empty_list)