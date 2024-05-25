from Displays import LCDDisplay
from Button import *
from Clock import *

class ClockController:
    """ Our implementation of the Clock Controller
        4 buttons for setting month, date, hour, min
        LCD display to show the time
    """

    def __init__(self): 
        self._clock = Clock()
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._buttons = [Button(10, 'white', buttonhandler=self),
                         Button(11, 'red', buttonhandler=self),
                         Button(12, 'yellow', buttonhandler=self),
                         Button(13, 'blue', buttonhandler=self)]
        self._month_names = {
            1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
            7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
        }

    def _getDaysInMonth(self, month):
        # create a dictionary for how many days are in each month
        month_days = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        return month_days.get(month, 30)

    def showTime(self):
        # show the time on the display
        (year, month, date, hour, minute, sec, wd, yd) = self._clock.getTime()
        month_name = self._month_names[month]
        self._display.showText(f'Time is {hour:02d}:{minute:02d}:{sec:02d}\n{date:02d} {month_name}   ')

    def buttonPressed(self, name):
        # Below are actions designed to handle the event when a button is pressed 
        # When any of the four colored buttons are pressed, the _incrementMonth 
        # method is executed, which increments the current month value stored in the Clock instance.                
        if name == 'white':
            self._incrementMonth()
            # It checks if the pressed button's name is 'white'.
            # If the button's name is 'white', it calls the 
            # _incrementMonth method to increment the current month.
        if name == 'red':
            self._incrementDate()
            # It checks if the pressed button's name is 'red'.
            # If the button's name is 'white', it calls the 
            # _incrementMonth method to increment the current month.

        if name == 'yellow':
            self._incrementHour()
            # It checks if the pressed button's name is 'yellow'.
            # If the button's name is 'white', it calls the 
            # _incrementMonth method to increment the current month.

        if name == 'blue':
            self._incrementMinute()
            # It checks if the pressed button's name is 'blue'.
            # If the button's name is 'white', it calls the 
            # _incrementMonth method to increment the current month.

    def buttonReleased(self, name):
        pass  
        # No action is executed when button is released

    def _incrementMonth(self):
        # Increments the current month in the Clock instance by one
        month = self._clock.getMonth()
        # Retrieves the current month using the getMonth method of the Clock instance
        if month == 12:
            self._clock.setMonth(1)
            # If the current month is December (12), it resets the month to January (1)
        else:
            self._clock.setMonth(month + 1)
            #  Else it increments the current month by one
        # The method updates the month in the Clock instance, 
        # wrapping around from December to January

    def _incrementDate(self):
        # Increments the current date (day of the month) in the Clock instance by one
        # Handling the transition from the last day of the month to the first day of the next month
        month, date = self._clock.getMonth(), self._clock.getDate()
        # Retrieves the current month and date using the getMonth and getDate methods of the Clock instance
        max_days = self._getDaysInMonth(month)
        # It then retrieves the maximum number of days in the current month using the _getDaysInMonth method
        if date >= max_days:
            self._clock.setDate(1)
            # If the current date is the last day of the month, it resets the date to the first day of the next month
        else:
            self._clock.setDate(date + 1)
            # Else, it increments the current date by one

    def _incrementHour(self):
        hour = self._clock.getHour()
        if hour == 23:
            self._clock.setHour(0)
        else:
            self._clock.setHour(hour + 1)

    def _incrementMinute(self):
        minute = self._clock.getMinute()
        if minute == 59:
            self._clock.setMinute(0)
        else:
            self._clock.setMinute(minute + 1)
