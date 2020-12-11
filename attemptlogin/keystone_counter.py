#!usr/bin/env python3
# this script will parse the file we are looking at and return the number of failed lgin attempts

loginfail = 0 #counter for fails

#the next line opens the file we want to parse

keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")

#the next line will turn the file into a list of lines in memory

keystone_file_lines=keystone_file.readlines()

#the next line will create a loop of the lines

for line in keystone_file_lines:
    #this if statement will find our "failure pattern"
    if "- - - - -] Authorization failed" in line:
        loginfail += 1 #this adds 1 to our login fail counter for each time we find our "fail pattern"
print("The nuber of failed log in attempts is: ", loginfail)
keystone_file.close() #this closes the file for us
