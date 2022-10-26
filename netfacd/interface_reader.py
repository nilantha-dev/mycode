#!/usr/bin/env python3
import netifaces
print(netifaces.interfaces())
for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print('MAC: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) # prints the MAC address
        print('IP: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) # prints the IP address
    except:
        print('Could not collect adapter information')

