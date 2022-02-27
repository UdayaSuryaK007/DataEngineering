#Q1-Print the following tuple in reverse order.
print("Q1-output:")
tuple_1 = (22, 65, 12, 54)
#print(tuple(reversed(tuple_1)))
print(tuple_1[::-1],'\n')

#Q2-Access the name 'David' from the list given below.
print("Q2-output:")
myList = [(2, 14, 'David'), [2, 7], 'Shaun']
print(myList[0][2],'\n')

#Q3-We have a set and a dictionary given below. Print the set once again after adding the keys of the dictionary to the set. 
# The order of the expected output may vary as it is a set.
print("Q3-output:")
mySet = {2, 4, 6}
myDict = {'A':'John', 'B':'Emma', 'C':'Sam'}
for k in myDict.keys():
    mySet.update(k)
print(mySet, '\n')

#Q4-We have two sets given below. Print all the items from these sets after removing the duplicates.
print("Q4-output:")
set_1 = {2, 4, 6, 8}
set_2 = {6, 8, 10, 12}
print(set_1.union(set_2), '\n')

#Q5-Write a Python program to print the first and the last second of the day.
print("Q5-output:")
import datetime
print("First Second: ", datetime.time.min)
print("Last Second: ",datetime.time.max, '\n')

#Q6-Print the total number of digits in the number given below.
print("Q6-output:")
num = 8842
count = 0
for i in str(num):
    count += 1 

print("Total digits are:", count, '\n')

#Q7-We have a list of lists that contains several numbers. I want you to print the list whose sum of elements is the highest and also the lowest.
print("Q7-output:")
num_list = [[2, 8, 11], [4, 5, 7, 12], [8, 9, 10, 11], [19, 13, 7], [2, 5, 16]]
print("The list with the maximum sum of elements: ",max(num_list, key=sum))
print("The list with the minimum sum of elements: ",min(num_list, key=sum),'\n')

#Q8-We have a string that contains the names of different fruits. I want you to convert this string into multiple substrings where each substring includes one fruit's name.
print("Q8-output:")
fruits_string = " Apple, Banana, Mango, Kiwi, Guava, Grapes, Pomegranate, Orange, Watermelon"
for fruit_name in fruits_string.split(','):
    print(fruit_name)
print('\n')

#Q9-Write a program to reverse words in a string.
print("Q9-output:")
sample_text = "Python is a high-level and general-purpose programming language"
reverse_string = sample_text.split(' ')
reverse_words = " ".join(reversed(reverse_string))
print(reverse_words,"\n")

#Q10-Given below is the height (in cm) of the top 10 students in a class. Print the heights of the top 3 students from the given list.
print("Q10-output:")
heights = [177, 160, 171, 163, 168, 175, 176, 183, 162, 170]
empty_lst = []
num = 3
for i in range(0, num):
    largeNo = 0
    for j in range(len(heights)):
        if heights[j] > largeNo:
            largeNo = heights[j]
    heights.remove(largeNo)
    empty_lst.append(largeNo)
print("Top Three Heights: ",empty_lst)



    

