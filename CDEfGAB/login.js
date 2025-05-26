window.addEventListener("load",InitControls);
window.addEventListener("load",addListener);

function InitControls()
{
	usermsg = document.getElementById("usermsg").value;
	if(usermsg == "login")
	{
		SwitchLogin();
	}
	else
	{
		SwitchSignUp();
	}
}

function addListener()
{
	document.getElementById("showsignup").addEventListener("click",SwitchSignUp);
	document.getElementById("showlogin").addEventListener("click",SwitchLogin);
}

function SwitchSignUp()
{
	document.getElementById("signup").style.display = "block";
	document.getElementById("login").style.display = "none";
	document.getElementById("txtsignupusername").focus();
}

function SwitchLogin()
{
	document.getElementById("login").style.display = "block";
	document.getElementById("signup").style.display = "none";
	document.getElementById("txtusername").focus();
}
