my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)

# RETURN LIST FROM INDEX 4
print(my_list[4:])

# RETURN LIST ELEMENTS FROM START TO INDEX 4
print(my_list[:4])

# RETURN ENTIRE LIST WITH SLICING
print(my_list[::])

# PRINT LIST ELEMENTS WITH A STEP OF 2
print(my_list[::2])

# PRINT THE LIST IN REVERSE
print(my_list[::-1])

# PRINT A PORTION OF THE LIST IN REVERSE
print(my_list[6:0:-1])

# APPEND NEW ELEMENTS
my_list.append(11)
print(my_list)

# APPEND A NEW LIST TO THE END OF A LIST
my_list02 = ['a','b','c','d','e','f']
print(my_list02)
my_list.append(my_list02)
print(my_list)
