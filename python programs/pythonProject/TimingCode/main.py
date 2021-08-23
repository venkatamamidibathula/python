#
# # Using time elapsed
# import time
#
#
# def func1(n):
#     time_start = time.time()
#     list_num1 = [str(x) for x in range(n)]
#     time_end = time.time()
#     elapsed_time = time_end - time_start
#     print(elapsed_time)
#
#
# def func2(n):
#     time_start = time.time()
#     list_num2 = list(map(str, range(n)))
#     time_end = time.time()
#     elapsed_time = time_end - time_start
#     print(elapsed_time)
#
#
# func1(1000000)
# func2(1000000)
#
#
# Using timeit module. Specifically designed for time code
import timeit

stmt = '''fun(100)'''
setup = '''
def fun(n):
    return [str(x) for x in range(n)]
'''

print(timeit.timeit(stmt,setup,number=10000))

stmt2='''func2(100)'''
setup2='''
def func2(n):
    return list(map(str,range(n)))
'''

print(timeit.timeit(stmt2,setup2,number=10000))
