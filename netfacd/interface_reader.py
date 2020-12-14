#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print('MAC: ', end=' ')
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) #this prints only the MAC address
            print('IP: ', end=' ')
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) #this prints only the IP address
        except:
            print('Could not collect adapter information') #this is an error message

def IP():
    print('IP: ', end=' ')
    print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
IP()

def MAC():
    print('MAC: ', end=' ')
    print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])

MAC()

#while

 #   ask = input('if you are finished please type Q, for IP addresses please type IP, for MAC addresses please type MAC: ")
   # if ask.upper == IP
