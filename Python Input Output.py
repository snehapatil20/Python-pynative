#Write a program to accept two numbers from the user and calculate multiplication
"""
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = num1 * num2
print("Multiplication Of num1 and num2 : ",num3)
Output :
Enter number 1 : 45
Enter number 2 : 23
Multiplication Of num1 and num2 :  1035
"""
#Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
"""
n1 ="Name"
n2 = "Is"
n3 = "James"

print(f"{n1}**{n2}**{n3}")
Output : 
Name**Is**James
"""
#Exercise 3: Convert Decimal number to octal using print() output formatting
"""
num1 = 8
print(oct(num1))
Output : 
0o10
"""
#Exercise 4: Display float number with 2 decimal places using print()
"""
num1 = 3456.678888
print("%.2f" %num1)
Output: 
3456.68
"""
#Exercise 5: Accept a list of 5 float numbers as an input from the user
"""
l1 = eval(input("Enter list of float numbers  : "))
print(type(l1))
print(l1)
Output : 
Enter list of float numbers  : [1.344,5.3455,89.56,67.45]
<class 'list'>
[1.344, 5.3455, 89.56, 67.45]
"""
#Exercise 6: Write all content of a given file into a new file by skipping line number 5 =

#f = open(r"F:\Hakim Sir Assignment\file\s1.txt",'x')
#f.write("My name is sneha sambhaji patil, My fav colour is blue")
"""
f = open(r"F:\Assignment_all\file\s1.txt",'w')
f.write("File is over written , my name is sneha ")
f = open(r"F:\Assignment_all\file\s1.txt",'a')
f.write("My brother name is shubham sambhaji patil")
import os
print(os.listdir())
print(os.path.isfile("raw1.py"))

with open(r"F:\Assignment_all\file\s1.txt",'a') as f1 :
    f1.write("Helllooooo")
c1 = 0
with open(r"F:\Assignment_all\file\s2.txt",'w') as f2 :
    f2.writelines(["Line1\n","Line2\n","Line3\n","Line4\n","Line5\n"])
    f2.close()
with  open(r"F:\Assignment_all\file\s2.txt", 'r') as f2:
    r1 = f2.readlines()
    f2.close()
with open(r"F:\Assignment_all\file\s3.txt", 'w') as f3:
    for i in r1:
        if c1 == 3:
            c1=c1+1
            continue

        else:
           f3.write(i)
        c1 = c1 + 1
"""
#Exercise 7: Accept any three string from one input() call
"""
s1 , s2, s3 = input("Enter String: ").split()
print(s1)
print(s2)
print(s3)
"""
#Exercise 8: Format variables using a string.format() method.
"""
quantity = 5
price = 450
print("Total Money = {a}  Quantity={b} Price ={c}".format(a=quantity*price,b=quantity,c = price))
"""
#Exercise 9: Check file is empty or not
"""
f1 = open(r"F:\Assignment_all\file\s3.txt", 'w')
f2 = open(r"F:\Assignment_all\file\s3.txt", 'r')
s1 =f2.readline()
if s1 == "":
    print("File is empty")
else:
    print("File is not empty")
"""
#Exercise 10: Read line number 4 from the following file
"""
with open(r"F:\Assignment_all\file\s3.txt", 'w') as f1:
    f1.write("line1\n")
    f1.write("line2\n")
    f1.write("line3\n")
    f1.write("line4\n")
    f1.write("line5")
count1=0
with open(r"F:\Assignment_all\file\s3.txt", 'r') as f1:
    s1 = f1.readlines()
    print(s1[3])
"""




