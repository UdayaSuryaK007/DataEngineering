#We have a list given below, which contains several numbers. 
# I want to slice this list based on its indexes, into 3 equal sub-lists.
num_list = [31, 24, 2, 16, 19, 45, 75, 63, 79]
intial_val = 0
index_val = 0
len_list = len(num_list)
for i in range(0,len_list,3):
    index_val += 1
    intial_val=i
    print("Sub-List",index_val,num_list[intial_val:intial_val+3])
