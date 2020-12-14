#!/usr/bin/env python3

from subprocess import call

from subprocess import check_output

call(["ip", "link", "up"])

print("this program will check your interfaces.")

interface = input("enter an interface, such as, ens3: ")

call(["ip", "addr", "show", "dev", interface])

