# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 12:04:11 2018

@author: Work Station #2
"""

users = {'lewis':'passwordL','john':'passwordJ','mark':'passwordM'}

#Our main function
def securitycheck():
    username = input(str('Please enter your username: '))
    if username in users.keys():
            attempts = 0
            allowance = 3
            while attempts < 3:
                password = input(str('Please enter your password. You have ' + str(allowance) + ' attempts remaining: '))
                attempts += 1
                allowance -= 1
                if password in users[username]:
                    print('Access granted')
                    break
                else:
                    print('Password denied')
    else:
        print('Sorry this username is not recognised, please try again')

