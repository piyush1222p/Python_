#Zip Function:
    #The zip() function takes iterables, aggregates(combine form) them in a tuple, and returns it.
    #The zip() function stops when the shortest input iterable is exhausted.
    #The zip() function is used to merge two or more lists or other iterables into a list
    # of tuples, where the i-th tuple contains the i-th element from each of the argument sequence or iterables.
useraname=["Dude","Bro","Mister"]
useremail=("dude@gmail.com","bro@gmail.com","mister@gmail.com")
users=dict(zip(useraname,useremail))


print(users)
print(type(users))
print(list(users))

for i in users:
    print(i)
print(type(users))

"Output"
for key,value in users.items():
    print(key+": "+value)

"We can also add two or more iterables and return the same value"

#__name__==__main__:

    #1) Module can be run as a standalone program
    #2) Module can be imported as a module in another program
    #3) Python Interpreter sets "special variable",one of which is __name__
    #4) The Python will execute the code found within __main__
    #5) If the module is run as a standalone program, then __name__ is set
    #6) If the module is imported as a module in another program, then __name__
if __name__=="__main__":
    print("This is a standalone program")
else:
    print("This is a module")

#Time Module:
#The time module provides various time-related functions.
#The time module is used to get the current time, delay the execution of a program, and
#to get the time elapsed since the program started.
import time
print(time.time())
#time.sleep(5) #This will pause the execution of the program for 5 seconds
print(time.ctime(0))
#time.ctime() returns a string representing local time
print(time.time())
#time.time() returns the current system time in seconds since the epoch (January 1,1970)
print(time.ctime(time.time()))
#time.ctime() returns a string representing local time
print(time.strftime(time.ctime()))
#time.strftime() returns a string representing the time under the control of an explicit format string
from time import ctime

print(time.ctime())
"Returns the date,time,day with year"
print(time.time())
"Returns the time in seconds"
print(time.strftime(ctime()))
""
print(time.ctime(0))
"Convert a time exposed in seconds since epoch to a readable string, epoch = when your computer thinks time began"
print(time.ctime(time.time()))
"It returns the current value of date,time,day"
time_1=time.localtime()
print(time_1)
"It returns the current date,time,day and etc with positional argument"
print(time.strftime("%B %d %Y %H:%M:%S",time_1))


#Threading:
#The threading module provides a high-level threading API.
#The threading module is used to create threads, which are lightweight processes that can run concurrently with the
#main program.
import threading
#Creating a thread
#A thread is created by creating a Thread object and passing a function to the target parameter.
#The target function is the function that will be executed by the thread.
import time
print(threading.active_count())
print(threading.enumerate())

def wakeup():
    time.sleep(3)
    print("Wake up")
def coffee():
    time.sleep(3)
    print("Going to take a sip")
def study():
    time.sleep(3)
    print("Time to study")
wakeup()
coffee()
study()

print(threading.active_count())
print(threading.enumerate())