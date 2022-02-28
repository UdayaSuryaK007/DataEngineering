#We have two lists given below. I want you to print the first list in the original order and 
# the second list in reverse order simultaneously.
list_1 = [12, 25, 31, 20, 18]
list_2 = [11, 9, 43, 22, 55]
lst_2 = list_2[::-1]
for i in range(len(list_1)):
    print(list_1[i],lst_2[i])