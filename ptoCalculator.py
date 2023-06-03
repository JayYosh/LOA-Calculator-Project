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

def BimonthlyCreator(AllDaysList):
    CleanDaysOfMonth = []
    BimonthlyPeriods = []
    for month in AllDaysList:
        Holder = []
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
    global BimonthlyPay
    BimonthlyPay = (YearlyWage/24)
    for bimonthlyPeriods in CleanDaysofBimonthly:
        bimonthlyPeriods.append(BimonthlyPay/len(bimonthlyPeriods))
        bimonthlyPeriods.append([0])
    return(CleanDaysofBimonthly)
     

#Cleans data to ensure the dates are in the start and end period.


def InDatePeriod(CleanDaysofBimonthly):
    global lengthofend 
    global lengthofbeginning
    if startDate[1] > 15:
        lengthofbeginning = len(CleanDaysofBimonthly[1][:-2])
        for day in CleanDaysofBimonthly[1][:-2]:
            if day[0] < startDate[1]:
                CleanDaysofBimonthly[1].remove(day)
        CleanDaysofBimonthly.remove(CleanDaysofBimonthly[0])
    if startDate[1] < 15:
        lengthofbeginning = len(CleanDaysofBimonthly[0][:-2])
        for day in CleanDaysofBimonthly[0][:-2]:
            if day[0] < startDate[1]:
                CleanDaysofBimonthly[0].remove(day)

    if endDate[1] < 15:
        lengthofend = len(CleanDaysofBimonthly[-2][:-2])
        for day in CleanDaysofBimonthly[-2][:-2]:
            if day[0] > endDate[1]:
                CleanDaysofBimonthly[-2].remove(day)
        CleanDaysofBimonthly.remove(CleanDaysofBimonthly[-1])
    if endDate[1] > 15:
        lengthofend = len(CleanDaysofBimonthly[-1][:-2])
        for day in CleanDaysofBimonthly[-1][:-2]:
            if day[0] > endDate[1]:
                CleanDaysofBimonthly[-1].remove(day)
    return(CleanDaysofBimonthly)

def Holidays(CleanDaysofBimonthly):
    Holiday = ''
    Holiday = input("List Holidays or Days off (ex. 06/04). When you are finished type 'done': ")
    while (Holiday != 'done'):
        Holiday2 = (int(Holiday[:2]), int(Holiday[3:]))
        Bicounter = 0
        for bimonthly in CleanDaysofBimonthly[(((Holiday2[0]-startDate[1])-1) *2 ): (((Holiday2[0]-startDate[1])-1) *2 ) +2 ]:
            counter = 0
            for day in bimonthly[:-2]:
                if Holiday2[1] == day[0]:
                    CleanDaysofBimonthly[Bicounter].remove(bimonthly[counter])
                counter += 1
            Bicounter += 1
        Holiday = input("List Holidays or Days off (ex. 06/04). When you are finished type 'done': ")
    return(CleanDaysofBimonthly)
        
def SDIandSDTL():
    SDI = int(input("how many weeks of SDI does employee get? (ex. 1, 8, etc. only one number): "))
    SDIamount = int(input("How much money is in one week of SDI: "))
    question = input("Does employee get SDTL? (y / n): ")
    SDTL = 0
    if question == 'y':
        
        SDTL = int(input("how many days of STDL does employee get? (ex. 1, 8, etc. only one number): "))
    return([SDI, SDTL, SDIamount])


                
                
def TheMommyProject():
    
    Alldays = monthdayextractor()
    SemiMonthlyPeriods = BimonthlyCreator(Alldays)
    WeekdaysofSemimonthlyperiod = BimonthlyWeekDaysCreator(SemiMonthlyPeriods)

    #Global bimonthlyPayment variable == yearlypay/24
    
    SemiMonthlyMaster = DailyPay(WeekdaysofSemimonthlyperiod)
    SemiMonthlyMaster = InDatePeriod(SemiMonthlyMaster)


    PTO = PTOtoDays()
    PTOdays = PTO[1]
    
    SDIandSTDL = SDIandSDTL()
    sdi = SDIandSTDL[0]
    stdl = SDIandSTDL[1]
    SDIamount = SDIandSTDL[2]
    

    
    counter = 0
    usedPTO = 0
    usedSDI = 0
    usedSTDL = 0
    SDIavailability = 0
    for semimonthly in SemiMonthlyMaster[0:1]:
        PTOamount = semimonthly[-2]
        STDLamount = (int(semimonthly[-2]) - int((SDIamount/5)))
        SemiMonthlyMaster[counter][-1][0] += ((lengthofbeginning - len(semimonthly[:-2])) * PTOamount)
        
        for day in semimonthly[:-2]:
            if SDIavailability == 1:   
                if sdi > 0:
                    if day[1] == 4:
                        usedSDI += 1
                        sdi -= 1
                        SemiMonthlyMaster[counter][-1][0] += SDIamount
            SDIavailability += 1

        for day in semimonthly[:-2]:
                    if (stdl > 0):
                        usedSTDL += 1
                        stdl -= 1
                        SemiMonthlyMaster[counter][-1][0] += STDLamount
                    elif ((PTOdays > 0) and ((SemiMonthlyMaster[counter][-1][0] + PTOamount) <= BimonthlyPay)):
                        usedPTO += 1
                        PTOdays -= 1
                        SemiMonthlyMaster[counter][-1][0] += PTOamount
        SemiMonthlyMaster[counter][-1].extend([usedSDI, sdi, usedSTDL, stdl, usedPTO, PTOdays])
        break            
    counter += 1 
    if len(SemiMonthlyMaster) > 2:
        for semimonthly in SemiMonthlyMaster[0:-1]:
                PTOamount = semimonthly[-2]
                STDLamount = (int(semimonthly[-2]) - int((SDIamount/5)))
                usedPTO = 0
                usedSDI = 0
                usedSTDL = 0
                for day in semimonthly[1:-2]:
                    if sdi > 0:
                        if day[1] == 4:
                            usedSDI += 1
                            sdi -= 1
                            SemiMonthlyMaster[counter][-1][0] += SDIamount
                for day in semimonthly[:-2]:
                        if (stdl > 0):
                            usedSTDL += 1
                            stdl -= 1
                            SemiMonthlyMaster[counter][-1][0] += STDLamount
                        elif ((PTOdays > 0) and ((SemiMonthlyMaster[counter][-1][0] + PTOamount) <= BimonthlyPay)):
                            usedPTO += 1
                            PTOdays -= 1
                            SemiMonthlyMaster[counter][-1][0] += PTOamount
                SemiMonthlyMaster[counter][-1].extend([usedSDI, sdi, usedSTDL, stdl, usedPTO, PTOdays])
                counter += 1

    for semimonthly in SemiMonthlyMaster[-1:]:
        PTOamount = semimonthly[-2]
        STDLamount = (int(semimonthly[-2]) - int((SDIamount/5)))
        SemiMonthlyMaster[-1][-1][0] += ((lengthofend - len(semimonthly[:-2])) * PTOamount)
        usedPTO = 0
        usedSDI = 0
        usedSTDL = 0
        
        for day in semimonthly[:-2]:
                if sdi > 0:
                    if day[1] == 4:
                        usedSDI += 1
                        sdi -= 1
                        SemiMonthlyMaster[-1][-1][0] += SDIamount
        for day in semimonthly[:-2]:
                    if (stdl > 0):
                        usedSTDL += 1
                        stdl -= 1
                        SemiMonthlyMaster[-1][-1][0] += STDLamount
                    elif ((PTOdays > 0) and ((SemiMonthlyMaster[-1][-1][0] + PTOamount) <= BimonthlyPay)):
                        usedPTO += 1
                        PTOdays -= 1
                        SemiMonthlyMaster[-1][-1][0] += PTOamount
        SemiMonthlyMaster[-1][-1].extend([usedSDI, sdi, usedSTDL, stdl, usedPTO, PTOdays])
        counter += 1
        break
    counter = 1
    for period in SemiMonthlyMaster:
        print('For semimonthly period ' +  str(counter) + ' use:')
        print('SDI: ' + str(period[-1][1]))
        print('Left over SDI: ' + str(period[-1][2]))
        print('STDL: ' + str(period[-1][3]))
        print('Left over STDL: ' + str(period[-1][4]))
        print('PTO: ' + str(period[-1][5]))
        print('Left over PTO: ' + str(period[-1][6]))
        print('Left over PTO hours: ' + str(PTO[2]))
        print('You will make: ' + str(period[-1][0]))
        print('You will not make: ' + str(BimonthlyPay - period[-1][0]))
        print('\n')
        counter += 1
    





     

#make if statement to see if not using and SDI then using a PTO is more efficient
   

#print(BimonthlyCreator(monthdayextractor()))
#print(BimonthlyWeekDaysCreator(BimonthlyCreator(monthdayextractor())))
#print(InDatePeriod(DailyPay(BimonthlyWeekDaysCreator(BimonthlyCreator(monthdayextractor())))))
#print(Holidays(InDatePeriod(DailyPay(BimonthlyWeekDaysCreator(BimonthlyCreator(monthdayextractor()))))))

TheMommyProject()




