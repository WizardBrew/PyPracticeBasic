# a={}                               # By Default its empty Dict

# b = set ()                          #Creats Empty Set
# print(b.add(4))                     # Adds elemets
# b.add(5)
# # b.add([2,4,6])                      # Cannot Add list bcz its changeable
# # b.add({2,4,6})                      # Cannot Add list bcz its changeable
# b.add((2,4,6))                      # Can Add list bcz its not changeable
# print(b)
#                                     #Sets Are Un order and Un Indexed
# b.remove(5)
# print(b)

mydict = {
    "panka":"Fan",
    "dabba":"box",
    "Vastu":"Item"

}
print("These are options",mydict.keys())
# a = input("Enter The Word\n")
# print("This is the meaning: ", mydict[a])           # should match the keys or will through error
# print("This is the meaning: ", mydict.get(a))       #Does not throw the error if not exist

# z = input("Enter Here \n")
h = list(mydict)
# print("Your Required OP", mydict.get(str.lower(z)))
