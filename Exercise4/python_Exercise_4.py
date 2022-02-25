#Q1: We have two sets given below. Print the set of elements that are present in either set1 or set2 but not both.
from copy import copy

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
print(set1.symmetric_difference(set2))

#Q2: Print all the keys of the dictionary given below.
myDict = {1:'One', 2:'Two', 3:'Three'}
print(myDict.keys())

#Q3: We have two sets given below. Print the elements common to both the sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print(set1.intersection(set2))

#Q4: We have a dictionary given below. Delete the item with key '3,' and add an item with key '7' and value 'Black.'
color = {1:'Red', 2:'Orange', 3:'White', 4:'Brown', 5:'Yellow'}
color.pop(3)
color[7]='Black'
print(color)

#Q5: We have two sets given below. Check if set1 is a subset of set2.
set1 = {2, 4, 6}
set2 = {2, 4, 6, 8, 10}
print(set1.issubset(set2))

#Q6: Merge the two dictionaries given below.
myDict1 = {1:'One', 2:'Two', 3:'Three'}
myDict2 = {4:'Four', 5:'Five', 6:'Six'}
myDict1.update(myDict2)
print(myDict1)

#Q7: We have two sets given below. Print the elements that are present in set1 but not in set2.
set1 = {2, 3, 4, 5}
set2 = {2, 4, 6, 8}
print(set1.difference(set2))


#Q8: We have a dictionary given below. Copy this dictionary into another dictionary 'replica,' and change the value of the key 103 to 'Sally' in the replica dictionary only. Finally, print both the dictionaries.
student_details = {101:'Judy', 102:'Victor', 103:'Sam'}
replica = student_details.copy()
replica[103]= 'Sally'
print('student Details: ' + str(student_details) + '\n' + 'Replica: ' + str(replica))
# print(id(student_details))
# print(id(replica))

#Q9: Remove all the duplicate items from the tuple given below.
myTuple = ('Red', 'Blue', 'Green', 'Red', 'Orange', 'Green')

emptyList = []
myList = list(myTuple)
# print(myList)
for i in myList:
    if i not in emptyList:
        emptyList.append(i)
    else:
        pass
print(tuple(emptyList))

#Q10: Print the number and the cube of that number in a dictionary from 0 to 5.
dic = {x: x**3 for x in range(0, 6)}

print(dic)