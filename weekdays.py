import calendar
import math

#start date in months, days, year
startDate = str(input("Start date (Ex. mm/nn/yyyy, Month/Day/Year): "))
startDate = [int(startDate[:2]), int(startDate[3:5]), int(startDate[6:])]

endDate = input("End date (Ex. mm/nn/yyyy, Month/Day/Year): ")
endDate = [int(endDate[:2]), int(endDate[3:5]), int(endDate[6:])]

#creating a calendar data set
calendardata = calendar.Calendar()

#PTO hours --> PTO days

def PTOtoDays():
    PTOhoursLeft = 0
    PTOhours = int(input('How Many PTO Hours Does Employee Have Left? (ex. 5): '))
    PTOdays = PTOhours // 8
    PTOhoursLeft = PTOhours % 8
    return([PTOhours, PTOdays, PTOhoursLeft])
        
def SDIandSDTL():
    SDI = int(input("how many weeks of SDI does employee get? (ex. 1, 8, etc. only one number): "))
    SDIamount = int(input("How much money is in one week of SDI: "))
    question = input("Does employee get SDTL? (y / n): ")
    SDTL = 0
    if question == 'y':
        
        SDTL = int(input("how many days of STDL does employee get? (ex. 1, 8, etc. only one number): "))
    return([SDI, SDTL, SDIamount])

def DailyPay(CleanDaysofBimonthly):
    YearlyWage = int(input("Input Yearly Income (ex. 120000. no commas.): "))
    global BimonthlyPay
    BimonthlyPay = (YearlyWage/24)
    for bimonthlyPeriods in CleanDaysofBimonthly:
        bimonthlyPeriods.append(BimonthlyPay/len(bimonthlyPeriods))
        bimonthlyPeriods.append([0])
    return(CleanDaysofBimonthly)
     


        


    return(biweekly)


def weeksofyear():
    ListofWeeks = []
    ListofWeeks.append(calendardata.itermonthdays2(startDate[2]))




print(weeksdayextractor())