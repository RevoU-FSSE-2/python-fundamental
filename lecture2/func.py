# def greet(): # void
#     print("Hello, world!")

# def sum_void(a, b):
#     result = a + b

#     return a + b

# def sum_with_default(a, b=1):
#     return a + b

# greet()
# hasil_intfloat = sum(1, 1.2)
# hasil_intint = sum(1, 2)
# hasil_strstr = sum("Hello", "World")


# var_x = 4
# var_y = 1
# hasil_default = sum_with_default(1)
# hasil_overide_default = sum_with_default(var_y,var_x)
# sum(a=1, b=2)
# sum(b=2, a=1)         # this optional
# variable_hasil = sum_with_default(var_y)
# variable_hasil_void = sum_void(var_y, var_x)
# # global variable
# score = 89.6

# def grade(score):
#     score = int(score)


# # *args == (1,2,3)
# # *args == ()

# def sum_all_numbers(*args):
#     result = 0
#     for number in args:
#         result += number
#     return result
# def response_data(**kwargs):
#     print(kwargs["a"], "<< value a")
#     print(kwargs["b"], "<< value b")
#     result = kwargs["a"] + kwargs["b"]
#     return result

# def argkwargs(*args, **kwargs):
#     print(args)
#     print(kwargs)

# response_data(a=1, b=1)
# response_data(x=1, y=1) # key error

# def argsonly(*,jumlah):
#     print(jumlah)


# sum_function = lambda a,b : a + b
# sum_function


## decorator

def my_decorator(func):
      def wrapper():
         print("Something is happening before the function is called.")
         func()
         print("Something is happening after the function is called.")
      return wrapper

def log_decorator(func):
    def wrapper():
        try:
            print("Function is called")
            func()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("Function is done")
    return wrapper

@my_decorator
def full_name():
    name = "John"
    lastname = "Doe"
    fullname = f"{name} {lastname}"
    print(f"My name is {fullname}")

@log_decorator
def sum_with_log_good():
    result = 1 + 2
    print(result)
@log_decorator
def sum_with_log_bad():
    result = 1 + "2"
    print(result)
sum_with_log_good() # its good
sum_with_log_bad() # its bad
