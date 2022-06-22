from statistics import mean

admin = {'Pavankushana' : 'Pavan_1919'}

studentInfo = {'Jay' : [67,78,85], 'Omsai' : [78,89,90], 'Ranjith' : [66,77,88]}

def enterGrades():  # creating a functon used to enter student grades
    studentName = input("Enter Student Name: ")
    studentGrade = input("Enter Student Grade: ")
    if  studentName in studentInfo:
        print("Adding Grade...")
        studentInfo[studentName].append(studentGrade) # adding value to the existing array
    else:
        print("Student doesn't exists")
    print(studentInfo)

def  removeStudent(): # creating a function used to remove student from the dictionary list
    remove = input("Enter Student Name to Remove ")
    if remove in studentInfo:
        print("Removing Student...")
        del studentInfo[remove]  #del command is used to delete element from the list
        '''if sudentInfo == 0:
            print("No students are to be removed")'''   #try to solve this
    else:
        print("Invalid Student Name entered! ")
    print(studentInfo)

def studentAvgGrade():
    for eachStudent in studentInfo:
        grade = studentInfo[eachStudent]
        studentAvg = mean(grade)
        print(eachStudent, "has an Average of :", studentAvg)

'''studentAvg = input("Enter Student Name to get Average: ")
    if studentAvg in studentInfo:
        print('Average of' , studentAvg)
        studentAvg = mean.studentInfo
    else:
        print("Invalid Student Name") 
   '''     
def main():
    
    print("""
    Welcome to Grade Central
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    """)
    value = input("What would you like to do Today? (Enter a number  ) ")

    if value == '1':
        enterGrades()  #functon calling 
    elif value == '2':
        removeStudent() #functon calling 
    elif value == '3':
        studentAvgGrade() #functon calling 
    elif value == '4':
        exit()  # this is the default inbuild function used to exit from the console
    else:
        print("Invalid value entered.....")

login = input("Username: ")
password = input("Password: ")

if login in admin:
    if admin[login] == password:
        print("Welcome,", login)
        while True:
            main()
    else:
        print("Invalid Password...")
else:
    print("Invalid Username, Try again later..")
    
