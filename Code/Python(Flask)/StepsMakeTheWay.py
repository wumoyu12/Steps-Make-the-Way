from flask import Flask, render_template, request, redirect
import os.path
from os import path

# symbol^.^
# intro info alert
# home button
# capitalize user info
# logo in title

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("login.html", usermsg="login")

@app.route("/AdminHome")
def AdminHome():
    return render_template("AdminHome.html",username = username);

@app.route("/UserHome")
def UserHome():
    return render_template("UserHome.html",username = username);

@app.route("/login",methods=["POST"])
def GetInfo():
    global username,userpasswd,filename
    global fileDir
    fileDir = os.path.dirname(os.path.realpath("__file__"));

    username = request.form.get('txtusername');
    userpasswd = request.form.get('txtpassword');
    usertype = request.form.get('usertype');

    if (username == "" or userpasswd == ""):
        error = "Please enter all fields"
        return render_template("login.html", error=error, usermsg="login")

    if(usertype == None):
        error =  "Please choose to login as a user or an admin"
        return render_template("login.html", error=error, usermsg="login")
    
    if(usertype == "admin"):
        return CheckAdmin();

    filename = username + ".doc"
    CheckExist(filename)
    if (status == "new"):
        error =  "Account Not Found"
        return render_template("login.html", error=error, usermsg="login")
    
    IfTrue = CheckPw(filename,userpasswd)
    
    if (IfTrue == "False"):
        error =  "Invalid password"
        return render_template("login.html", error=error, usermsg="login")
    else:
        return render_template("UserHome.html",username = username);
    
def CheckPw(name,pw):
    file = open(name, "r+")
    fileitems = file.read().split("^");
    file.close()

    if(fileitems[0] != pw):
        TorF = "False"
    else:
        TorF = "True"
    return TorF

def CheckExist(name):
    global status
    fileexist = bool(path.exists(name))

    if (fileexist == False):
        status = "new"
    else:
        status = "exist"

def CheckAdmin():
    if(username == "admin"):
        if(userpasswd == "admin123"):
            #thefile = "admin.doc"
            #CheckExist(thefile);
            #if(status == "new"):
            #    CreateFile(thefile)
            return render_template("AdminHome.html",username = username);
        else:
            error =  "Incorrect password"
            return render_template("login.html", error=error, usermsg="login")  
    else:
        error =  "This account doesn't have admin privelige"
        return render_template("login.html", error=error, usermsg="login")
    
@app.route("/signup", methods=["POST"])
def SignUp():
    global filename
    username = request.form.get('txtsignupusername')
    userpasswd = request.form.get('txtsignuppassword')
    userpasswdr = request.form.get('txtsignuprpassword')
    
    if (username == "" or userpasswd == "" or userpasswdr == ""):
        return render_template("login.html", error="Please fill all fields", usermsg="signup")
    
    if (userpasswd != userpasswdr):
        return render_template("login.html", error="Passwords don't match", usermsg="signup")

    filename = username + ".doc"
    CheckExist(filename)
    if (status == "exist"):
        return render_template("login.html", error="Account already exists", usermsg="signup")
    else:
        CreateFile(filename)
        Append(filename,userpasswd)
        purchasingfile = "Purchase_" + username + ".doc"
        CreateFile(purchasingfile)
    
    return render_template("login.html", error="Account created successfully! You can now use your info to login!", usermsg="login")

def CreateFile(name):
    adminfile = open(name,"x");
    adminfile.close();

def Append(name,info):
    adminfile = open(name,"a");
    adminfile.write(info + "^");
    adminfile.close();

############### Admin Intro Page Appears ###############
@app.route("/AdminIntro")
def AdminIntro():
    global previewerror
    previewerror = ""
    CreateStatusFile();
    CreateIntroFile();

    return CheckDisplayIntro();

def CreateStatusFile():
    thefilename = "IntroStatus.doc"
    CheckExist(thefilename)
    if (status == "new"):
        CreateFile(thefilename)

def CreateIntroFile():
    filename = "AdminIntro.doc"
    CheckExist(filename)
    if (status == "new"):
        CreateFile(filename)

def CheckIntroStatus():
    whichfile = "IntroStatus.doc"
    Introwhich = GetInforamtion(whichfile);
    if(Introwhich == "" or Introwhich == "Default Introduction(shown below)"):
        which = "Default Introduction(shown below)"
    else:
        which = "Custom Introduction"
    return which

def GetInforamtion(name):
    file = open(name, "r")
    text = file.read()
    file.close()
    return text;

def CheckDisplayIntro():
    global whichIntro
    whichIntro = CheckIntroStatus();
    ifempty = GetInforamtion("AdminIntro.doc")
    if(ifempty == ""):
        return render_template("AdminIntro.html",previewerror=previewerror,whichIntro=whichIntro);
    else:
        return DisplayIntro();
    
def DisplayIntro():
    whichIntro = CheckIntroStatus();
    filename = "AdminIntro.doc"
    items = GetItems(filename)
    lengthItems = len(items) -1

    if(lengthItems == 3):
        content3 = items[2]
        content2 = items[1]
        content1 = items[0]
        return render_template("AdminIntro.html",previewerror=previewerror,whichIntro=whichIntro,content1=content1,content2=content2,content3=content3);
    elif(lengthItems == 2):
        content2 = items[1]
        content1 = items[0]
        return render_template("AdminIntro.html",previewerror=previewerror,whichIntro=whichIntro,content1=content1,content2=content2);
    else:
        content1 = items[0]
        return render_template("AdminIntro.html",previewerror=previewerror,whichIntro=whichIntro,content1=content1);
    
############### Admin Intro Preview Intro ###############
@app.route("/PreviewCustom", methods=["POST"])
def PreviewCustom():
    global previewerror
    previewerror = ""
    Intro = [];
    txtIntro1 = request.form.get('txtIntro1');
    txtIntro2 = request.form.get('txtIntro2');
    txtIntro3 = request.form.get('txtIntro3');
    if(txtIntro1 == "" and txtIntro2 == "" and txtIntro3 == ""):
        previewerror = "Please enter your custom Introduction before you click on preview"
        print(previewerror)
        return CheckDisplayIntro()
    else:
        filename = "AdminIntro.doc"
        
        if(txtIntro1 != ""):
            Intro.append(txtIntro1)
        if(txtIntro2 != ""):
            Intro.append(txtIntro2)
        if(txtIntro3 != ""):
            Intro.append(txtIntro3)

        lenIntro = len(Intro)
        if(lenIntro == 1):
            Write(filename,Intro[0]+"^")
        else:
            Write(filename,Intro[0]+"^")
            for i in range(0,lenIntro-1):
                Append(filename,Intro[i+1]);

        return DisplayIntro();

def Write(file,info):
    adminfile = open(file,"w");
    adminfile.write(info);
    adminfile.close();
        
def GetItems(name):
    file = open(name, "r+")
    fileitems = file.read().split("^");
    file.close()
    return fileitems

@app.route("/ApplyCustom")
def ApplyCustom():
    global previewerror
    previewerror = ""
    whichIntro = CheckIntroStatus();
    ifempty = GetInforamtion("AdminIntro.doc")
    if(ifempty == ""):
        previewerror = "Please enter your custom Introduction and preview before you click on apply"
        return render_template("AdminIntro.html",previewerror=previewerror,whichIntro=whichIntro);
    else:
        previewerror = "Applied!"
        whichIntro = "Custom Introduction"
        whichfile = "IntroStatus.doc"
        Write(whichfile,whichIntro)
        return DisplayIntro();

############### Admin Intro Default ###############
@app.route("/ApplyDefault", methods=["POST"])
def ApplyDefault():
    global previewerror
    previewerror = ""
    whichfile = "IntroStatus.doc"
    whichIntro = "Default Introduction(shown below)"
    Write(whichfile,whichIntro)

    return CheckDisplayIntro();

@app.route("/DeleteCustomIntro")
def DeleteCustomIntro():
    global previewerror
    previewerror = "Custom Intro is Deleted!"
    
    whichfile = "AdminIntro.doc"
    whichIntro = ""
    Write(whichfile,whichIntro)
    
    whichfile = "IntroStatus.doc"
    whichIntro = "Default Introduction(shown below)"
    Write(whichfile,whichIntro)

    return CheckDisplayIntro();

@app.route("/UserIntro")
def UserIntro():
    thefile = "IntroStatus.doc"
    CheckExist(thefile);
    if(status == "new"):
        ifDefalut = False
        return render_template("UserIntro.html",ifDefalut=ifDefalut);
    else:
        whichIntro = CheckIntroStatus();
        if(whichIntro == "Default Introduction(shown below)"):
            ifDefalut = False
            return render_template("UserIntro.html",ifDefalut=ifDefalut);
        else:
            ifDefalut = True
            filename = "AdminIntro.doc"
            items = GetItems(filename)
            lengthItems = len(items) -1

            if(lengthItems == 3):
                content3 = items[2]
                content2 = items[1]
                content1 = items[0]
                return render_template("UserIntro.html",ifDefalut=ifDefalut,content1=content1,content2=content2,content3=content3);
            elif(lengthItems == 2):
                content2 = items[1]
                content1 = items[0]
                return render_template("UserIntro.html",ifDefalut=ifDefalut,content1=content1,content2=content2);
            else:
                content1 = items[0]
                return render_template("UserIntro.html",ifDefalut=ifDefalut,content1=content1);

########AdminProducts#########
@app.route("/AdminProduct")
def AdminProduct():
    thefile = "Product.doc"
    CheckExist(thefile);
    if(status == "new"):
        return render_template("AdminProduct.html");
    else:
        adminfile = open(thefile,"r+")
        allInfo = adminfile.read();
        adminfile.close();
        thelength = len(allInfo);
        
        if(thelength == 0):
            return render_template("AdminProduct.html");
        else:
            whichAccount = "admin"
            Retrieve(thefile,whichAccount);
            headings = ("Image","Product","Price","Description")
            return render_template("AdminProduct.html",headings = headings,data = data)

@app.route("/AdminProductForm", methods=["POST"])
def AdminProductForm():
    thefile = "Product.doc"
    CheckExist(thefile);
    if(status == "new"):
        adminfile = open(thefile,"x");
        adminfile.close();
        
    msg=""
    GetProductInfo();
    CheckProductPrice(pprice);
    if(iscorrect != 0 or decimalnum > 1):
        msg = "Invalid input for price, please try again"
    else:
        AddProductInfo(thefile);

    adminfile = open(thefile,"r+")
    allInfo = adminfile.read()
    adminfile.close()
    
    if(allInfo == ""):
        return render_template("AdminProduct.html",msg=msg)
    else:
        whichAccount = "admin"
        Retrieve(thefile,whichAccount);
        
    headings = ("Image","Product","Price","Description")
    return render_template("AdminProduct.html",headings = headings,data = data,msg=msg)

def GetProductInfo():
    global pimage,pname,pprice,pdescription;
    pimage = request.form.get('Selectimg');
    pname = request.form.get('txtproductname');
    pprice = request.form.get('txtproductprice');
    pdescription = request.form.get('txtdescription');

def CheckProductPrice(item):
    global iscorrect, decimalnum
    iscorrect = 0;
    decimalnum = 0;
    numberlist = list(item)
    length = len(numberlist);
    if(length == 0 or item == "0"):
        iscorrect = iscorrect + 1;
    else:
        for i in range(length):
            checkitem = ord(numberlist[i])
            if(checkitem >= 48 and checkitem <= 57):
                iscorrect = iscorrect + 0;
            else:
                if(checkitem == 46):
                    decimalnum = decimalnum + 1;
                else:
                    iscorrect = iscorrect + 1;

def AddProductInfo(file):
    adminfile = open(file,"r+")
    allInfo = adminfile.read();
    adminfile.close();
    thelength = len(allInfo);
    if(thelength == 0):
        adminfile = open(file,"w")
        adminfile.write(str(pimage) + "^" + str(pname) + "^" + str(pprice) + "^" + str(pdescription));
    else:
        adminfile = open(file,"a")
        adminfile.write("^" + str(pimage) + "^" + str(pname) + "^" + str(pprice) + "^" + str(pdescription));
    adminfile.close()

def Retrieve(myfilename,account):
    global data,productarray,pricearray,imagearray,descriptionarray
    data = [];
    productarray = [];
    pricearray = [];
    imagearray = [];
    descriptionarray = [];
    adminfile = open(myfilename,"r+")
    allInfo = adminfile.read().split("^");
    adminfile.close();
    length = (len(allInfo)/4);
    num = 0
    
    for i in range(int(length)):
        theimage = allInfo[num]
        thename = allInfo[num+1]
        theprice = "$" + allInfo[num+2]
        thedescription = allInfo[num+3]
        subdata = [];

        subdata.append(theimage)
        subdata.append(thename)
        subdata.append(theprice)
        subdata.append(thedescription)

        if(account == "user"):
            imagearray.append(theimage)
            productarray.append(thename)
            pricearray.append(theprice)
            descriptionarray.append(thedescription)

        num = num+4
        data.append(subdata)

@app.route("/DeleteProducts")
def DeleteProducts():
    FileName = "Product.doc"
    msg2 = AdminDelete(FileName);
    return render_template('AdminProduct.html',msg2=msg2)

def AdminDelete(aFile):
    CheckExist(aFile);
    if(status == "new"):
        themsg = "It is already empty!"
    else:
        adminfile = open(aFile,"r+")
        allInfo = adminfile.read()
        adminfile.close()
        if(allInfo == ""):
            themsg = "It is already empty!"
        else:
            adminfile = open(aFile,"w")
            allInfo = adminfile.write("")
            adminfile.close()
            themsg = "Everything is deleted!"
    return themsg

########UserProducts#########
@app.route("/UserProduct")
def UserProduct():
    FileName = "Product.doc"
    CheckExist(FileName);
    if(status == "new"):
        return render_template("NoProduct.html");
    else:
        adminfile = open(FileName,"r+")
        allInfo = adminfile.read();
        adminfile.close();
        thelength = len(allInfo);
        if(thelength == 0):
            return render_template("NoProduct.html");
        else:
            whichAccount = "user"
            Retrieve(FileName,whichAccount);
            listofproducts = []
            for i in range(0,len(productarray)):
                listofproducts.append(str(i+1) + "." + productarray[i])
            headings = ("Image","Product","Price","Description")
            return render_template('UserProduct.html',headings = headings,data = data,listofproducts = listofproducts)

@app.route("/UserProductForm", methods=["POST"])
def CheckPrice():
    character = []
    selectedproduct = request.form.get("productdropdown");
    selectequantity = int(request.form.get("howmany"))
    
    character = selectedproduct.split(".");
    productprice = pricearray[int(character[0])-1]
    element = productprice.split("$");
    productprice = element[1]
    TotalPrice = selectequantity * float(productprice)

    Product = character[1]
    Quantity = str(selectequantity)

    productimage = imagearray[int(character[0])-1]
    productdesc = descriptionarray[int(character[0])-1]

    SaveInfo(Product,Quantity,TotalPrice,productimage,productdesc)
    return GetInfoAgain(Product,Quantity,TotalPrice)

def SaveInfo(aProduct,aQuantity,aTotalPrice,aImage,aDesc):
    file = "Purchase_" + username + ".doc"
    
    adminfile = open(file,"r+")
    allInfo = adminfile.read();
    elements = allInfo.split("^")
    thelength = len(elements);
    adminfile = open(file,"a")
    if(thelength == 1):
        adminfile.write(str(aImage) + "^" + str(aProduct) + "^" + str(aQuantity) + "^" + str(aDesc) + "^" + str(aTotalPrice));
    else:
        adminfile.write("^" + str(aImage) + "^" + str(aProduct) + "^" + str(aQuantity) + "^" + str(aDesc) + "^" + str(aTotalPrice));
    adminfile.close()

def GetInfoAgain(theproduct,thequantity,theprice):
    whichAccount = "user"
    Retrieve("Product.doc",whichAccount);
    listofproducts = []
    for i in range(0,len(productarray)):
        listofproducts.append(str(i+1) + "." + productarray[i])
    headings = ("Image","Product","Price","Description")
    return render_template('UserProduct.html',headings = headings,data = data,listofproducts = listofproducts,theprice=theprice,thequantity=thequantity,theproduct=theproduct)

@app.route("/cart")
def Cart():
    global headings2
    TorF = Retrieve2();
    if (TorF == False):
        return render_template("EmptyCart.html")
    else:
        headings2 = ("Image","Product","Quantity","Description","Price")
    return render_template('Cart.html',headings = headings2,data = data2,pricetotal=pricetotal)

def Retrieve2():
    global data2,pricetotal
    file = "Purchase_" + username + ".doc"
    data2 = [];
    pricetotal = 0
 
    adminfile = open(file,"r+")
    allInfo = adminfile.read().split("^");
    length = len(allInfo);
    adminfile.close()
    if(length == 1):
        return False
    else:
        length = (len(allInfo)/5);
        num = 0
        
        for i in range(int(length)):
            theimage = allInfo[num]
            thename = allInfo[num+1]
            thenum = allInfo[num+2]
            thedesc = allInfo[num+3]
            theprice = "$" + allInfo[num+4]
            subdata = [];

            pricetotal = float(allInfo[num+4]) + pricetotal

            subdata.append(theimage)
            subdata.append(thename)
            subdata.append(thenum)
            subdata.append(thedesc)
            subdata.append(theprice)

            num = num+5
            data2.append(subdata)
        return True

@app.route("/delete")
def Clear():
    UserDelete();
    return render_template('EmptyCart.html')

def UserDelete():
    file = "Purchase_" + username + ".doc"
    #adminfile = open(file,"r+")
    #allInfo = adminfile.read().split("^");
    #length = len(allInfo);
    #for i in range(0,length-1):
    #    allInfo.pop(1)

    #thepw = allInfo[0]
    adminfile = open(file,"w")
    #adminfile.write(str(thepw)+"^")
    adminfile.write("")

    adminfile.close()

@app.route("/viewreceipt")
def Receipt():
    Retrieve2();
    UserDelete();
    return render_template('Receipt.html',headings = headings2,data = data2,pricetotal=pricetotal)



#Admin(Edit)Events-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@app.route("/AdminEvents")
def AdminRequstEmail():
    file = "email.doc"
    CheckExist(file)
    if status == "new":
        CreateFile(file)
        return render_template("AdminEmail.html")
    else:
        adminfile = open(file, "r")
        content = adminfile.read()
        adminfile.close()  
        if(content == ""):
            return render_template("AdminEmail.html")
        else:
            return AdminEvents()
    
def AdminEvents():
    thefile = "eventdetail.doc"
    CheckExist(thefile)
    if status == "new":
        CreateFile(thefile)
    events = GetEvents()
    return render_template("AdminEvents.html", EventName=events, msg3="")


def GetEvents():
    thefile = "eventdetail.doc"
    file = open(thefile, "r")
    content = file.read()
    file.close()
    
    if content == "":
        return []
    
    events = content.split("^")
    eventlist = []
    for event in events:
        if(event != ""):
            parts = event.split("//")
            if(len(parts) == 6):
                eventlist.append({
                    "name": parts[0],
                    "place": parts[1],
                    "date": parts[2],
                    "starttime": parts[3],
                    "endtime": parts[4],
                    "details": parts[5]
                })
    return eventlist

@app.route("/SubmitEmail", methods=["POST"])
def SubmitEmail():
    email = request.form.get('txtemail')
    if(email == ""):
        error = "Please enter your email"
        return render_template("AdminEmail.html",error=error)
    else:
        file = "email.doc"
        adminfile = open(file, "w")
        adminfile.write(email)
        adminfile.close()  
        return AdminEvents()

@app.route("/AdminEmail")
def AdminEmail():
    file = "email.doc"
    adminfile = open(file, "r")
    content = adminfile.read()
    adminfile.close()  
    return render_template("AdminEmail.html",email=content)

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
    
    #if (eventname == "" or eventplace == "" or eventdate == "" or starttime == "" or endtime == "" or eventdetails == ""):
    #    details = []
    #    error = "Please fill all fields"
    #    return render_template("AdminEditEvents.html", details=details, error=error)
    
    eventinfo = eventname + "//" + eventplace + "//" + eventdate + "//" + starttime + "//" + endtime + "//" + eventdetails
    SaveEventToFile(eventinfo)
    
    return redirect("/AdminEvents")

def SaveEventToFile(eventinfo):
    filename = "eventdetail.doc"
    file = open(filename, "a")
    file.write(eventinfo + "^")
    file.close()
    
@app.route("/AdminDeleteEvents")
def AdminDeleteEvents():
    FileName = "eventdetail.doc"
    msg3 = AdminDelete(FileName);
    return render_template('AdminEvents.html',msg3=msg3)

def AdminDelete1(aFile):
    CheckExist(aFile);
    if(status == "new"):
        themsg = "It is already empty!"
    else:
        adminfile = open(aFile,"r+")
        allInfo = adminfile.read()
        adminfile.close()
        if(allInfo == ""):
            themsg = "It is already empty!"
        else:
            adminfile = open(aFile,"w")
            allInfo = adminfile.write("")
            adminfile.close()
            themsg = "Everything is deleted!"
    return themsg

#UserEvent------------------------------------------------------------------
@app.route("/UserEvents")
def UserEvents():
    filename = "eventdetail.doc"
    CheckExist(filename)
    if status == "new":
        return render_template("NoProduct.html")
    
    file = open(filename, "r")
    content = file.read()
    file.close()
    if(content == ""):
        return render_template("NoProduct.html")
    
    event_list = []
    events = content.split("^")
    for event in events:
        if event != "":
            parts = event.split("//")
            if len(parts) == 6:
                event_list.append(parts)

    thefile = "email.doc"
    email = GetInforamtion(thefile)
    return render_template("UserEvents.html",email=email, events=event_list)

    
#UV--------------------------------------------------------------------------
@app.route("/UserVolunteer")
def UserVolunteer():
    userfile = username + ".doc"
    #CheckExist(userfile)
    #if status == "new":
    #    return render_template("UserVolunteer.html", usermsg="form")
    #else:
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
    
    #if (firstname == "" or lastname == "" or birthdate == "" or gender == ""):
    #    return render_template("UserVolunteer.html", error="Please fill all fields", usermsg="form")
    
    #currentuserfile = "currentuser.doc"
    #CheckExist(currentuserfile)
    #file = open(currentuserfile, "r")
    #username = file.read()
    #file.close()
    
    filename = "volunteer.doc"
    CheckExist(filename)
    if(status == "new"):
        CreateFile(filename)
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
    file.write(userinfo)
    file.close()
    
    return render_template("UserVolunteer.html", usermsg="info", volunteerid=volunteerid, firstname=firstname, lastname=lastname, dob=birthdate, gender=gender)



#AV----------------------------------------------------------------------------------------------------------
@app.route("/AdminVolunteers")
def AdminVolunteers():
    filename = "volunteer.doc"
    CheckExist(filename)
    if(status == "new"):
        return render_template("NoVolunteers.html")
    
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



if __name__ == "__main__":
    app.run()
