#! /usr/bin/python3
import os
import time
import webbrowser

x='''
  press1 to check date and time
  press2 to create a file
  press3 to create a directory
  press4 to search something on google 
  press5 to logout from your system
  press6 to shutdown your system
  press7 to check internet connection in your system
  press8 to login into whatsapp on browser
  press9 to check all connected ip in your network
  press10 to check the ip address 
   '''
print x                                               #printing the menu

choice=int(raw_input("please enter your choice"))     #taking the choice of user

if choice==1 :
  data=time.ctime()
  print "time : "  
  print data.split()[3]
  print "date :"
  print data.split()[0:3]
elif choice==2 :
  f_name=raw_input("enter the name of file") 
  os.system(' sudo gedit '+ f_name )
elif choice==3 :
  dir_name=raw_input("enter the name of directory")
  os.system('mkdir '+ dir_name)
elif choice==4 :
  msg=raw_input("type to search")
  webbrowser.open_new_tab('https://www.google.com/search?q='+msg)
elif choice==5 :
  print 'hey you want to logout'
  os.system('gnome-session-quit')
elif choice==6 :
  os.system('poweroff')
elif choice==7 :
  os.system('ping www.google.com')
elif choice==9 :
  print os.system('sudo nmap -v -sn 192.168.43.0/24')
else :
  print 'your ip address is:'
  print os.system('hostname -I')




