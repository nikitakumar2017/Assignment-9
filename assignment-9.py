#Q.1- Name and handle the exception occured in the following program:
'''
a=3
if a<4:
    a=a/(a-3)
    print(a)

'''
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError as msg:
    print("The name of the exception is ZeroDivisionError and the message is: ",msg) 

#Q.2- Name and handle the exception occurred in the following program: 
#l=[1,2,3] 
#print(l[3]) 
l=[1,2,3] 
try:
    print(l[3])
except:
    print("The name of the exception is IndexError and the message is list index out of range")

#Q.3- What will be the output of the following code:
# Program to depict Raising Exception
'''
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not

'''
Output will be:
An exception
NameError :Hi There 

#Q.4- What will be the output of the following code: 
# Function which returns a/b
'''
def AbyB(a , b):
        try:
            c = ((a+b) / (a-b))
        except ZeroDivisionError:
            print("a/b result in 0")
        else:
            print(c)
    
    # Driver program to test above function
    AbyB(2.0, 3.0)
    AbyB(3.0, 3.0)
    '''
case 1 output: -5
case 2 output: a/b result in 0   
    
#Q.5- Write a program to show and handle following exceptions: 
#1. Import Error 
#2. Value Error 
#3. Index Error
try:
    import abcdefg
except ImportError:
    print("There is not module with this name ")


try:
    a=int(input("Enter a string to throw ValueError Exception"))
except ValueError:
    print("You cannot enter string value where int is required")


try:
    l=[1,2,3,4]
    print(l[5])
except IndexError:
    print("This index does not exist ")
    

