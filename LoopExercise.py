#Loop through a Range
#Problem: Write a program that prints all the even numbers from 1 to 20 using a for loop.

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in num:
    if i % 2 == 0:
        print("Even Number", i)