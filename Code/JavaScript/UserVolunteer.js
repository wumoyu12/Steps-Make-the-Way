window.addEventListener("load", function()
{
    var usermsg = document.getElementById("usermsg").value;

    if (usermsg == "form")
	{
        document.getElementById("registrationform").style.display = "block";
        document.getElementById("volunteerinfo").style.display = "none";
        
        document.getElementById("txtfirstname").value = "";
        document.getElementById("txtlastname").value = "";
        document.getElementById("txtbirthdate").value = "";
        document.getElementById("gender").value = "";
        document.getElementById("txtfirstname").focus();
    }
	else if (usermsg == "info")
	{
        document.getElementById("registrationform").style.display = "none";
        document.getElementById("volunteerinfo").style.display = "block";
    }

    var btnsubmit = document.getElementById("btnsubmit");
    if (btnsubmit != null)
	{
        btnsubmit.addEventListener("click", function()
		{
            var firstname = document.getElementById("txtfirstname").value;
            var lastname = document.getElementById("txtlastname").value;
            var birthdate = document.getElementById("txtbirthdate").value;
            var gender = document.getElementById("gender").value;
            
            if (firstname == "" || lastname == "" || birthdate == "" || gender == "")
			{
                alert("Please fill all fields");
                return false;
            }
            
            document.getElementById("VolunteerForm").submit();
        });
    }
});