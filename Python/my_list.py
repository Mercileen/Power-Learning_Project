# empty list
my_list = []
# Append the following elements to my_list: 10, 20, 30, 40.
my_list = [10, 20, 30, 40,]
print("Before Append:",my_list)
#Insert the value 15 at the second position in the list.
my_list.insert(1,15)
print(my_list)
#Extend the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print(my_list)
#Remove the last element from the list
my_list.pop()
print(my_list)
#Sort the list in ascending order
my_list.sort()
print(my_list)
#Find and print the index of the value 30
index_of_30 = my_list.index(30)
print(index_of_30)
