# String Slicing

MyString = " Hi there! Do you Love Programing"

# print("Warrior", "WizardBrew", sep='@', end="com")  # how sep & end works. also end"\n"

string = "WizardBrew"                       # String unpacking
# x,y,z,a,b,c,d,e,f,g = string
# print(x,y,z,a,b,c)

# print(len(MyString))

print(MyString[4::])                      # Print from 4th Character to rest of it
print(MyString[:10:])                     # Prints till the 10 Chracter from 1st
print(MyString[::2])                      # Skipes 1 Characters (However default is 1)
print(MyString[-10::])                    # Prints from last 10 characters only (Programing)
print(MyString[:-10:])                    # Prints skipping last 10 Characters  skips (Programing)
print(MyString[::-1])                     # Prints In reverse Order all Characters  from back 
print(MyString[::-2])                     # Skips In reverse 2 Order all Characters  from back 
print(MyString[11:23:])                   # Prints from 11 Characters  till 23 & skips rest
print(MyString[-22:-11:])                 # Prints reverse -25th char till reverse -15th char
print(MyString[11:23:2])                  # Prints from 11 Characters  till 23 & skips 2 between
print(MyString[-22:-11:2])                # Prints reverse -22th char till reverse -11th char skips 2




