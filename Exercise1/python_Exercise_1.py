# Q1:There are two numbers given below. Print the sum of these numbers if their product is greater than 100. Otherwise, print their product.
a = 15
b = 12
if (a*b)>100:
    print(a+b)
else:
    print(a*b)

#Q2 : Write a Python program to print the volume of a cone whose height and diameter are given below. (Take pi = 3.14)
pi = 3.14
h = 10
d = 13
volumn = (1/12) * pi * (d ** 2) * h
print(volumn)

#Q3 : We have the name and seat numbers of a student given below as two tuples. With this given data, 
# print the students' names and their assigned seat numbers in a single line using the appropriate data type.
name = ('Shaun', 'Ron', 'Michael')
seat_numbers = (101, 102, 103)
dct = {name[i]:seat_numbers[i] for i in range(len(name))}
print(dct)

#Q4 : We have a number given below. If the number is greater than 0, add 1 to it. Otherwise, subtract 1 from it, and print the new number obtained.
num = -6
if num > 0:
    print(num + 1)
else:
    print(num-1)
#Q5 : I have four variables, each assigned with certain values given below. A massive expression line follows it. Re-write the expression which suits the desired lexical model.
a = 5
b = 2
c = 8
d = 7
x = (((a + b) * (a + c) * (a + d)) / ((b + a) * (b + c) * (b + d)) / ((c + a) * (c + b) * (c + d))) * (a * b * c * d)

print(x)

#Q6 : There are two numbers given below. Compare them and print the result obtained.
a = 5
b = 9
if a>b:
    print('a is greater than b')
else:
    print('b is greater than a')

#Q7 : We have a set given below. Find out whether 10 and 7 are present in the given set or not.
mySet = {5, 7, 2, 6, 3}
print(10 in mySet)
print(9 in mySet)

#Q7 : We have a number given below. Write a program to check for the divisibility of this number by 3 and 5, and print the result obtained.
a = 12
if a%3==0 or a%5==0:
    print('a is divisible by either 3 or 5, but not both')
else:
    print('a is not divisible by both numbers')

#Q8 : Write a Python program to check if the given year is a leap year.
year = 1996
if year%4==0:
    print('Leap Year')
else:
    print('Not a Leap Year')

#Q9 : I have an examination form that requires the following information.
# Name, Age, Roll Number, and Subjects.
# Declare the parameters mentioned above with a suitable data type, and then assign some values to it, and finally print the result.
Name = input("Enter Name:")
Age = int(input("Enter Age: "))
Roll_Number = int(input("Enter Roll Number: "))
#Subjects = input("Enter the Subjects:")
lst = [x for x in input("Enter list elements:").split(',')]
print('Name : ' + Name + '\n' + 'Age : ' + str(Age) + '\n' + 'Roll Number : ' + str(Roll_Number)+ '\n' + 'Subjects : ' + str(lst))
