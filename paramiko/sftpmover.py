#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

## where to connect to
t = paramiko.Transport (input("IP address: "), 22) ## IP and port
username = input("Username: ")
password = input("Password: ")

## how to connect (see other labs on using id_rsa private/public keypairs)
t.connect(username=(username), password=(password))

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
for x in os.listdir("/home/student/mycode/paramiko/filestocopy/"): # iterate on directory contents
  if not os.path.isdir("/home/student/mycode.paramiko/filestocopy/"+x): # filter everything that is NOT a directory
    sftp.put("/home/student/mycode/paramiko/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connection
sftp.close() # close the connection
