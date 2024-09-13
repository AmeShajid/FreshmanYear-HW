#Ame Shajid
#January 22, 2023
#In this code we are creating 3 functions and use them to create a number output, it will ask the user for two values both integers and compute them into different values. 


#Importing math module
import math
#creating the integer input 
#initalizing variables
a = int(input("Enter Value 1: "))
b = int(input("Enter Value 2: "))
x = a 
y = b

#function for f(x) with a in the front
def ffunctions(a):
    f = (2 * pow(a, 2)) - 7
    return f
f1 = ffunctions(a)

#function for f(x) with b in the front
def ffunctions(b):
    f = (2 * pow(b, 2)) - 7
    return f
f2 = ffunctions(b)

#function for g(x) with a , b
def gfunctions(a, b):
    g =pow(a, 3) - b  
    return g
g1 = gfunctions(a, b) 

#function for g(x) part 2 with b,a
def g2functions(a, b):
    g =pow(b, 3) - a 
    return g
g2 = g2functions(a, b) 

#function for H(x) with a
def hfunctions(a):
    h=(2 * pow(a, 2)) + (3 * a) + 9 
    return h
h1 = hfunctions(a) 

#function for H(x) with b
def hfunctions(b):
    h=(2 * pow(b, 2)) + (3 * b) + 9 
    return h
h2 = hfunctions(b) 


#print all the function values
print("f(", x, ")=",f1, sep="")
print("f(", y, ")=",f2, sep="")
print("g(", x, ",",y, ")=", g1, sep="")
print("g(", y, ",",x, ")=", g2, sep="")
print("h(", x, ")=",h1, sep="")
print("h(", y, ")=",h2, sep="")
print("f(h(", a, ")=",ffunctions(hfunctions(a)), sep="")
print("h(f(", b, ")=",hfunctions(ffunctions(b)), sep="")
print("g(f(", a, "),", "h(", b, "))=", gfunctions(ffunctions(a), hfunctions(b)), sep="")
print("g(h(", a, "),", "f(", b, "))=", gfunctions(hfunctions(a), ffunctions(b)), sep="")





