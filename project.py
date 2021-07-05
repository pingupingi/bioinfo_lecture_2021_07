#! /usr/bin/env python

#2
name = input("insert your name: ")
print("Hello",name)


#3
acid = input("insert your acid: ")
if acid=="A":
    print("Adenine")
elif acid=="C":
    print("Cytosine")
elif acid=="G":
    print("Guanine")
elif acid=="T":
    print("Thymine")
elif acid=="U":
    print("Uracil")
else:
    print("Acid only has A,C,G,T,U")


#4
num = int(input("insert number: "))
try:
    result = 10/num
    print(result)
except ZeroDivisionError:
    print("can't divide with 10")



#5
sum=1
def fact(a):
    if a==1:
        return 1
    return a*fact(a-1)
print(fact(5))
