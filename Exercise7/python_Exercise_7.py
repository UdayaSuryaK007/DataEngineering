from datetime import datetime
#Q1: We have defined a variable x equals 2. Then we have the if-else condition, which checks if x is equal to 2 or not. 
# But we get an error in the output. Decode the error and rectify the program to get the expected output.
print("Q1-output: ")
def sample_demo(a):
    try:
        if a == 2:
            print("Exact match!"+'\n')
        else:
            print("No Exact match!"+'\n')
    except Exception as Ex:
        print(Ex)
x = 2
sample_demo(x)

#Q2: There is a message given below. When we try to print the message, we are getting a syntax error. Look at the error and rectify it.
print("Q2-output: ")
msg = "Don't run in the park."
print(msg+"\n")

#Q3: We have a program given below that generates an AttributeError exception. 
# Make changes in the program to handle this exception and print the message 'An error occured.'
print("Q3-output: ")
class raiseAttribute():
    def __init__(self):
        self.a = 'getting an attribute errors'

obj = raiseAttribute()
try:
    print(obj.a.append())

except AttributeError:
    print("An Error occured."+'\n')

#Q4: We have a function given below which prints an element from the list.But what if the user calls an invalid index? 
# So, I want you to re-write the following function using the try-except block to handle the IndexError exception.
print("Q4-output: ")
class get_IndexError():
    def __init__(self):
        self.lst = [1,2,4,'Uday',7,8]
    def get_method(self):
        #lst = [1,2,4,5,7,8]
        try:
            print(self.lst[9])
        except IndexError:
            print("Invalid index, try again."+'\n')

objIndex = get_IndexError()
objIndex.get_method()

#Q5: We have a function given below that adds elements of two lists. 
# However, I can think of two exceptions that can occur in this program.
#       1. The index entered by the user during the function call may be out of bound.
#       2. The list entered by the user can consist of int objects, str objects, or even a combination of both. 
#          And what if we try to add an int object and an str object?
# Re-write this program to handle the two exceptions mentioned above.
print("Q5-output: ")
class sampleException():
    def __init__(self, lst_1, lst_2, index):
        self.list_1 = lst_1
        self.list_2 = lst_2
        self.index = index
    def add_elements(self):
        try:
            #for IndexError
            print(self.list_1[self.index])
            # adding both 'int'-type & 'str'-type lists elements 
            result = [self.list_1[i] + self.list_2[i] for i in range(len(self.list_1))]
            print(result)
        except Exception:
            print('Invalid index, try again')
# print("Enter list1 int elements:")
# list_1 = [int(x) for x in input().split(',')]
# print("Enter list2 int & str elements:")
# list_2 = [x for x in input().split(',')]
# index = int(input('Enter index: '))
objExcept = sampleException([1,2,3,4,5], [2,4,'Uday','Surya'], 6)
objExcept.add_elements()

#Q6: Write a Python program to find the day of the week for the date given below. 
# Also, we don't know what errors we might encounter while executing the program. 
# So, wrap the code inside a try-except block and handle the exceptions by printing the message 'Oops! An error occurred.'
print("Q6-output: ")
given_date = datetime(2010, 6, 12)

class day_Of_Week():
    def __init__(self, given_date):
        self.given_date=given_date
    
    def get_DayOfWeek(self):
        try:
            get_day = self.given_date.strftime('%A')
            print(get_day+'\n')
        except Exception:
            print('Oops! An error occurred.'+'\n')

obj_Day = day_Of_Week(given_date)
obj_Day.get_DayOfWeek()

#Q7: Write a function to reverse a string if it's length is an even number. I think of the TypeError exception 
# if a numeric value is passed inside the function call. But there might be other exceptions too that can occur 
# while executing the program. So, wrap the function around a try-except block and handle the TypeError exception 
# with the message 'Check the string.' For all other exceptions, print the message 'Something went wrong.'
print("Q7-output: ")
Input_String = 'Python'
def reverse_String(str):
    try:
        if len(str)%2==0:
            print(str[::-1]+'\n')
    except TypeError:
        print('Check the string.'+'\n')
    except Exception:
        print('Something went wrong.'+'\n')

reverse_String(Input_String)

#Q8: Write a function to extract the first ten letters of a string passed as an argument. 
# But if the string is less than ten characters long, raise a ValueError and 
# handle it using the message 'Oops! Too short string.'
print("Q8-output: ")
def extract_strng(extrct_str):
    try:
        # checks the user input string is greater than 10.
        if len(extrct_str)>=10:
            ten_letters = extrct_str[:10]
            #print(ten_letters)
        else:
            #Raised when the user input length is less than 10 and it will pass to except.
            raise ValueError
    except ValueError:
        print('Oops! Too short string.'+'\n')
str = input("Enter the string:")
extract_strng(str)

#Q9: Write a program to square the number entered by the user. 
# But what if the user enters a string or an alphanumeric value, or if some other unexpected exceptions occur. 
# So, wrap the program inside the try-except block to handle the exceptions, and 
# the program should run until the user enters a numeric value.
print("Q9-output: ")
def square_Method():
    while True:
        try:
            num = int(input("Enter the number:"))
            #Squaring the number
            print(num**2, '\n')
        except Exception:
            #Exception raised and the loop will started again untill the user can entered valid input
            print('Enter a valid input.')
            continue
        else:
            #once entered a valid number then ready to exit the loop
            break
# obj_Square = square_number()
square_Method()

#Q10: Write a program to process the results of the user. 
# The program should consist of a user-defined exception class 'InvalidNumError' to raise an error 
# if the marks entered by the user is less than 0 or greater than 100. Otherwise, print the message 'Results processing.'
# ---- Creating USer defined Exception ----
print("Q10-output: ")
class InvalidNumError(Exception):
    def __init__(self, msg):
        self.msg = msg
#--- 
def user_marks(mrks):
    try:
        if 0 <= mrks <= 100:
            print("Results processing."+'\n')
        else:
            raise InvalidNumError('Error! Try again.')

    except InvalidNumError as error:
        print(error+'\n')

marks = int(input("Enter the marks: "))
user_marks(marks)