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
        for day in calendardata.itermonthdays2(startDate[2] + (math.floor(startCounter/12) ) , (startCounter % 12)):
            HoldingList.append(day)
        AllDaysList.append(HoldingList)
        startCounter += 1
    return(AllDaysList)



#taking the amount of days in those months and dividing them into bi monthly pay segments

def BimonthlyCreator(weeksOfMonths):
    CleanDaysOfMonth = []
    Holder = []
    BimonthlyPeriods = []
    for month in weeksOfMonths:
        for day in month:
            if day[0] != 0:
                Holder.append(day)
        CleanDaysOfMonth.append(Holder)
    for month in CleanDaysOfMonth:
        BimonthlyPeriods.append(month[:15])
        BimonthlyPeriods.append(month[15:])
        
    return(BimonthlyPeriods)



def BimonthlyWeekDaysCreator(BimonthlyPeriods):
    CleanDaysOfBimonthly = []
    BimonthlyWeekdays = []
    for Bimonthly in BimonthlyPeriods:
        Holder = []
        for day in Bimonthly:
            if (day[1] < 5):
                Holder.append(day)
        CleanDaysOfBimonthly.append(Holder)      
    return(CleanDaysOfBimonthly)




#print(BimonthlyCreator(monthdayextractor()))
print(BimonthlyWeekDaysCreator(BimonthlyCreator(monthdayextractor())))