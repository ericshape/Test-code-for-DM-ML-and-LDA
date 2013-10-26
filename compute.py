#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Ji Wang on 2012-11-12.
Copyright (c) 2012 Ji Wang. All rights reserved.
"""

# calculate the area of triangle
# computes the area of a triangle
def triangle_area(base, height):    # header - ends in colon
    time = base * height
    print time
    area = (1/2.0) * base * height  # body - all of body is indented
    return area                     # body - return outputs value

a1 = triangle_area(3, 8)
print a1
a2 = triangle_area(14, 2)
print a2

# converts fahrenheit to celsius
def fahrenheit2celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# test!!!
c1 = fahrenheit2celsius(32)
c2 = fahrenheit2celsius(212)
print c1, c2

# converts fahrenheit to kelvin
def fahrenheit2kelvin(fahrenheit):
    celsius = fahrenheit2celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

# test!!!
k1 = fahrenheit2kelvin(32)
k2 = fahrenheit2kelvin(212)
print k1, k2

# prints hello, world!
def hello():
    print "Hello, world!"

# test!!!
hello()      # call to hello prints "Hello, world!"
h = hello()  # call to hello prints "Hello, world!" a second time
print h      # prints None since there was no return value


num = 49
tens = num // 10
ones = num % 10
print tens, ones
print 10*tens+ones




def great(friend, money):
	if friend:
		print "Hi"
		money = money +10
	return money

money = 15

money = great(True, money)
print "Money:", money
print ""









