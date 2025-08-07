#while loops are used for iterating the statement for a number of times specified by the user
#it evaluates the condition true or false
#If condition is true the statement inside the while loop will be executed
#The while loop executes the statements continuously until the condition becomes false
#if the condition never becomes false,then it executes the statement infinite number of times

#eg program

a=input("you are in the lost forest.where you want to go left or right?")
while(a=="right"):#string is case sensitive,error will arise if a="RIGHT" is typed
    print("you are in the lost forest!!")
    a=input("where you want to go left or right?")
print("you are out of the lost forest!")

#eg 2

n=0
while(n<5):
    print(n)
    n+=1
print(n)

#eg 3

a=input("you are in the lost forest.where you want to go left or right?")
n=0#iteration can be done by setting loop variable outside the while loop 
while(a=="right"):
    print("you are in the lost forest!!")
    if(n==2):
        print(":(")
    a=input("where you want to go left or right?")
    n=n+1 
print("you are out of the lost forest!")

#finding factorial of a number using while loop

num=int(input("Enter a number to find its factorial: "))
n=1
fact=1
while(n<=num):
    fact=fact*n
    n+=1
print(fact)


#for loop is also a function used for executing the same statement for the defined number of times
#the difference betweeen while and for loop is that,in the for loop,loop variable is defined in the for loop itself

for i in range(6):
    print(i)

#range() in for loop can be used by defining the start,stop and step values similar to string slicing

for i1 in range(1,4,1):
 print(i1)
for j in range(1,4,2):
 print(j*2)
for me in range(4,0,-1):
 print("$"*me)

#running sum in the for loop

runsum=0
for i in range(6):
    runsum+=i
print(runsum)

#finding factorial of a number using for loop

num=int(input("Enter a number to find its factorial: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)


    

