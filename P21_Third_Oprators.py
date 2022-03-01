# Oprators Chapter with all 7 types.

# Add
# Fn=5
# Sn=3
# Tn=25.5
# Fs="Final"

# Airthmetic operator
'''
print('Addition of ', Fn + Sn ) 
print('Substract of ', Fn - Sn )
print('Multiply of ', Fn * Sn )
print('Division of ', Fn / Sn )
print('Modulous of ', Fn % Sn )
print('Exponantial of ', Fn ** Sn )
print('Floor Division of ', Fn // Sn )
'''
# Assign Oprators (+=, <, >, <=, >=,!=)#
# x = 5
# y = 3
'''
print("Comparision", x==y)      # x(5) is not same or equal to 3 so its False.
print("Comparision", x<y)       # x(5) is smaller than y(3) so Value is False.
print("Comparision", x>y)       # x(5) is Grater than y(3) so value is True.
print("Comparision", x<=y)      # x(5) is not smaller or equal to (y)3 so False.
print("Comparision", x>=y)      # x(5) is Grater or equal to y()3 Yes so True. 
print("Comparision", x!=y)      # x(5) is not equal to y(3) so value is true.
print(type(x!=y))               # Prints fun-type 
'''
# Logical Operators(and, or, not)
'''
print(x==5 and y==3)            # Both Value should be right to get true.
print(x==6 and y==3)            # Both Value should be right to get true.

print(x==5 or y==3)             # Any one of the value should be true
print(x==6 or y==6)             # Any one of the value should be Worng. True

print(not(x==6 and y==3))       # Both Value should be wrong to get True.
print(not(x==5 and y==3))       # Both Value should be wrong to get True.
'''

# Bitwise Operator(^,|,&,~,<<,>>)
# w =16
# x = 7
# y = 2
# z = 4
'''
print("Bitwise for XOR", x^y)          #0111 ^ 0010(5) = 0101 (0*0=0, 1*0=1, 1*1=0, 0*1=1) inverts with unlike 1*0 is 1 other all 0 
print("Bitwise for OR",  x|y)          #0111 | 0010(7) = 0111 (0*0=0, 1*0=1, 1*1=1, 0*1=1) only 0*0 is 0 other all 1
print("Bitwise for AND", x&y)          #0111 & 0010(2) = 0010 (0*0=0, 1*0=0, 1*1=1, 0*1=0) only 1*1 is 1 other all 0

print("Bitwise for NOT",  ~(x))        #0111 = 1000(8) Inverts the value of given. 

print("Bitwise for L'S",  x<<y)      # 7x2=14, 14x2=28
print("Bitwise for L'S",  x<<4)      # 7x2=14, 14x2=28, 28x2=56, 56x2=112
print("Bitwise for R'S",  x>>y)      # 7/2=3.5, 3.5/2=1
print("Bitwise for R'S",  w>>z)      # 16/2=8, 8/2=4, 4/2=2, 2/2=1
'''

# Membership Operators (in, not in)
#x = ["India", "USA", "Russia"]
'''
print("India" in x)                 # Using list define and in or not in to get Element Boolean
print("Turkey" not in x)
'''
#Identity Operators(is, is not)
# x = ["BMW", "Audi", "Lamborgini"]
# y = ["BMW", "Audi", "Lamborgini"]
# z = x
# x.append('car')           # Any modification will refelect in z      #Adds Item to the tables End/ Last
# z.append('Bike')          # Add any thing to get at last in x root value
# x[0] = 'Cycle'            # Adds item at the start of the Table using [0] can be any num.
'''
print(x is z)                   # X is Z bcz root Value has been assigned
print(x is y)                   # X is not y bcz its not root value
print(x == y)                   # x==y bcz values are same is Logical value
print(z)                        # Z is copy of x or refelcts root change
print(y)                        # Just copied but not refelects Root change.
'''