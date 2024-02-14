# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()


def greet(func):
    def mfunc():
        print("Good morning")
        func()
        print("Thanks")
    return mfunc

@greet 
def hello():
    print("Hello World")

hello()