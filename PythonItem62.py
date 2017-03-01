# -*- coding: cp1252 -*-

##Title: Datetime – Python 2.7 – IDLE
##
##Scenario: The company you work for just opened two new branches. One is in New York City,
##the other in London. They need a very simple program to find out if the branches are open or
##closed based on the current time of the Headquarters here in Portland. The hours of both
##branches are 9:00AM - 9:00PM in their own time zone.
##
##What is asked of you:
##Create code that will use the current time of the Portland HQ to find out the time in the NYC &
##London branches, then compare that time with the branches hours to see if they are open or
##closed.
##Print out if each of the two branches are open or closed.

import time
from time import gmtime, strftime

branches = (("Portland",-8),("New York",-5),("London",0))

for i in branches:
   hour = int(time.strftime("%H",gmtime())) + int(i[1])
   minute = int(time.strftime("%M"))
   localTime = (str(hour) + ":" + str(minute))
   if (hour < 21 and hour > 9):
      state = "open"
   else:
      state = "closed"
   print(i[0]+" branch:")
   print("Local time is " + str(localTime))
   print("They are currently " + state + "\n")


   
