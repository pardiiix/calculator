# -*- coding: utf-8 -*-
"""
Created on August 17th, 2017

@author: Pardis Ranjbar
E-mail: pardis.ranjbar@gmail.com
#==============================================================================
# This code gets numbers from user and calculates what to do with them.
#==============================================================================
"""
import time
def add(x1,x2): #defines a function of adding two numbers
    print('the sum is=',x1+x2, sep='') #the seperator makes sure there is no space between str and the command
def minus(x1,x2):
    print('the subtraction is=',x1-x2, sep='')
def div(x1,x2):
    print('the division is=',x1/x2, sep='')
def multiply(x1,x2):
    print('the multiplication is=',x1*x2, sep='')
    
x1=input('enter a number:\n')#gets the first number from user
x2=input('enter another number:\n')#gets the second number from user
the_action=input('what do you want to do with these numbers? type +, -, * or /:\n') #asks what to do with the numbers
while x1.isnumeric()==True and x2.isnumeric()==True: #checks if x1 and x2 were numbers
    if the_action=='+':
        add(int(x1),int(x2))
        break #breaks the while loop and the calculation is done
    elif the_action=='-':
        minus(int(x1),int(x2))
        break
    elif the_action=='*':
        multiply(int(x1), int(x2))
        break
    elif the_action=='/':
        try:
            div(int(x1),int(x2))
            break
        except ZeroDivisionError: #if user enters zero as x2:
            print('The Divisor cannot be zero')
            break
    else:#if user enters and action other than given
        print('Choose one of the given symbols: (+-*/)')
        time.sleep(2)#a two-second interuption
        the_action=input('what do you want to do with these numbers? type +, -, * or /:\n')
