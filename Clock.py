from Counters import Time
class Clock:
    """
    Our implementation of the Clock class
    """
    def getTime(self):
        # calling getTime
        return Time.getTime()
        # returns the current time in the form of a tuple
    
    def setTime(self, timetuple):
        # calls the setTime class method from the Time class and passes the provided timetuple to it.
        Time.setTime(timetuple)

    def getHour(self):
        # return the current hour as an int 
        timetuple = Time.getTime()
        return timetuple[3]

    def setHour(self, hour):
        # It first retrieves the current time as a tuple.
        timetuple = Time.getTime() 
        # Converts the tuple to a list to allow modification.
        timelist = list(timetuple)  
        # Updates the hour in the list.
        timelist[3] = hour       
        # Sets the updated time list back to the system's RTC using the setTime method from the Time class
        Time.setTime(timelist)   

    def getMinute(self):
        # Retrieves the current minute from the system's real-time clock (RTC)
        # It first calls the Time.getTime() method to get the current time as a tuple.
        timetuple = Time.getTime()
        # It then extracts and returns the minute value (the fifth element of the tuple).
        return timetuple[4]
        # The method returns the current minute as an integer.
    
    def setMinute(self, minute):
        # sets the current minute on the system's real-time clock (RTC).
        # It first retrieves the current time as a tuple.
        timetuple = Time.getTime() 
        # Converts the tuple to a list to allow modification.
        timelist = list(timetuple) 
        # Updates the minute in the list.
        timelist[4] = minute      
        # Sets the updated time list back to the system's RTC using the setTime method from the Time class.
        Time.setTime(timelist)   
        # The real-time clock on the system is updated with the new minute value while 
        # keeping the other components (year, month, date, hour, second, weekday, yearday) unchanged   

    def getDate(self):
        # retrieves the current date (day of the month) from the system's real-time clock (RTC)
        # It first calls the Time.getTime() method to get the current time as a tuple.
        # It then extracts and returns the date value (the third element of the tuple).
        timetuple = Time.getTime()
        return timetuple[2]
        # The method returns the current date (day of the month) as an integer.
    
    def setDate(self, date):
        # sets the current date (day of the month) on the system's real-time clock (RTC)
        timetuple = Time.getTime() 
        timelist = list(timetuple) 
        timelist[2] = date         
        Time.setTime(timelist)  
        # The real-time clock on the system is updated with the new date value 
        # while keeping the other components (year, month, hour, minute, second,
        # weekday, yearday) unchanged.   
    
    def getMonth(self):
        # retrieves the current month from the system's real-time clock (RTC).
        timetuple = Time.getTime()  
        return timetuple[1]
        # The method returns the current month as an integer.

    def setMonth(self, month):
        # sets the current month on the system's real-time clock (RTC)
        timetuple = Time.getTime() 
        timelist = list(timetuple) 
        timelist[1] = month         
        Time.setTime(timelist)  
        # The real-time clock on the system is updated with the new month 
        # value while keeping the other components (year, date, hour, minute, 
        # second, weekday, yearday) unchanged.