
"""
#Multiplication and addition of 2 numbers.
num1 = int(input("Enter Number : "))
num2 = int(input("Enter NUmber : "))
num3 =  num1 + num2
print(f"Number is : {num3}")


Output :
Enter Number : 56
Enter NUmber : 89
Number is : 145
num1 = int(input("Enter Number : "))
num2 = int(input("Enter NUmber : "))
num3 =  num1 * num2
print(f"Number is : {num3}")

Output :
Enter Number : 45
Enter NUmber : 67
Number is : 3015


"""

"""
#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
num1 = 0
for i in range(0,10):
    j=i+1
    sum1 = i + j
    print(f"Current number {j} and previous number {i} , its sum is {sum1}" )
    
Output :
Current number 1 and previous number 0 , its sum is 1
Current number 2 and previous number 1 , its sum is 3
Current number 3 and previous number 2 , its sum is 5
Current number 4 and previous number 3 , its sum is 7
Current number 5 and previous number 4 , its sum is 9
Current number 6 and previous number 5 , its sum is 11
Current number 7 and previous number 6 , its sum is 13
Current number 8 and previous number 7 , its sum is 15
Current number 9 and previous number 8 , its sum is 17
Current number 10 and previous number 9 , its sum is 19

"""

#Write a program to accept a string from the user and display characters that are present at an even index number.

"""
s1 = input("Enter String : ")
for i in s1 :
    n1 = s1.index(i)
    if n1% 2==0:
        print(i,end="")
Output : 
Enter String : sneha
sea

"""
#Write a program to remove characters from a string starting from zero up to n and return a new string.
"""
n1 =""
n1 = input("Enter String : ")
n2 = int(input("Enter number : "))
for i in range(n2):
   n1 = n1.replace(n1[i],"0")
n1 = n1.replace("0","")
print(n1)

Output : 

Enter String : Sneha
Enter number : 1
neha

Enter String : Sneha
Enter number : 2
eha
"""
#
"""
def check_1_and_last():
    l1 = eval(input("Enter List : "))
    if l1[0] == l1[len(l1)-1]:
        return "true"
    else:
        return "false"
s1 = check_1_and_last()
print(s1)
Output : 
Enter List : [1,2,3,1]
true
"""
#Iterate the given list of numbers and print only those numbers which are divisible by 5
"""
l1 = [1,2,35,45,56,67,55,67]
for i in l1 :
    if i%5==0:
        print(i)
        
Output : 35
45
55

"""
#Return the count of a given substring from a string
"""
s1 = "Good Morning, have a Good day"
sub = "Good"
l1 = s1.split(" ")
c1 = l1.count(sub)
print(c1)

"""
#output : 2
#Exercise 8: Print the following pattern
"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""
# Code
"""
for i in range(6):
    for j in range(i):
        print(i, end =" ")
    print()
"""
#Exercise 9: Check Palindrome Number
"""
num1 = int(input("Enter number : "))
s1 = str(num1)
s2=s1[::-1]
num2 = int(s2)
if num1==num2:
    print("Number is palindrome")
else:
    print("Number is not a palindrome")
    
Output : 
Enter number : 67
Number is not a palindrome
"""
#
"""
Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from 
the first list and even numbers from the second list.


l1 = [1,2,3,4,7,8,9,56,45,78,34]
l2=[23,4,67,79,88,99,40,78]
l3=[]
for i in l1:
    if i%2!=0:
        l3.append(i)
for j in l2:
    if j%2==0:
        l3.append(j)
        
print(l3)
Output : [1, 3, 7, 9, 45, 4, 88, 40, 78]
"""
#
"""
Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

num1 = int(input("Enter number : "))
reverse = 0
while num1>0:
    reminder = num1 % 10

    num1 = num1//10
    print(reminder,end =" ")

Output :
Enter number : 1234567
"""
#7 6 5 4 3 2 1
"""
For example, suppose the taxable income is 45000, and the income tax payable is
10000*0% + 10000*10%  + 25000*20% = $6000.
"""
"""
num1 = int(input("Enter Salary : "))
num2 = num1
if num1<10000:
    tax = 0
elif num1==10000:
    tax = (10000*10)/100
else:
    tax = 0
    tax = (10000*10)/100

    num1 = num1-20000
    tax = tax + (num1*20)/100

print(f"Amount is : {num2} tax is {tax} ")

Enter Salary : 45000
Amount is : 45000 tax is 6000.0 
"""
#Exercise 13: Print multiplication table from 1 to 10
"""
for i in range(1,11):
    for j in range(1,11):
        print(i * j, end = " ")
    print("")
    
Output
1 2 3 4 5 6 7 8 9 10 
2 4 6 8 10 12 14 16 18 20 
3 6 9 12 15 18 21 24 27 30 
4 8 12 16 20 24 28 32 36 40 
5 10 15 20 25 30 35 40 45 50 
6 12 18 24 30 36 42 48 54 60 
7 14 21 28 35 42 49 56 63 70 
8 16 24 32 40 48 56 64 72 80 
9 18 27 36 45 54 63 72 81 90 
10 20 30 40 50 60 70 80 90 100 

"""

#Exercise 14: Print a downward Half-Pyramid Pattern of Star
"""
for i in range(5,0,-1):
    print('* '*i, end=" ")
    print("")
Output
* * * * *  
* * * *  
* * *  
* *  
*  
"""

#Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
"""
n1 = int(input("Enter base: "))
n2 = int(input("Enter exp : "))
print(n1**n2)
Output : 
Enter base: 7
Enter exp : 3
343
"""
