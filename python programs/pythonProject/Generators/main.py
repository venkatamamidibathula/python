# Python Program to get the febinoicci series

def get_febinoicci_series(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


n = int(input("Enter the range of febinoicci numbers you want to enter\n"))
for number in get_febinoicci_series(n):
    print(number)


