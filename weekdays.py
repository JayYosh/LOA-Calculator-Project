

def PTOtoDays():
    PTOhoursLeft = 0
    PTOhours = int(input('How Many PTO Hours Does Employee Have Left? (ex. 5): '))
    PTOdays = PTOhours // 8
    PTOhoursLeft = PTOhours % 8
    return([PTOhours, PTOdays, PTOhoursLeft])
        

SDIavailibity = 0
def SDIandSDTL():
    SDI = int(input("how many weeks of SDI does employee get? (ex. 1, 8, etc. only one number): "))
    SDIamount = int(input("How much money is in one week of SDI: "))
    question = input("Does employee get SDTL? (y / n): ")
    SDTL = 0
    if question == 'y':
        SDIavailibity += 1 
        SDTL = int(input("how many days of STDL does employee get? (ex. 1, 8, etc. only one number): "))
    return([SDI, SDTL, SDIamount])

def DailyPay():
    YearlyWage = int(input("Input Yearly Income (ex. 120000. no commas.): "))
    global biweeklypay
    biweeklypay = ((YearlyWage/52) * 2)
    dailyamount = ((YearlyWage/52/5))
    return(dailyamount)
     


        


    return(biweekly)

def loacalculator():
    
    numberofweeks = []
    numberofLOA = []
    week1 = ''
    week2 = ''
    digitofweeks = int(input("how total COMPLETE weeks are the employee gone for? : "))
    
    week1 = input("is the FIRST WEEK, the first or second week of the pay cycle? (1/2): ")
    if input("is there an incomplete week in the beginning? (y/n) ") == 'y':        
        
        beginningweek = (int(input("how many days are they gone for? (ex. 4): ")))

        if week1 == '1':
            numberofweeks.append(beginningweek)
    else: 
        beginningweek = 5

    
    for x in range(digitofweeks):
        numberofweeks.append(5)

    week2 = input("is the LAST WEEK, the first or second week of the pay cycle? (1/2): ")
    if input("is there an incomplete week in the end? (y/n):  ") == 'y':
        
        endweek = (int(input("how many days are they gone for? (ex. 4): "))) 
        numberofweeks.append(endweek)
    else:
         endweek = 5
        
    
   

    
    
    dailyamount = (DailyPay())


    PTO = PTOtoDays()
    PTOdays = PTO[1]
    
    SDIandSTDL = SDIandSDTL()
    sdi = SDIandSTDL[0]
    stdl = SDIandSTDL[1]
    SDIamount = SDIandSTDL[2]
    PTOamount = dailyamount
    STDLamount = (dailyamount - int((SDIamount/5)))
    
    usedPTO = 0
    usedSDI = 0
    usedSTDL = 0
    
    
    weekcounter = 1 
    biweeklylistcounter = 0
    for week in numberofweeks:
        counter = 0
        

        if (weekcounter == 1):
            numberofLOA.append([0])
            if (week1 == '1'):
                
                
                while counter != (beginningweek + 1):
                    if (sdi > 0):
                        if (counter == 0):
                            usedSDI += 1
                            sdi -= 1
                            numberofLOA[biweeklylistcounter][0] += (SDIamount)
                    if (stdl > 0):
                        usedSTDL += 1
                        stdl -= 1
                        numberofLOA[biweeklylistcounter][0] += STDLamount
                    elif ((PTOdays > 0) and (((numberofLOA[biweeklylistcounter][0] + PTOamount))) <= biweeklypay):
                            usedPTO += 1
                            PTOdays -= 1
                            numberofLOA[biweeklylistcounter][0] += (dailyamount) 
                    counter += 1
            else:
                weekcounter += 1
                numberofLOA[biweeklylistcounter][0] += (dailyamount*5)
                while counter != beginningweek:
                    if (sdi > 0) and ((numberofLOA[biweeklylistcounter][0] + (SDIamount))) <= biweeklypay:
                        if (counter == 1) or (counter == 6):
                            usedSDI += 1
                            sdi -= 1
                            numberofLOA[biweeklylistcounter][0] += (SDIamount)
                    if (stdl > 0):
                        usedSTDL += 1
                        stdl -= 1
                        numberofLOA[biweeklylistcounter][0] += STDLamount
                    elif ((PTOdays > 0) and ((numberofLOA[biweeklylistcounter][0] + (dailyamount))) <= biweeklypay):
                            usedPTO += 1
                            PTOdays -= 1 
                            numberofLOA[biweeklylistcounter][0] += (dailyamount) 
                    counter += 1
            if weekcounter % 2 == 0:    
                numberofLOA[biweeklylistcounter].append([usedSDI, sdi, usedSTDL, stdl, usedPTO, PTOdays])
                biweeklylistcounter += 1
                numberofLOA.append([0])
                weekcounter += 1
                usedPTO = 0
                usedSDI = 0
                usedSTDL = 0
            else: 
                
                weekcounter += 1
                

        elif weekcounter == (len(numberofweeks) + 1):
            if week2 == '1':
                numberofLOA[biweeklylistcounter][0] += (5*dailyamount)
            while counter != endweek:
                if (sdi > 0):
                    if (counter == 0):
                        usedSDI += 1
                        sdi -= 1
                        numberofLOA[biweeklylistcounter][0] += (SDIamount)
                if (stdl > 0):
                    usedSTDL += 1
                    stdl -= 1
                    numberofLOA[biweeklylistcounter][0] += STDLamount
                elif ((PTOdays > 0) and ((numberofLOA[biweeklylistcounter][0] + PTOamount) <= biweeklypay)):
                        usedPTO += 1
                        PTOdays -= 1
                        numberofLOA[biweeklylistcounter][0] += (dailyamount) 
                            
                counter += 1  
            if weekcounter % 2 == 0:
                numberofLOA[biweeklylistcounter].append([usedSDI, sdi, usedSTDL, stdl, usedPTO, PTOdays])
                biweeklylistcounter += 1
                weekcounter += 1
                usedPTO = 0
                usedSDI = 0
                usedSTDL = 0
            else: 
                weekcounter += 1
                numberofLOA[biweeklylistcounter].append([usedSDI, sdi, usedSTDL, stdl, usedPTO, PTOdays])

                
           
                        

        else:
            counter = 0
            while counter != 5:
                if (sdi > 0):
                    if (counter == 0):
                            usedSDI += 1
                            sdi -= 1
                            numberofLOA[biweeklylistcounter][0] += (SDIamount)
                if (stdl > 0):
                            usedSTDL += 1
                            stdl -= 1
                            numberofLOA[counter] += STDLamount
                elif ((PTOdays > 0) and ((numberofLOA[biweeklylistcounter][0] + PTOamount) <= biweeklypay)):
                            usedPTO += 1
                            PTOdays -= 1 
                            numberofLOA[biweeklylistcounter][0] += (dailyamount)
                counter += 1 
            if weekcounter % 2 == 0:
                numberofLOA[biweeklylistcounter].append([usedSDI, sdi, usedSTDL, stdl, usedPTO, PTOdays])
                biweeklylistcounter += 1
                numberofLOA.append([0])  
                weekcounter += 1 
                usedPTO = 0
                usedSDI = 0
                usedSTDL = 0
            else:    
                weekcounter += 1

            
            
    counter = 1
    for period in numberofLOA:
            print('For biweekly period ' +  str(counter) + ' use:')
            print('SDI: ' + str(period[-1][0]))
            print('Left over SDI: ' + str(period[-1][1]))
            print('STDL: ' + str(period[-1][2]))
            print('Left over STDL: ' + str(period[-1][3]))
            print('PTO: ' + str(period[-1][4]))
            print('Left over PTO: ' + str(period[-1][5]))
            print('Left over PTO hours: ' + str(PTO[2]))
            print('You will make: ' + str(period[0]))
            print('You will not make: ' + str(biweeklypay - period[0]))
            print('\n')
            counter += 1
    




print(loacalculator())