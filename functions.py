import inquirer, getpass, csv
import validation as v


def replay(message,choices):
    return inquirer.prompt([
        inquirer.List(
            "replay",
            message=message,
            choices=choices
        )
    ])['replay']
    

def logIn():

    email = input("email ? ")
    usersFile = csv.DictReader(open("users.csv"))

    for row in usersFile:
        if email == row['email']:
            attempt = 0
            while True:
                password = getpass.getpass("password ? ")
                if password == row['password']:
                    print("log in successfully")
                    return row  
                else:
                    attempt += 1
                    if attempt == 5 :
                        print("exceeded maximum attempt!, try again later")
                        return False
                    print("password not correct!, try again")
                    
    print("email not found! do you want to register?")
    return False

def register() :

    while True :
        fName = input("please , Inter your first name :  ")
        lName = input("please , Inter your last name :  ")
        if not (v.nameValidate(fName) and v.nameValidate(lName)) :
            print("first name and last name are required and must be all characters")
        else:
            break

    while True:
        email = input("please , Inter your email :  ")
        if not (v.emailValidate(email) and v.uniqueEmail(email)):
            print("email not valid")
        else:
            break

    while True:
        phone = input("inter you phone :  +20")
        if not v.phoneValidate(phone) :
            print("phone not allowed")
        else:
            break

    while True:
        password = getpass.getpass("Enter you password: ")
        confirmPassword = getpass.getpass("Entering your password again: ")
        if not v.passValidate(password,confirmPassword):
            print("password must be less than 10 and greater than 5 and matched")
        else :
            break
 
    return [fName, lName, email, phone, password]




def createProject():

    while True :
        title = input("please , Inter your project title :  ")
        if not v.nameValidate(title):
            print("title is required and must be all characters")
        else:
            break

    details = input("Any details? :  ")


    while True:
        target = input("Target? :  ")
        if not v.numValidate(target):
            print("Not valid!!")
        else:
            break

    while True:
        startYear = input("Start year? :")
        startMonth = input("Start month? :")
        startDay = input("Start day? :")
        endYear = input("End year? :")
        endMonth = input("End month? :")
        endDay = input("End day? :")
        start = v.dateValidate(startYear, startMonth, startDay)
        end = v.dateValidate(endYear, endMonth, endDay)
        if not (start and end) or start > end:
            print("date not valid!, Try again")
        else:
            break
    return [title, details, target, str(start), str(end)]