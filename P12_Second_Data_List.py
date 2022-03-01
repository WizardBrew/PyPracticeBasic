# List operation 

# MyList = ["Apple", "Orange", "Mango", "Graph"]    3 List Operation Add two lists in short
# print(" <=====> ".join(MyList))
# print(" ".join(MyList))

# MyList = ["Apple", "Orange", "Mango", "Graph"]      # List
MyList = ["Apple", "Orange", "Mango", "Graph","Apple", "straw", "Apple"]      # List


MX = max(MyList, key =MyList.count)                 # counts max value or many same values in list
pX = max(set(MyList), key =MyList.count)
print(MX," \t",pX) 
print(MyList.count('Apple'))                          # counts max value or many same values in list

# MyList[0] = "Pulse"                                 # List item will be added at start
# MyList.append("Cereals")                            # List will be added at end
# MyList.remove("Mango")                              # List will Remove item in list
# MyList.pop()                                        # List will pop last item from list
# mylst = MyList.copy()                                 # Variable copy list
# AddList = ["Fruits", "Vegitables"]                  # List after new Variable 
# MyList += AddList                                   # Simple Concatination of Lists
# fruits = ["apple", "banana", "cherry"]            
# fruits.insert(2, "lemon")                           # Inserts item at the Second Place 
# print(fruits)
# mylst.append("Onion") 
# fruits = ["apple", "banana", "cherry"]
# print(fruits[-1])
# print(MyList)
# print(mylst)
'''
# lst = [1,2,3,4,5]
# a,b,c,d,e = lst
# print(a,b,c,d)
'''

'''
if "Apple" in MyList:
    print("yes")
    
    '''