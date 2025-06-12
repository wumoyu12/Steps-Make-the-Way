#Admin(Edit)Events--------------------------------------------------------------------------------------------------------------
@app.route("/AdminEvents")
def AdminEvents():
    CheckEventFile()
    events = GetEvents()
    return render_template("AdminEvents.html", EventNmae=events)

@app.route("/AdminEditEvents")
def AdminEditEvents():
    details = []
    return render_template("AdminEditEvents.html", details=details)

@app.route("/SaveEvent", methods=["POST"])
def SaveEvent():
    eventname = request.form.get('txteventname')
    eventplace = request.form.get('txteventplace')
    eventdate = request.form.get('txteventdate')
    starttime = request.form.get('txtstarttime')
    endtime = request.form.get('txtendtime')
    eventdetails = request.form.get('txteventdetails')
    
    if (eventname == "" or eventplace == "" or eventdate == "" or 
        starttime == "" or endtime == "" or eventdetails == ""):
        details = []
        error = "Please fill all fields"
        return render_template("AdminEditEvents.html", details=details, error=error)
    
    eventinfo = eventname + "//" + eventplace + "//" + eventdate + "//" + starttime + "//" + endtime + "//" + eventdetails
    SaveEventToFile(eventinfo)
    
    return redirect("/AdminEvents")

def CheckEventFile():
    filename = "eventdetail.doc"
    CheckExist(filename)
    if status == "new":
        CreateFile(filename)

def SaveEventToFile(eventinfo):
    filename = "eventdetail.doc"
    file = open(filename, "a")
    file.write(eventinfo + "^")
    file.close()

def GetEvents():
    filename = "eventdetail.doc"
    CheckExist(filename)
    if status == "new":
        return []
    
    file = open(filename, "r")
    content = file.read()
    file.close()
    
    if content == "":
        return []
    
    events = content.split("^")
    eventlist = []
    for event in events:
        if event != "":
            parts = event.split("//")
            if len(parts) == 6:
                eventlist.append({
                    "name": parts[0],
                    "place": parts[1],
                    "date": parts[2],
                    "starttime": parts[3],
                    "endtime": parts[4],
                    "details": parts[5]
                })
    
    return eventlist


#UserEvent------------------------------------------------------------------
@app.route("/UserEvents")
def UserEvents():
    filename = "eventdetail.doc"
    CheckExist(filename)
    if status == "new":
        return render_template("userevents.html", events=[])
    
    file = open(filename, "r")
    content = file.read()
    file.close()
    
    if content == "":
        return render_template("userevents.html", events=[])
    
    event_list = []
    events = content.split("^")
    for event in events:
        if event != "":
            parts = event.split("//")
            if len(parts) == 6:
                event_list.append(parts)
    
    return render_template("userevents.html", events=event_list)


@app.route("/RegisterForEvent", methods=["POST"])
def RegisterForEvent():
    event_name = request.form.get('event_name')
    user_email = request.form.get('user_email')
    
    currentuserfile = "currentuser.doc"
    CheckExist(currentuserfile)
    file = open(currentuserfile, "r")
    username = file.read()
    file.close()
    
    filename = "event_registrations.doc"
    CheckExist(filename)
    registration_info = username + "^" + event_name + "^" + user_email + "^"

    Append(filename, registration_info)
    
    return redirect("/UserEvents")

def GetEventRegistrations():
    filename = "event_registrations.doc"
    CheckExist(filename)
    if status == "new":
        return []
    
    file = open(filename, "r")
    content = file.read()
    file.close()
    
    if content == "":
        return []
    
    registrations = content.split("^")
    registration_list = []
    for reg in registrations:
        if reg != "":
            parts = reg.split("^")
            if len(parts) >= 3:
                registration_list.append({
                    "username": parts[0],
                    "event_name": parts[1],
                    "email": parts[2]
                })
    
    return registration_list

#UV--------------------------------------------------------------------------
@app.route("/UserVolunteer")
def UserVolunteer():
    currentuserfile = "currentuser.doc"
    CheckExist(currentuserfile)
    file = open(currentuserfile, "r")
    username = file.read()
    file.close()
    
    userfile = username + ".doc"
    CheckExist(userfile)
    if status == "new":
        return render_template("UserVolunteer.html", usermsg="form")
    else:
        file = open(userfile, "r")
        content = file.read()
        file.close()
        
        parts = content.split("^")
        volunteerinfo = None
        for part in parts:
            if part.startswith("volunteer'"):
                volunteerinfo = part.split("'")
                break
        
        if volunteerinfo and len(volunteerinfo) >= 5:
            return render_template("UserVolunteer.html", 
                                 usermsg="info",
                                 volunteerid=volunteerinfo[1],
                                 firstname=volunteerinfo[2],
                                 lastname=volunteerinfo[3],
                                 dob=volunteerinfo[4],
                                 gender=volunteerinfo[5])
        else:
            return render_template("UserVolunteer.html", usermsg="form")

@app.route("/RegisterVolunteer", methods=["POST"])
def RegisterVolunteer():
    firstname = request.form.get('txtfirstname')
    lastname = request.form.get('txtlastname')
    birthdate = request.form.get('txtbirthdate')
    gender = request.form.get('gender')
    
    if (firstname == "" or lastname == "" or birthdate == "" or gender == ""):
        return render_template("UserVolunteer.html", error="Please fill all fields", usermsg="form")
    
    currentuserfile = "currentuser.doc"
    CheckExist(currentuserfile)
    file = open(currentuserfile, "r")
    username = file.read()
    file.close()
    
    filename = "volunteer.doc"
    CheckExist(filename)
    file = open(filename, "r")
    content = file.read()
    file.close()
    
    if content == "":
        volunteerid = 1
    else:
        volunteers = content.split("..")
        volunteerid = len(volunteers) + 1
    
    volunteerinfo = str(volunteerid) + "'" + firstname + "'" + lastname + "'" + birthdate + "'" + gender
    file = open(filename, "a")
    if content == "":
        file.write(volunteerinfo)
    else:
        file.write(".." + volunteerinfo)
    file.close()
    
    userinfo = "volunteer'" + str(volunteerid) + "'" + firstname + "'" + lastname + "'" + birthdate + "'" + gender
    filename = username + ".doc"
    file = open(filename, "a")
    file.write("^" + userinfo)
    file.close()
    
    return render_template("UserVolunteer.html", usermsg="info", volunteerid=volunteerid, firstname=firstname, lastname=lastname, dob=birthdate, gender=gender)



#AV----------------------------------------------------------------------------------------------------------
@app.route("/AdminVolunteers")
def AdminVolunteers():
    filename = "volunteer.doc"
    CheckExist(filename)
    file = open(filename, "r")
    content = file.read()
    file.close()
    
    volunteers = []
    if content != "":
        volunteer_entries = content.split("..")
        for entry in volunteer_entries:
            if entry != "":
                parts = entry.split("'")
                if len(parts) >= 5:
                    volunteers.append({
                        "id": parts[0],
                        "firstname": parts[1],
                        "lastname": parts[2],
                        "birthdate": parts[3],
                        "gender": parts[4]
                    })
    
    return render_template("AdminVolunteer.html", volunteers=volunteers)
