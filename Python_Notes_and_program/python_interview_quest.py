#decorator:
def my_dec(func):
    print("hello")
    def inside():
        print("before calling the function")
        func()
        print("After calling the function")
    return inside

@my_dec
def outside_fn():
    print("hi")

print(outside_fn())

##decorator logging
def dec_log(func):
    def wrapper(*args,**kwargs):
        print(f"Starting '{func.__name__}' function")
        result = func(*args, **kwargs)
        print(f"Finished '{func.__name__}' function")
        return result
    return wrapper

@dec_log
def process_data(data):
    print("Processing data...")
    return [x * 2 for x in data]

result = process_data([1, 2, 3])
print("Result:", result)


