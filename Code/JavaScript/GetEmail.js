window.addEventListener("load", AddListeners);
window.addEventListener("load", InitControls);

function InitControls() 
{
    document.getElementById("txtemail").value = "";
    document.getElementById("txtemail").focus();
}

function AddListeners() 
{
    document.getElementById("btnsubmit").addEventListener("click", CheckInfo);
}

function CheckInfo() 
{
    email = document.getElementById("txtemail").value;
        
    if (email == "") 
	{
        alert("Please enter the email");
		document.getElementById("txtemail").focus();
    }
	else
	{
        alert("Your information is updated!");
		document.getElementById("EmailForm").submit();
	}
}
