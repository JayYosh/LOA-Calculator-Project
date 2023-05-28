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

#only grabs the weekdays of the bimonthly periods

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


#finds the average pay of each day

def DailyPay(CleanDaysofBimonthly):
    YearlyWage = int(input("Input Yearly Income (ex. 120000. no commas.): "))
    BimonthlyPay = (YearlyWage/24)
    for bimonthlyPeriods in CleanDaysofBimonthly:
        bimonthlyPeriods.append(BimonthlyPay/len(bimonthlyPeriods))
    return(CleanDaysofBimonthly)
     

#Cleans data to ensure the dates are in the start and end period.

def InDatePeriod(CleanDaysofBimonthly):
    if startDate[1] > 15:
        for day in CleanDaysofBimonthly[1][:-1]:
            if day[0] < startDate[1]:
                CleanDaysofBimonthly[1].remove(day)
        CleanDaysofBimonthly.remove(CleanDaysofBimonthly[0])
    if startDate[1] < 15:
        for day in CleanDaysofBimonthly[0][:-1]:
            if day[0] < startDate[1]:
                CleanDaysofBimonthly[0].remove(day)

    if endDate[1] < 15:
        for day in CleanDaysofBimonthly[-2][:-1]:
            if day[0] > endDate[1]:
                CleanDaysofBimonthly[1].remove(day)
        CleanDaysofBimonthly.remove(CleanDaysofBimonthly[-1])
    if endDate[1] > 15:
        for day in CleanDaysofBimonthly[-1][:-1]:
            if day[0] > endDate[1]:
                CleanDaysofBimonthly[-1].remove(day)
    return(CleanDaysofBimonthly)














#print(BimonthlyCreator(monthdayextractor()))
#print(BimonthlyWeekDaysCreator(BimonthlyCreator(monthdayextractor())))
print(InDatePeriod(DailyPay(BimonthlyWeekDaysCreator(BimonthlyCreator(monthdayextractor())))))
