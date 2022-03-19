# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:18:53 2022

@author: User
"""

import http.client

print("The program returns a list of method if OPTIONS is enabled")
HOST = input("enter the host's ip")
PORT= input("enter the port")

if (PORT == ""):
    PORT = 80
    
try:
    #the http.client module defines classes that implement the client side of HTTP and HTTPS protocols
    connection = http.client.HTTPConnection(HOST, PORT)
    #sending http request , the first parameter is the method, the second is the url
    connection.request('OPTIONS' , '/')
    response = connection.getresponse()
    print("The enabled methods are", response.getheader('allow'))
except ConnectionRefusedError:
    print("connection failed")