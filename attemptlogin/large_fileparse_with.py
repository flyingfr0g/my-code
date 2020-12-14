#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails

#parse keysotne.common.wgsi and return number of successfull login attepmts
loginsuccess = 0 #counter for successfull logins

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            print(line.split(" ")[-1]) #this will show us the ip addresses associated with the failed logins
        elif not "- - - - -] Authorization failed" in line:
            loginsuccess += 1 #this add 1 to the successfull logins counter
            print(line)
            # You had it say loginsuccess =+ 1, which is assigning that value to 1, every single time this is true. Even though it assigned it 51 times, it still was always assigned to 1. ok yeah i see what happened. i had the   = and + switched which made it so that it always equaled 1.
print("The number of failed log in attempts is: ", loginfail)

print("The number of successfull login attempts is: ", loginsuccess)

