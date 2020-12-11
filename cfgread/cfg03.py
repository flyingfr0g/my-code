#!/usr/bin/env python3
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    
## file was just auto closed (no more indenting)

## read the number of lines and print how many there are at the top

#lines = 0

#for line in configlist:
 #   if "\n" in line:
  #      lines += 1
linecount = len(configlist)
print(linecount)


## display list with no "\n"
print(configlist)
