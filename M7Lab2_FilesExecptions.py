# Michel Jurado
# October 14,2021
# CSC-121

#---get this 
#get student course number
#get student course name
#days it meets
#times it will meet

#---create schedule file
# CIS
# 115
# mw
# 10-12
# CSC
# 121
# tth
# 01-03


#---create report file
# Student Name 2019 Spring Schedule (center this heading)
# Class Name       Meting Days   Meeting Times
# CIS115               MW                10-12
# CSC121              TTh                01-03

#---create file menu]
# 1.	Create Schedule File
# 2.	Create Report File
# 3.	Exit
# Please enter your choice: 

choice = 0

def createsched():
    '''Create text file'''
    schedule = open('schedule.txt',mode='w')
    report = open('report.txt',mode='w')
#write to both files at the same time
    try:
        length = int(input("How many classes are you taking? "))
        for i in range(length):
            coursename = str(input("Enter course name and number ex:(MAT-171): "))
            schedule.write(coursename+'\n')
            days = str(input("Enter days you meet(m,t,w,th): "))
            schedule.write(days+'\n')
            times = str(input("Enter times you will meet: "))
            schedule.write(times+'\n')
        
            report.write(coursename+' ')
            report.write(days+' ')
            report.write(times+'\n')

        schedule.close()
        report.close()

        with open('schedule.txt',mode='r') as schedule:
            for record in schedule:
                prt = record.strip()
                print(prt)
    except Exception:
        print("Enter a number instead of letter for number of classes you are taking.")

def createrepo():
    try:
        stuname = str(input("Enter student name: "))
        print(f'     Student:{stuname} | 2019 Spring Schedule')
        with open('report.txt',mode='r') as report:
            print(f'{"Class Name":<10}\t{"Meeting Days":<10}\t{"Meeting Times":<10}')
            for record in report:
                course, meetingdays, meetingtms = record.split()
                print(f'{course:<10}\t{meetingdays:<10}\t{meetingtms:<10}')
    except Exception:
        print("Most likely did not create schedule file")
          
def printmenu():
    '''Will print menu'''
    print("MENU",'\n',"------------------------",'\n')
    print("1) Create schedule file")
    print("2) Create report file")
    print("3) Exit")

while choice != 3:
    printmenu()
    try:
        choice = int(input("Enter option: "))
        if choice == 1:
            createsched()
        if choice == 2:
            createrepo()
        if choice == 3:
           print("Exiting...")
           quit()
    except Exception:
        print('\n')
        print("Enter a menu option please...")
