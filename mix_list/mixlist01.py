#!/usr/bin/env python3
my_list = [ "192.168.0.5", 5060, "UP" ]

#this line prints the first object in the list

print("The first item in the list (IP): " + my_list[0] )

#this line prints the second object in the list

print("The second item in the list (port): " +str(my_list[1]) )

#this line prints the last object in the list

print("The last item in the list (state:) " + my_list[2] )

#the next line is a new list

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#this code will use the second list and show each variable in a creative sentance 

print(f"When I {new_list[5]} into IP addresses {new_list[3]} or {new_list[4]} I am unable to ping ports {new_list[0]}, {new_list[1]}, or {new_list[2]}.")



