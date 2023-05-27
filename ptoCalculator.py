import calendar
import math

#start date in months, days, year
startDate = str(input("Start date (Ex. 02/19/2018, Month/Day/Year): "))
startDate = [int(startDate[:2]), int(startDate[3:5]), int(startDate[6:])]

endDate = input("End date (Ex. 02/19/2018, Month/Day/Year): ")
endDate = [int(endDate[:2]), int(endDate[3:5]), int(endDate[6:])]

#creating a calendar data set
calendardata = calendar.Calendar()

#PTO hours --> PTO days
PTOhoursLeft = 0
def PTOtoDays():
    PTOhours = int(input('How Many PTO Hours Does Employee Have Left? (ex. 5): '))
    PTOdays = PTOhours % 8
    PTOhoursLeft = PTOhours - (PTOdays * 8)
    return(PTOhours, PTOdays, PTOhoursLeft)

#Taking the Start and End date, grabbing all of the months in between them


def monthdayextractor():
    startCounter = startDate[0]
    AllDaysList = []
    while (startCounter % 12) != (endDate[0] + 1):
        HoldingList = []
        for day in calendardata.itermonthdays2(startDate[2] + (math.floor(startCounter/12) ) , startCounter):
            HoldingList.append(day)
        AllDaysList.append(HoldingList)
    print(AllDaysList)

monthdayextractor()
