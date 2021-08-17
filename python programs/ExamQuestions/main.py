import random

with open('questions.txt', 'r') as myfile:
    contents = random.sample(myfile.readlines(), 10)
    x = [x.removesuffix('\n') for x in contents]

for _ in range(10):
    y=x.pop()
    print(y[y.index(".")+1::])


