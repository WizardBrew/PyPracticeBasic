

'''
# unpacking concepts

# tupl = (1,2,3,4,5)
# a,b,c,d,e = tupl                          # this will defualt takes and assign the value of tupple
# print(a,b,c,d,e)                          # Should pass the same elements of tup

# lst = [1,2,3,4,5]
# a,b,c,d,e = lst
# print(a,b,c,d)

# string = "WizardBrew"
# x,y,z,a,b,c,d,e,f,g = string
# print(x,y,z,a,b,c)

# Dicti = {"A":"Apple", "B": "Ball", "C":"Cat"}
# M,N,O = Dicti.values()
# M,N,O = Dicti.keys()
# M,N,O = Dicti.items()
# print(M,N)

# coords = [40,50]
# x,y =coords
# print(x,y)
'''

#Compression

# ex = ["Hello" for i in range(4)]                     # prinits ["hello"] * 4 times in same list
# print(ex)


# SepHello = (i for i in "Hello")
# print(set(SepHello))
# print(list(SepHello))
# print(tuple(SepHello))

# x = [0 for i in range(100)]                        # prints the 100 of 0's
# print(x)

# x = [i for i in range(100)]                        # prints the 100 numbers from 0
# print(x)

# x = [i for i in range(100) if i %2]                # prints the Odd numbers from 0 to 100
# print(x)

# x = [i for i in range(100) if i %2==0]             # prints the Even numbers from 0 to 100
# print(x)

# y =[i for i in range(5) for i in range(5)]          # prints 1-5 elements 012340123401234
# print(y)

# y = [[i for i in range(4)]for i in range(8)]        # prinits [0,1,2,3,4] * 8 times
# print(y)

# y = [["Hello" for i in range(4)] for i in range(5)]             # prinits [Hello *4 ] [* 8 times]
# print(y)                                                        # starting i Obj



# m =(i for i in "Wizard")
# n =(list(m))
# print(n[2])

big_strg = "Hey bro how are you i love to code"
x = (i for i in big_strg)
xb = (list(big_strg))
t =(str(xb.whitespace))
print(t)