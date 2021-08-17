#Program to get the median of a list of numbers
n = int(input("Please enter the number of numbers you wish to enter"))
l = []
for _ in range(n):
    l.append(int(input("Please enter a number")))
    l.sort()

median = [l[int(n - 1 / 2)] if n % 2 != 0 else (l[int(n/2)] + l[int(n/2) - 1]) / 2]
print(median.pop())
