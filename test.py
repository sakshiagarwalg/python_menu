#! /usr/bin/pyhton2

import os

x=int(raw_input("please enter your age"))
if (x==14) or (x<14) :
  print"kid"
elif (x>14) or (x<18) :
  print"you are an adolescent"
elif (x==18) or (x<40) :
  print"adult & young"
elif (x>=41) and (x<60) :
  print"you are at middle adulthood and aging"
elif (x>60) or (x<85) :
  print"aged"
else :
  print"congrats! you have lived an good number of the age"
