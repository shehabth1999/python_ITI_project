import functions , classes, sys

while True:
    log=functions.replay("HI",["Log in", "Register", "Exit"])
    if log == "Log in":
        user = functions.logIn()
        if user :
            currentUser = classes.User(user['fName'],user['lName'],user['email'],user['phone'],user['password'])
            break
    elif log == "Register" :
        user = functions.register()
        currentUser = classes.User(user[0],user[1],user[2],user[3],user[4])
        currentUser.save()
        print("Your data saved successfully ")
    else:
        if functions.replay("Are you sure !?",["YES", "NO"]) == 'YES':
            sys.exit()

while True:
    
    action = functions.replay("what do you want to do?",["Create project?", "List projects?", "Edit project?", "Delete project?","Exit?"])
    if action == "Create project?":
        project = functions.createProject()
        project.append(currentUser.email)
        campaign = classes.Campaign(project[0],project[1],project[2],project[3],project[4],project[5])
        campaign.save()
        print("Your data saved successfully")

    elif action == "List projects?":
        for project in currentUser.listProjects()[0] : 
            print(project)

    elif action == "Edit project?":
        listed = []
        for i in currentUser.listProjects()[1]:
            listed.append(i["title"])
        if listed == [] :
            print('you do not have any projects, do you want to create one?')
            continue
        selectedProject = functions.replay("Select project to edit : ",listed)
        for project in currentUser.listProjects()[1]:
            if project["title"] == selectedProject :
                pass
                campaign = classes.Campaign(project['title'],project['details'],project['target'],project['start'],project['end'],project['owner'])
        field = functions.replay("which field do you want to edit? ",["title", "details", "target", "start", "end"])
        newData = input("inter new data : ")
        if functions.replay("Are you sure !?",["YES", "NO"]) == 'YES':
            campaign.update(field,newData)

    elif action == "Delete project?":
        listed = []
        for i in currentUser.listProjects()[1]:
            listed.append(i["title"])
        if listed == [] :
            print('you do not have any projects, do you want to create one?')
            continue
        selectedProject = functions.replay("Select project to edit : ",listed)
        for project in currentUser.listProjects()[1]:
            if project["title"] == selectedProject :
                campaign = classes.Campaign(project['title'],project['details'],project['target'],project['start'],project['end'],project['owner'])
        if functions.replay("Are you sure !?",["YES", "NO"]) == 'YES':
            campaign.delete()
    else :
        if functions.replay("Are you sure !?",["YES", "NO"]) == 'YES':
            sys.exit()
