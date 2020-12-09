#!/usr/bin/env python3
# Author: alexander.b.scull@gmail.com
# Check hostname given by user

## Collect input from user
hostname = input("What value should we set for hostname?")

## use lower to see make sure that case doesnt mess up the test
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

## Always print out to the user
print("Exiting the script")
