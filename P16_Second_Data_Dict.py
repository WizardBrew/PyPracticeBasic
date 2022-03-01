# Dictionary function.

MyDict = {"Windows": "Desktop", "Android": "Andro Mobile", "Mac": "I-Mac"}

MyDict["IOS"]= "I-Phone"
MyDict.update({"Linux":"DevSystem", "CentOS": "LinusOs"})

# print(MyDict["Android"])
# print(MyDict.get("Mac")) 
# exp = (tuple(MyDict["Windows"]))
# print(MyDict.pop("CentOS"))
# print(MyDict.popitem())
# del MyDict
# MyDict.clear()
# print(MyDict.keys())
# print(MyDict.values())
# print(list(MyDict.keys()))         # Converts to list and kives keys
# M = (list(MyDict.keys()))          # Converts to list and kives keys

d1 ={"a":1, "b":2}
d2 = {"c":3,"d":4}

# D_Add = dict(d1, **d2)                # Method 1 of adding the dict
# print(D_Add)

# print({**d1, **d2})                   # Same as Above method 1 short method

# Dicti = {"A":"Apple", "B": "Ball", "C":"Cat"}         # Assign the value to unpack
# M,N,O = Dicti.values()
# M,N,O = Dicti.keys()
# M,N,O = Dicti.items()
# print(M,N)

# print(str.lower(M))                # Need to test not Working code. Trial base
# for i in MyDict:
#     print(i)
#     print(MyDict[i])



# for x in MyDict.keys():
#     print(x)

# for x, y in MyDict.items():
#     print(x,"==", y)


# Urdict = MyDict.copy()

# print(MyDict)
# print(Urdict)

