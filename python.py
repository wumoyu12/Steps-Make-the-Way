from flask import Flask, render_template, request, redirect
import os.path
from os import path

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def GetInfo():
    global username,userpasswd
    global fileDir
    fileDir = os.path.dirname(os.path.realpath("__file__"));

    username = request.form.get('txtusername');
    userpasswd = request.form.get('txtpassword');
    usertype = request.form.get('usertype');

    if(usertype == "admin"):
        return render_template("AdminHome.html",username = username);
    else:
        return render_template("UserHome.html",username = username);

def CheckExist():
    filename = username + ".doc"
    fileexist = bool(path.exists(filename))

    if (fileexist == False):
        status = "new";
    else:
        status = "edit";

if __name__ == "__main__":
    app.run()
