import csv

class Campaign:

    def __init__(self, title, details, target, start, end, owner):
        self.title = title
        self.details = details
        self.target = target
        self.start = start
        self.end = end
        self.owner = owner
    
    def save(self):
        with open('projects.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([self.title, self.details, self.target, str(self.start), str(self.end), self.owner])



    def update(self,field,value):

        projectsFile = csv.DictReader(open("projects.csv"))
        data=[]
        for row in projectsFile:
            data.append(row)
        with open("projects.csv", "w") as projects:
            projects.truncate()
        with open("projects.csv", "a") as projects:
            writer = csv.writer(projects)
            writer.writerow(['title', 'details', 'target', 'start', 'end', 'owner'])
            for row in data:
                if row['title'] == self.title:
                    row[field] = value
                writer.writerow(list(row.values()))

    def delete(self):

        projectsFile = csv.DictReader(open("projects.csv"))
        data=[]
        for row in projectsFile:
            data.append(row)
        with open("projects.csv", "w") as projects:
            projects.truncate()
        with open("projects.csv", "a") as projects:
            writer = csv.writer(projects)
            writer.writerow(['title', 'details', 'target', 'start', 'end', 'owner'])
            for row in data:
                if row['title'] == self.title:
                    continue
                writer.writerow(list(row.values()))
 

class User:

    def __init__(self,fName,lName,email,phone, password) -> None:
        self.fName = fName
        self.lName = lName
        self.email = email
        self.phone = phone
        self.password = password
    
    def save(self):
        with open('users.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([self.fName, self.lName, self.email, self.phone,self.password])


    def listProjects(self):
        projectsFile = csv.DictReader(open("projects.csv"))
        ownerList = []
        allList = []
        for row in projectsFile:
            allList.append(f"<<<{row['title']}>>> : ({row['owner']})")
            if row['owner'] == self.email :
                ownerList.append(row)
        return [allList, ownerList]


