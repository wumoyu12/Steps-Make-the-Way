from flask import Flask, render_template, request, redirect
import os.path
from os import path

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def GetInfo():
    global username, userpasswd
    username = request.form.get('txtusername')
    userpasswd = request.form.get('txtpassword')
    usertype = request.form.get('usertype')
    
    error = CheckInput()
    if error:
        return render_template("login.html", error=error)
    
    if usertype == "admin":
        return render_template("AdminHome.html", username=username)
    else:
        return render_template("UserHome.html", username=username)

@app.route("/signup", methods=["POST"])
def SignUp():
    username = request.form.get('txtsignupusername')
    userpasswd = request.form.get('txtsignuppassword')
    userpasswdr = request.form.get('txtsignuprpassword')
    usertype = request.form.get('usertype')
    
    if username == "" or userpasswd == "" or userpasswdr == "":
        return render_template("login.html", error="Please fill all fields")
    
    if userpasswd != userpasswdr:
        return render_template("login.html", error="Passwords don't match")
    
    CheckExist(username)
    if status == "exist":
        return render_template("login.html", error="Account already exists")
    
    filename = username + ".doc"
    file = open(filename, "w")
    file.write(userpasswd + " " + usertype)
    file.close()
    
    return render_template("login.html", error="Account created successfully")

def CheckInput():
    if username == "" or userpasswd == "":
        return "Please enter all fields"
    
    CheckExist(username)
    if status == "new":
        return "Account Not Found"
    
    filename = username + ".doc"
    file = open(filename, "r")
    content = file.read()
    file.close()
    
    userinfo = content.split(" ")
    if userpasswd != storedpasswd:
        return "Invalid password"
    

def CheckExist(username):
    global status
    filename = username + ".doc"
    fileexist = bool(path.exists(filename))

    if fileexist == False:
        status = "new"
    else:
        status = "exist"

if __name__ == "__main__":
    app.run()
