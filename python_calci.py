n = int(input("Enter the operation number N: "))

""" n is use to choose the operations such as add, sub, multi, devide, etc.
for add use 1, for sub use 2, for multi use 3, for devide use 4, 
for modulus use 5, for floor devision use 6 """

A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))

if(n==1):
    print("A + B = ", A+B)
    
elif(n==2):
    print("A - B = ", A-B)
    
elif(n==3):
    print("A * B = ", A*B)
    
elif(n==4):
    print("A / B = ", A/B)
    
elif(n==5):
    print("A % B = ", A%B)
    
elif(n==6):
    print("A // B = ", A//B)
    
else:
    print("Invalid Input...")
