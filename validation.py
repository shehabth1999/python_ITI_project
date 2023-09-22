import csv, re
from datetime import datetime


def uniqueEmail(email):
    usersFile = csv.DictReader(open("users.csv"))
    for row in usersFile:
        if email == row['email']:
            print(f"Sorry, email {email} is token already!")
            return False
    return True

def phoneValidate(phone):
    if not phone.isdigit() or len(phone) != 10 or phone[0] != "1" or phone[1] not in ["0","1","2","5"]:
        return False
    return True

def numValidate(num):
    if not num.isdigit():
        return False
    return True


def dateValidate(year, month, day):
    try:
        newDate = datetime(int(year), int(month), int(day))
    except ValueError:
        return False
    
    if (newDate-datetime.now()) < (datetime.now()-datetime.now()):
        return False
    return newDate


def nameValidate(name):
    if name.isalpha():
        return True
    return False

def emailValidate(email):
    if(re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email)):
        return True
    return False

def passValidate(password,confirmPassword):
    if len(password) < 5 or len(password) > 10 or password != confirmPassword:
        return False
    return True
