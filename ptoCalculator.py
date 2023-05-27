import calendar

#start date in months, days, year
startDate = str(input("Start date (Ex. 02/19/2018, Month/Day/Year): "))
startDate = [int(startDate[:2]), int(startDate[3:5]), int(startDate[6:])]

endDate = input("End date (Ex. 02/19/2018, Month/Day/Year): ")
endDate = [int(endDate[:2]), int(endDate[3:5]), int(endDate[6:])]



#PTO hours --> PTO days
PTOhoursLeft = 0
def PTOtoDays():
    PTOhours = int(input('How Many PTO Hours Does Employee Have Left? (ex. 5): '))
    PTOdays = PTOhours % 8
    PTOhoursLeft = PTOhours - (PTOdays * 8)
    print(PTOhours)
    print(PTOdays)
    print(PTOhoursLeft)

#Taking the Start and End date, grabbing all of the months in between them




