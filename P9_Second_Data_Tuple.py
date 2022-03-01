#Operations of list

mylist = ("FootBall", "VolleyBall", "Cricket", "Teniss", "Rugby") # this is my list Displayed

# Method 1st
'''
addlist = list (mylist)         # First Create and Assign list made
addlist.append("Carrom")        # Add the item to created Variable.
mylist = tuple (addlist)        # Initialize main list with tuple created.
print(mylist)                   # Print the master list will be added with created list.
''' 

# Method 2nd
'''
addlist = ("Carrom",)           # create Variable for list
mylist += addlist               # initilz main list with created Variable using logical Operator
print(mylist)                   # Print Master list
'''
#Method 3rd
'''
addlist = list (mylist)         # First initlz variable with main list
addlist[0] = "Carrom"           # Replace the item 
addlist.append("carrom")        # Adds the item in the last.
mylist = tuple(addlist)         # define the created valiable as main list
print(mylist)                   # Print Main List
'''

#TimTuts

a,b,c,d,e = mylist              # this will defualt takes and assign the value of tupple
print(a,b,c,d,e)                # Should pass the same elements of tup

