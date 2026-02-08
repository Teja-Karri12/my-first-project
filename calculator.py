#creating a simple calculator using function 
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
#user input values
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
print("1-Addition")
print("2-Subraction")
print("3-multiplication")
print("4-division")
choice=int(input("Enter a number in (1-4):"))
if choice==1:
    print("Result:",add(x,y))
elif choice==2:
    print("Result:",sub(x,y))
elif choice==3:
    print("Result:",mul(x,y))
elif choice==4:
    print("Result:",div(x,y))
else:
    print("Invalid choice")