# Q1-We have two lists of numbers given below. I want you to create a third list by picking an odd-indexed element
#  from the first list and even-indexed elements from the second list.
from pickletools import int4


list_1 = [5, 10, 15, 20, 25, 30, 35]
list_2 = [7, 14, 21, 28, 35, 42, 49]
third_list = []
for i in list_1:
    if i%2 == 0:
        third_list.append(i)
for j in list_2:
    if j%2 != 0:
        third_list.append(j)
print("Q1-output:"+ '\n' + str(third_list) + '\n')

#Q2-You have two dictionaries, with each of them containing several letters associated with certain values.
print("Q2-output:")
num_1 = {'a' : 5, 's' : 7, 'x' : 11, 'm' : 12, 'o' : 8}
num_2 = {'r' : 12, 'x' : 9, 'n' : 8, 'm' : 12, 'q' : 10}
#get the common key value pairs in two dictionary using intersection()
print("1. common to both these dictionaries output" + '\n' + str(set(num_1).intersection(set(num_2))) +'\n')
print("2.  Print out the (key, value) pair, which is common to both these dictionaries.")
empty_dict = dict()
for k,v in num_1.items():
    # to checks the common values from two dictionary's
    if k in num_2 and num_1[k] == num_2[k]:
        empty_dict[k] = num_1[k] 
print(str(empty_dict) + '\n')
print("3. Print out all the letters which have occurred only once in these dictionaries." + '\n' + str(set(num_1).union(set(num_2))) + '\n')
print("4. Print out the letters in num_1 that are not present in num_2." + '\n' + str(set(num_1).difference(set(num_2))) + '\n')
print("5. Print out a new dictionary num_3, which contains unique letters of num_1 from the previous:")
num_3 = dict()
for key, value in num_1.items():
    if key not in num_2:
        num_3[key] = value
print(str(num_3) + '\n')

#Q3-Find out the number of letters and digits from the given alpha-numeric text.
print("Q3-output:")
sample_text = "Learning Journal 2020"
letters = digits = 0
for ltr_dig in sample_text:
    if ltr_dig.isalpha():
        letters += 1
    elif ltr_dig.isdigit():
        digits +=1
print("Number of Letters:"+ str(letters) + '\n' + "Number of Digits:" + str(digits) + '\n')

#Q4-We have a list given below. Add an item 200 to the list, after the item 100.
print("Q4-output:")
myList = [2, 8, [10, 20, [40, 60, [90, 100], 30, 70], 80], 50]
myList[2][2][2].append(200)
print(myList,'\n')

#Q5-We have two sets given below. Print the first set again after removing the elements common to both of these sets.
print("Q5-output:")
set_1 = {2, 8, 19, 13, 24, 55, 48, 93}
set_2 = {7, 11, 55, 84, 8, 65, 73, 13}
empty_set = set()
for element in set_1:
    if element not in set_2:
        empty_set.add(element)
print(empty_set, '\n')

#Q6-Print all the prime numbers between the given range.
print("Q6-output:")
start = 20
end = 60
print("Prime numbers between 20 and 60 are:", end='')
for num in range(start, end+1):
    if num>1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
        
print('\n')

#Q7-Here we have a list of 3 letters. I want you to concatenate this list with another list of numbers whose range varies from 1 to 3 (3 is included).
print("Q7-output:")
letters_list = ['H', 'R', 'S']
# empty_letter_list = []
# for no in range(len(letters_list)):
#     for no1 in letters_list:
#         empty_letter_list.append(no1+str(no+1))
# print(empty_letter_list)
sample_list = ['{}{}'.format(lt_1,lt_2) for lt_2 in range(1, len(letters_list)+1) for lt_1 in letters_list]
print(str(sample_list) + '\n')
    
#Q8-Print all the numbers between 1 and 100 (both being included) that are multiples of 3 and 5 both.
print("Q8-output:")
lst = [get_mul for get_mul in range(1, 100) if (get_mul%3 == 0) and (get_mul%5 == 0)]
print(str(lst) + '\n')

#Q9-Here we have a poem by Walt Whitman. I want you to print this poem once again after removing all the vowels from them.
print("Q9-output:")
poem = "Centre of equal daughters, equal sons, All, all alike endeared, grown, ungrown, young or old, Strong, ample, fair, enduring, capable, rich, Perennial with the Earth, with Freedom, Law and Love, A grand, sane, towering, seated Mother, Chaired in the adamant of Time."
empty_str = ""
vowels = ['a', 'e', 'i', 'o', 'u']
for remove_vowel in poem:
    if remove_vowel not in vowels:
        empty_str += remove_vowel
print(empty_str+'\n')

#Q10-Here we have some information about Python programming extracted from Wikipedia. Find all the occurrences of the word 'python' in the given python_info, ignoring the case.
print("Q10-output:")
python_info = "Python is an interpreted, high-level, and general-purpose programming language. Python is dynamically typed and garbage-collected. Python was created in the late 1980s as a successor to the ABC language, Python 2.0. Python 3.0 was released in 2008. A non-profit organization, the Python Software Foundation, manages and directs resources for Python development."
count = 0
for get_python in python_info.split(' '):
    if 'Python' == get_python:
        count += 1
print("The 'Python' count in python_info is:"+ str(count))




