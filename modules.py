#there are three types  of modules

#own modules
#thirdy party modules
#python modules

#example python modules. see below

import datetime #here we are importing python module.

print(datetime.date.today())#if you want how to do see the documentation. this show the current date.


#another example. 

#another way of call methods.

from datetime import timedelta

print(timedelta(minutes=100)) # you dont have to call datatime, you call direclty de module.
# print(datetime.timedelta(minutes=100))


#another example

from datetime import timedelta, date #we have added more modules to avoid call any time

print(date.today())


#my own module, verify from fmath.py

import fmath
fmath.substract(1, 2)

#another example

from fmath import substract, add

substract(5, 6)
add(4, 5)

#note with pip command you can install thirdy part modules

