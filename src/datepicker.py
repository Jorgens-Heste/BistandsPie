
#Copied from https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
import time


class DatePicker(object):


    @staticmethod
    def strTimeProp(start, end, format, prop):
        """Get a time at a proportion of a range of two formatted times.

        start and end should be strings specifying times formated in the
        given format (strftime-style), giving an interval [start, end].
        prop specifies how a proportion of the interval to be taken after
        start.  The returned time will be in the specified format.
        """

        stime = time.mktime(time.strptime(start, format))
        etime = time.mktime(time.strptime(end, format))

        ptime = stime + prop * (etime - stime)

        return time.strftime(format, time.localtime(ptime))

    @staticmethod
    def randomDate(start, end, prop):
        return DatePicker.strTimeProp(start, end, '%d/%m/%Y', prop)

