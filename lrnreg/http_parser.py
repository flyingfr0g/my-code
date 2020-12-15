#!/usr/bin/env python3

import urllib.request

import re

print("where should we search? ")

url = input()

print("Great! So we will try to open this url " + str(url) + " to search for the phrase.")
#print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")

searchFor = input()

searchme = urllib.request.urlopen(url).read().decode("utf-8")

if re.search(searchFor, searchme):
    print("Fround a match!")
else:
    print("No matches found" )

