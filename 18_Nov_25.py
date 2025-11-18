#COntrol Structures
#indentation 
print("hello")
 #print("Hello") #IndentationError: unexpected indent
a=int(input("input a:"))
#input() function always takes input from user in string format and it always return string.
b=int(input("input b:"))

#if a>b:
#print (a) #IndentationError: expected an indented block after 'if' statement on line 8
# minimum single sapce indentation is required
#significant or consistant indentation is must
if a>b:
    print("Geatest number is:",a)
else:
    print("greatest number is:",b)


#Interpolation - f-string
name1 = input("enter name:")
name2 = input("enter name2:")
Name=name1+name2 # concatination
print(f"welcome: {Name}")

num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num=num1+num2
print(f"sum of {num1} and {num2} is: {num}")
#print(f"sum of {num1} and {num2} is: {num}") is popular or updated version of print statement from python 3.6 onwards
if num>0:
    print(f"{num} is positive")
elif num<0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")