#-*-coding:utf-8-*-
# from functools import wraps

def new_decorator(func):
    def wrapTheFunction():
        print("work before executing a_func()")
        func()
        print("work after executing a_func()")

    return wrapTheFunction


def func_requiring_decoration():
    print("function which needs some decoration")


func_requiring_decoration()     # outputs: "I am the function which needs some decoration"

function_requiring_decoration = new_decorator(func_requiring_decoration)
# now func_requiring_decoration is wrapped by wrapTheFunction()

function_requiring_decoration()
# outputs: work before executing func()
#          function which needs some decoration
#          work after executing func()

'''
    Using @
'''
print(' ')
@new_decorator
def a_func_requiring_decoration():
    """Decorate me!"""
    print("I am the function which needs some decoration")

a_func_requiring_decoration()
#outputs: I am doing some boring work before executing a_func()
#         I am the function which needs some decoration to remove my foul smell
#         I am doing some boring work after executing a_func()

# @a_new_decorator is a short way of saying: a_function_requiring_decoration = new_decorator(a_func_requiring_decoration)

print(a_func_requiring_decoration.__name__)     # Output: wrapTheFunction   [Problem !!!]


'''
    Right way Using @
        @wraps
'''
print(' ')
from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("before executing a_func()")
        a_func()
        print("after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    """Decorate me!"""
    print("function which needs some decoration")

print(a_function_requiring_decoration.__name__)     # Output: a_function_requiring_decoration


'''
    Application: Authorization
'''
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated


'''
    Application: logging
'''
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x

result = addition_func(4)   # Output: addition_func was called



'''
    Decorators with Arguments: Nesting a Decorator Within a Function

        --- create a wrapper which lets us specify a logfile to output to.
'''
def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # Open the logfile and append
            with open(logfile, 'a') as opened_file:     # log to the specified logfile
                opened_file.write(log_string + '\n')
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()   # Output: myfunc1 was called
# A file called out.log now exists, with the above string

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()   # Output: myfunc2 was called
# A file called func2.log now exists, with the above string



'''
    Decorators with Arguments: Decorator Classes

    --- Now we have our logit decorator in production, but when some parts of our application are considered critical, failure might be something that needs more immediate attention. Let’s say sometimes you want to just log to a file. Other times you want an email sent, so the problem is brought to your attention, and still keep a log for your own records. This is a case for using inheritence, but so far we’ve only seen functions being used to build decorators.

    ---Classes can also be used to build decorators.
'''

class logit(object):

    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        print(log_string)
        # Open the logfile and append
        with open(self._logfile, 'a') as opened_file:   # log to the specified logfile
            opened_file.write(log_string + '\n')
        self.notify()    # send a notification

        return self.func(*args)     # return base func

    def notify(self):
        # logit only logs, no more
        pass
# This implementation has an additional advantage of being much cleaner than the nested function approach, and wrapping a function still will use the same syntax as before:

logit._logfile = 'out2.log' # if change log file
@logit
def myfunc1():
    pass

myfunc1()   # Output: myfunc1 was called

# Now, let’s subclass logit to add email functionality

class email_logit(logit):
    '''
    A logit implementation for sending emails to admins
    when the function is called.
    '''
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # Send an email to self.email
        # Will not be implemented here
        pass
