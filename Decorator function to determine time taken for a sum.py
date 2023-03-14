
'''using decorator function,output time taken by a sum function to sum numbers from 100,1000 and another
 function to sum numbers from 1000 to 10000'''


import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        #The wrapper function measures the execution time of the input function using the time.perf_counter() function, which returns the current time in seconds.
        res = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"time taken :{end_time-start_time}seconds")
        return res
    return wrapper

@time_it
def sum_numbers1():
    return sum(range(100,1001))

@time_it
def sum_numbers2():
    return sum(range(1000,10000))

print(sum_numbers1())
print(sum_numbers2())