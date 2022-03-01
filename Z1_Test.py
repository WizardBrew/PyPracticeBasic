

x = "*"
y = "+"
z = "/"


Take_one = int(input("Enter the first number: "))

Oper = input("Enter the operator: ")

def ops(x,y,z):
    if Oper == x:
       print( Take_one * Take_two)
       if Take_one == 43 & Take_two == 3 & Oper == x:
           print("555")
    elif Oper == y:
        print (Take_one + Take_two)

    elif Oper == z:
        return Take_one / Take_two
    else:
        print(Take_one, Take_two)




# if Oper == x:
#     print("Multiplication of ",Take_one, "X" )
# elif Oper == y:
#     print("Addition of ",Take_one, "Y" )
# elif Oper == z:
#     print("Division of ",Take_one, "Z" )
# else:
#     print("Invalid Operator")

Take_two = int(input("Enter the second number: "))

print(ops(x,y,z))
# print(Take_one, Oper, Take_two, "=", Take_one Take_two)






# result = int(input("Enter your Age\n"))

# if result<18:
#     print("you are not eligible to drive ")
# elif result==18:
#     print("Plese Walkin for test to decised")
# else :
#     print("You are eligible")


# a=10

# while a<5:
#     print(a)
#     a+=1
    


# a= 50 if 20>15 else 5
# print(a)

# MyList = ["Apple", "Orange", "Mango", "Graph"]
# print(" <=====> ".join(MyList))
# print(" ".join(MyList))

# for s in range(1, 10):
#     print(s)

# itr = list(range(1,10))
# print(itr)

# m = 50 if 25<30 else 40
# print(m)

# mk = set(range(1,21))
# print(mk)

# mj = 70 if 50 >100 else list(range(1,20))
# print(mj)

# a= 1
# while a<10:
#     print(a)
#     a+=1
#     if a==5:
#         break

# xm = "parvez"
# print("Captain", " America",sep= ' ' , end=" Avenger")



# prz = int(input())

# while prz<=25:
#     print(prz)
#     prz+=1