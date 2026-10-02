print("Calculator app")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        print("Zero cant be divide")
        return(x/y)
def power(x,y):
    return x**y
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
option=int(input("select an option:"))
if option==1:
    print('result:',add(num1,num2))
elif option==2:
     print('result:',subtract(num1,num2))
elif option==3:
     print('result:',multiply(num1,num2))
elif option==4:
     print('result:',divide(num1,num2))
elif option==5:
     print('result:',power(num1,num2))
else:
    print("invalid option")