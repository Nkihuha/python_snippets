# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:07:05 2019

@author: nkihuha
"""

# Write a program that prints the longest substring of s in which the
# letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
# then your program should print
# Longest substring in alphabetical order is: beggh
#

string = input("Please enter the main string :",)

#pointer to keep the second of the string
count =1
#hold the current string val
temp=string[0]

longest = ""


#loop through the string, comparing if prev is larger than current

while count<len(string):  
    if(string[count-1]<=string[count]):        
        temp+=string[count]
    else: # sequence is broken, store the current as the longest if it is larger than current longest        
        if(len(longest)<len(temp)):
            longest=temp
        temp=string[count] #set new sequence as current character in the string
    count+=1
        
     
print("Longest substring in alphabetical order is ",longest)
