try:
    print(1/0)
except ZeroDivisionError:
    print('you were trying to divide something by zero')

# Other examples
try:    # it will print the Value Error, And if we use only except without any arguments then it will goint to print the default one.
    a = int("jatin")
except ZeroDivisionError:
    print('you were trying to divide something by zero')
except ValueError:
    print("You were trying to convert a string to an int")

# base class in python for error exception is Exception
try:
    print(1/0)
    a = int("jatin")
except Exception as e:
    print(e) # division by zero

# custom exceptions
# we can raise the exceptions by using the "raise" keyword
try:
    raise Exception("My custom error")
except Exception as e:
    print(e)  # My custom error

# Custom exception class
# class MyException:
#     def __init__(self, message):
#         self.message = message
#
#     def __str__(self):
#         return self.message
#
# try:
#     raise MyException("some error")
# except Exception as e:
#     print(e) # exceptions must derive from BaseException

class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

try:
    raise MyException("some error")
except Exception as e:
    print(e.message) # some error

# Other tips
# else : will always execute if the try block didn't therw any error
# finally: will always execute no matter what

try:
    print("Hello, world!")
    print(10/0)
except:
    print("Ok error occured")
else:
    print("woah")
finally:
    # cleanup code goes inside the finally block
    print("Bye bye world")
