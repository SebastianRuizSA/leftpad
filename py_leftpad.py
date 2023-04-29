#!/usr/bin/env_python

def leftpad(strng, leng, char):
    new_string = []
    if char is None:
        char = ' '
    for i in range(leng):
        new_string.append(char)
    for st in strng:
        new_string.append(st)
    new_new_string = ''.join([elem for elem in new_string])
    print(new_new_string)
    
leftpad('string', 6, 'h')
