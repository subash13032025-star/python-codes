#break statement is used to exit or break the loop.
#once the python interpreter finds this break statement,it exits the loop
#if there are nested loops exists , then break exits the innermost loop

#eg
mysum=0
for i in range(5,10,1):
    mysum+=i
    if(mysum==5):#break statement breaks the loop not for branching stament
        break
print(mysum)
    
#program for finding the even numbers present in the specified range of for loop

even_num=0
for i in range(2,9,3):
    if i%2==0:
        even_num+=1
print(even_num)

#for loop can be used in strings to loop over the characters present in the string
#code to check letter i or u in a string

s = "demo loops - fruit loops"
for index in range(0,len(s)):
     if(s[index]=="i" or s[index]=="u" ):
         print("there is an i or u")
         break

#simpler form
for char in s:
    if char=="i" or char=="u" :
        print("there is an i or u")
        break

#simplest form
for char in s:
    if char in "iu":
        print("there is an i or u")
        break

#code for finding the unique characters present in the string
    
s="aabbccddee"
seen=""
for char in s:
    if char not in seen:
        seen+=char
print(len(seen))

#Guess and check algorithm

x=int(input("Enter a number: "))
guess=0
while guess**2<x:
    guess+=1
if guess**2 == x:
    print(f"the square root of {x} is {guess}")
else:
    print(f"{x} is not a perfect square")

#in case of negative numbers

x=int(input("Enter a positive number: "))
guess=0
neg_flag=False
if x<0:
      neg_flag=True
while guess**2 < x:
    guess+=1
if guess**2==x:
    print(f"the square root of {x} is {guess}")
else:
    print(f"{x} is not a perfect square")
if neg_flag:
    print(f"Did you mean {-x}")


#cube root for positive cubes using for loop (Guess and check algorithm)

x=int(input("Enter a number: "))
guess=0
for guess in range(x+1):
    if guess**3 == x:
        print(f"the cube root of {x} is {guess}")

#cube root for negative cubes using for loop (Guess and check algorithm)

x=int(input("Enter a number: "))
for guess in range(abs(x)+1):
    if guess**3==abs(x):
        if x<0:
            guess=-guess
        print(f"the cube root of {x} is {guess}")

#eg program

for alysa in range(11):
    for ben in range(11):
        for cindy in range(11):
            total=(alysa+ben+cindy==10)
            two_less=(ben==alysa-2)
            twice=(cindy==2*alysa)
            if total and two_less and twice:
                print(f"Alysa sold {alysa} tickets")
                print(f"Ben sold {ben} tickets")
                print(f"Cindy sold {cindy} tickets")

#for higher range
    
for alyssa in range(1001):
    ben=max(alyssa- 20, 0)
    cindy=alyssa*2
    if ben+cindy+alyssa==1000:
        print("Alyssa sold " + str(alyssa) + " tickets")
        print("Ben sold " + str(ben) + " tickets")
        print("Cindy sold " + str(cindy) + " tickets")

#consider a prgm

x=0.1
for i in range(10):
    x+=0.1
print(x==1)
print(x,"==",10*0.1)#small error will arise

#binary coversion for a given number

num=int(input("Enter a number: "))
if num<0:
    neg=True
    num=abs(num)
else:
    neg=False
result=""
if num==0:
    result="0"
while num>0:
    result=str(num%2)+result
    num=num//2
if neg:
    result="-"+result
print(f"the binary conversion of {num} is {result}")


    



