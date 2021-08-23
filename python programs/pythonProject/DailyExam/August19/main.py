# How to remove a simple file in OS?
# There are two ways to remove a file. First way is where you can use os module to unlink a path. os.unlink("filename")
# The second way is where you can use send2trash module
import os

# os.unlink("D:\\SQL Videos\\fileiwantdelete.txt")

# The only difference is send2trash sends it to recyle bin instead of complete deletion
import send2trash

# send2trash.send2trash("D:\\SQL Videos\\filetodelete.txt")
# 11.How to remove a folder irrespective of files present or not permanently? shutil.rmtree() removes the folders and its contents completely
import shutil

#shutil.rmtree("E:\\Fodlertodelete")

#8.How to list files in a directory in python?
#print(os.getcwd())

#10.How to remove a directory in OS?.os.rmdir() but this works only if the directory is empty
#os.rmdir("E:\\removefolder")

#20.Program to obtain the leap year?
#  An year is a leap year if that year is divisible and not divisble 100 and incase divisble by 100 it should be divisble by 400 also

# year=int(input("Enter the year which you want to check whether its a leap year or not\n"))
#
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("Its a leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Its a leap year")
# else:
#     print("Its not a leap year")

#18.What is the significance of counter and where is it available? Counter is available in collections module and its used to obtain the count of items in a list or dictionry

# from collections import Counter
# l=[91,92,43,12.76,12,31,91,92]
# print(Counter(l))

# 15.Write a program to get the febinooici series given a range of number?

# def get_febinoicci(n):
#     a=1
#     b=1
#     for _ in range(n):
#         yield a
#         a,b=b,a+b
#
# for n in get_febinoicci(10):
#     print(n)

#7.How to list directory in python?
# import os
# print(os.listdir("D:\\"))
#17.Write a program to get the cubes of first n natural numbers?

# def cubes(n):
#     for i in range(1,n+1):
#         yield i**3
#
# for i in cubes(10):
#     print(i)
