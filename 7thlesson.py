#1
# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper
#
# @my_decorator
# def hello():
#     print("Hello, Wolrd!")
# hello()


#2
# def decorator_function(original_function):
#     def wrapper_function():
#         print("Wrapper executed this before {}". format(original_function.__name__))
#         return original_function()
#     return wrapper_function
#
# @decorator_function
# def display():
#     print("Display function excuted")
# display()


#3
# def log_function_call(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function {func.__name__} was called with arguments {args} and keyboard arguments {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper
# @log_function_call
# def add(a,b):
#     return a+b
# @log_function_call
# def multiply(a,b):
#     return a*b
# add(5,10)
# multiply(2,10)

#4
# def print_output(should_print):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args,**kwargs)
#             if should_print:
#                 print(f"Function output: {result}")
#             return result
#         return wrapper
#     return decorator
#
# @print_output(should_print=True)
# def add (a,b):
#     return a+b
# add(5,3)

#5
# def decorator_one(func):
#     def wrapper():
#         print("Decorator One")
#         return func()
#     return wrapper
# def decorator_two(func):
#     def wrapper():
#         print("Decorator Two")
#         return func()
#     return wrapper
# @decorator_one
# @decorator_two
# def hello():
#     print("Hell, Wolrd!")
# hello()

#6
# class MyClass:
#     @staticmethod
#     def greet(name):
#         return f"Hello, {name}"
# print(MyClass.greet("Yusufjon"))

#7
# def check_arguments(expected):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if len(args) !=expected:
#                 print(f"Warning: Expected {expected} arguments, but got {len(args)}")
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
# @check_arguments(2)
# def divide(a,b):
#     return a/b
# divide(4,2)
# divide(4)

#class project
#8
# import time
#
# def time_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Time taken by {func.__name__}: {end_time - start_time:.6f} seconds")
#         return result
#     return wrapper
#
# # Example usage
# @time_decorator
# def sample_function():
#     time.sleep(2)
#     print("Function execution completed!")
#
#
# sample_function()

#9
# def role_required(required_role):
#     def decorator(func):
#         def wrapper(user_role, *args, **kwargs):
#             if user_role == required_role:
#                 return func(*args, **kwargs)
#             else:
#                 print(f"Access denied: {user_role} does not have permission to execute {func.__name__}")
#         return wrapper
#     return decorator
#
# @role_required("admin")
# def admin_function():
#     print("Admin function executed successfully!")
#
# @role_required("user")
# def user_function():
#     print("User function executed successfully!")
#
# # Test cases
# admin_function("admin")
# admin_function("user")
# user_function("user")
# user_function("admin")

#10
def cache_decorator(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print("Returning cached result for", args)
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper

# Example usage
@cache_decorator
def expensive_function(x, y):
    print(f"Computing result for {x}, {y}...")
    return x * y

# Test cases
print(expensive_function(3, 4))
print(expensive_function(3, 4))
print(expensive_function(5, 6))
print(expensive_function(5, 6))