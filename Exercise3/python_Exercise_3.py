#Q1 : Convert the string given below into a list by taking each word separated by a comma as an element.
languages = "Java, Python, C++, Scala, C"
empty_list = []
for i in languages.split(','):
    empty_list.append(i)
print(empty_list)

#Q2 : We have a list of numbers given below. Add the element '10' at the 3rd position of the list and finally print the list.
num_list = [5, 6, 8, 7, 9]
num_list[3] = 10
print(num_list)

#Q3 : Print all the multiples of 3 between 5 and 25.
for i in range(5, 25):
    if i%3==0:
        print(i)
#Q4 : We have a list of numbers given below. Print the square of these numbers into another list using list comprehension.
num = [2, 4, 6, 8]

list_comprhension = [x**2 for x in num]
print(list_comprhension)

#Q5 : Print the first 10 natural numbers.
i = 1
while i<=10:
    print(i)
    i = i+1

#Q6 : We have a tuple of numbers given below. Remove the largest number from the tuple and print it in sorted order.
num_tuple = (5, 8, 13, 2, 17, 1)
lst = list(num_tuple)
#max_val = max(lst)
lst.remove(max(lst))
lst.sort()
print(lst)

#Q7 : Convert the list given below into a string using a comma as a separator argument.
myList = ['Lenovo', ' Dell', ' Acer', ' Asus', ' HP']
strng_val = ""

joined_string = ','.join(myList)
print(joined_string)

#Q8 : Print all the even numbers between -10 and 0.
for i in range(-10, 0):
    if i%2==0:
        print(i)

#Q9 : Reverse the integer given below.  
n = 5623
print(str(n)[::-1])

#Q10 : We have a list of numbers given below. Print the number, square of the number, and the cube of the number, all in a single list.
num = [2, 4, 6, 8]
lst_com = [(x, (x**2), (x**3)) for x in num]
print(lst_com)


