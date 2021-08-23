import random


def pythonquestionpaper(path):
    with open(path,'r') as l:
        contents=random.sample(l.readlines(),11)
        x=[x.removesuffix('\n') for x in contents]
    for i in x:
        print(i)

pythonquestionpaper("D:\\python\\python programs\\Python Questions.txt")
