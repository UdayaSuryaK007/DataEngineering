from datetime import datetime
#Q1: Write a Python function to check whether the number given below is present in between 5 to 10 (both included) or not.

num = 7
def to_Check():
    if 5<=num<=10:
        print("Q1-output: " + "\n" + "7 is present between 5-10."+ '\n')
    else:
        print("Q1-output: " + "\n" + "7 is not present between 5-10."+ '\n')
to_Check()

#Q2: Write a Python function that accepts two arguments and calculates the addition and subtraction of it.
# Also, print both the arithmetic results in a single return call.
def add_Sub_Operations(num1, num2):
    add = num1 + num2
    sub = num1 - num2    
    return add,sub
# num1 = int(input("Enter num1 value:"))
# num2 = int(input("Enter num2 value:"))
print("Q2-output: " + "\n" + "(Addition,Subtraction) : " + str(add_Sub_Operations(40, 10))+ "\n")

#Q3: Create a function in Python that displays the name and results of a candidate. 
# The function should accept the candidate's name and his/her results as "Pass/Fail." 
# If the result is missing in the function call, show it as "Pass."
print("Q3-output: ")
def candidates_func(name, result="Pass"):
    print(name + ' is ' + result)

candidates_func('Sam')
candidates_func('Judy','Fail')
print('\n')

#Q4: We have a list of numbers given below. Write a Python function to print all the odd-indexed items from the list.
n = [2, 3, 5, 6, 8, 9]
empty_List = []
def odd_Indexing(lst):
    for i in range(0, len(lst)):
        if i%2 != 0:
            empty_List.append(lst[i])
odd_Indexing(n)
print("Q4-output: " + '\n' + str(tuple(empty_List))+'\n')

#Q5: We have the names of six countries given below. Write a Python function to print all the countries that start with the letter 'A.'
print("Q5-output: ")
countries = 'Austraiia', 'India', 'Austria', 'America', 'Russia', 'Iran'
empty_Countries = []
def countries_Func(return_var):
    for i in list(return_var):
        if 'A' in i:
            empty_Countries.append(i)
        else:
            pass
    return empty_Countries
countries_Func(countries)
print(str(empty_Countries) + '\n')

#Q6: A list of tuples is given below, containing the candidate's name and their heights(in cm). 
# Sort this list using Lambda functions according to the heights of the candidates.
print("Q6-output: ")
candidate_details = [('Harry', 168), ('Jhonny', 160), ('Brad', 178), ('Chris', 172)]
def lambda_func(candidates_Details):
    final_Sort_Val = sorted(candidates_Details, key=lambda val:val[1])
    return final_Sort_Val

print(str(lambda_func(candidate_details))+'\n')


#Q7: Write a Python function to find 'Mall' from the dictionary 'map_details' given below.
print("Q7-output: ")
map_details = {101:'Park', 102:'Zoo', 103:'Mall'}
def dict_map_details(get_dict):
    for k, v in get_dict.items():
        if v == 'Mall':
            return k
        else:
            pass
print(str(dict_map_details(map_details))+'\n')


#Q8: Write a Python program to add the three lists given below using Python map and Lambda function.
list_1 = [1, 5, 8]
list_2 = [3, 2, 5]
list_3 = [2, 3, 6]
print("Q8-output: ")
def map_Lambda_Func(lst_1,lst_2,lst_3):
    result_list = list(map(lambda x,y,z:x+y+z, lst_1,lst_2,lst_3))
    return result_list

print(str(map_Lambda_Func(list_1,list_2,list_3))+ '\n')

#Q9: We have the marks of a student in each subject given below. 
# Write a Python function that takes two parameters 'name' and 'subjects_marks.' 
# Finally, print the student's name and all the subjects in which his/her marks are above 60. 
# If the 'name' is not provided, print 'None.'
print('Q9-output: ')
# Mathematics = 80; Physics = 58; Chemistry = 62; English = 72; Biology = 50
subjects_marks = {'Mathematics':80, 'Physics' : 58, 'Chemistry' : 62, 'English' : 72, 'Biology' : 50}
def student_Details(subjects_marks, name=None):
    comp = {key for key,values in sorted(subjects_marks.items()) if values>60}
    print('Name: '+ name + '-' + 'Subjects:', comp, '\n')
    # Name: Brandon - Subjects: {'Chemistry', 'English', 'Mathematics'}
student_Details(subjects_marks, name='Brandon')

#Q10: Using Lambda function, extract and print the year from the datetime object given below.
print('Q10-output: ')
given_date = datetime(2008, 6, 12, 10, 30, 0)

def extract_Year(get_date):
    return get_date.strftime('%Y')
print(extract_Year(given_date))







