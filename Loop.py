#Exercise 1: Print First 10 natural numbers using while loop
"""
i=0
while i<11:
    print(i)
    i=i+1
"""
#Exercise 2: Print the following pattern
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""
#Exercise 3: Calculate the sum of all numbers from 1 to a given number
"""
n1 = int(input("Enter Number : "))
sum = 0
for i in range(1, n1+1):
    sum = sum+i
print(sum)
Output : 
Enter Number : 10
55
"""
#Exercise 4: Write a program to print multiplication table of a given number
"""
n1 = int(input("Enter Number : "))
for i in range(1,11):
    print(i*n1,end =" ")
Output : 
Enter Number : 3
3 6 9 12 15 18 21 24 27 30 
"""
#Exercise 5: Display numbers from a list using loop
"""
l1 = [12,23,45,56,4,67,9]
for i in l1:
    print(i,end=" ")
Output :
12 23 45 56 4 67 9 
"""
#Exercise 6: Count the total number of digits in a number
"""
num1 =1234555
num2 = str(num1)
print(len(num2))
Output :
7
"""
#Exercise 7: Print the following pattern
"""
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end =" ")
    print()
"""
#
"""
Output :
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
"""
#Exercise 8: Print list in reverse order using a loop
"""
list1 = [10,20,30,40,50,60]
list2 = reversed(list1)
for i in list2:
    print(i)
Output : 
60
50
40
30
20
10
"""
#Exercise 9: Display numbers from -10 to -1 using for loop
"""
for i in range(-10,0,1):
    print(i, end=" ")
output :
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
"""
#Exercise 10: Use else block to display a message “Done” after successful execution of for loop
"""
for i in range(4):
    print(i)
else:
    print("Done")
"""
#Exercise 11: Write a program to display all prime numbers within a range
"""
n1 = int(input("Enter number 1: "))
j=3
c1 = "not prime"
l1=[]
for num1 in range(3, n1+1):
         for i in range(2, num1):
                 if num1%i==0:
                      break
         else:
             print(num1)

Output:
Enter number 1: 20
3
5
7
11
13
17
19
"""
#Exercise 12: Display Fibonacci series up to 10 terms
"""
num = int (input("Enter Number : "))
num2=1
num1 =0
print(num1,end=" ")
for i in range(num+1):
    f = num1 + num2

    num2 = num1
    num1 = f

    print(f,end =" ")
Output :
Enter Number : 10
0 1 1 2 3 5 8 13 21 34 55 89 
"""
#Exercise 13: Find the factorial of a given number
"""
n1 = int(input("Enter Number : "))
s1 = 1
for i in range(1, n1+1):
    s1 = s1*i
print(s1)
Output :
Enter Number : 5
120
"""

#Exercise 14: Reverse a given integer number
"""
n1 = 56789
n2 = n1
rev = 0
while n1>0:
    rem = n1%10
    rev = (rev *10)+rem
    n1=n1//10
print("NUmber is : ",n2)
print("Reverse is : ",rev)
Output :
NUmber is :  56789
Reverse is :  98765
"""
#Exercise 15: Use a loop to display elements from a given list present at odd index positions
"""
l1 =[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16]
for i in range(1,len(l1),2):
    print(l1[i],end =" ")
    
Output :
2 4 6 8 11 13 15 
"""
#Exercise 16: Calculate the cube of all numbers from 1 to a given number
"""
n1 = int(input("Enter number : "))
for i in range(1, n1+1):
    print(i**3,end = " ")

output : 
Enter number : 20
1 8 27 64 125 216 343 512 729 1000 1331 1728 2197 2744 3375 4096 4913 5832 6859 8000

"""
#Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
"""
sum = 0
start = 2
for i in range(5):
    sum = sum + start
    start = (start * 10)+2
print(sum)

Output :
24690
"""
#Exercise 18: Print the following pattern
"""
for i in range(0, 5):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("")

for i in range(5, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("")
    
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""