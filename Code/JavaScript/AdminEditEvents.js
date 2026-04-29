window.addEventListener("load", InitControls);
window.addEventListener("load", AddListeners);

function InitControls() 
{
    document.getElementById("txteventname").value = "";
    document.getElementById("txteventplace").value = "";
    document.getElementById("txteventdate").value = "";
    document.getElementById("txtstarttime").value = "";
    document.getElementById("txtendtime").value = "";
    document.getElementById("txteventdetails").value = "";
    document.getElementById("txteventname").focus();
}

function AddListeners() 
{
    document.getElementById("btnsubmit").addEventListener("click", ValidateAndSubmit);
    document.getElementById("btnadddetail").addEventListener("click", AddDetail);
}

function ValidateAndSubmit() 
{
    var eventName = document.getElementById("txteventname").value;
    var eventPlace = document.getElementById("txteventplace").value;
    var eventDate = document.getElementById("txteventdate").value;
    var startTime = document.getElementById("txtstarttime").value;
    var endTime = document.getElementById("txtendtime").value;
    var eventDetails = document.getElementById("txteventdetails").value;
    
    if (eventName == "" || eventPlace == "" || eventDate == "" || startTime == "" || endTime == "" || eventDetails == "") 
	{
        alert("Please fill in all fields");
        return false;
    }
    
    document.getElementById("EventForm").submit();
}

function AddDetail() 
{
    var detailInput = document.getElementById("txteventdetails");
    var detailText = detailInput.value;
    
    if (detailText == "") 
	{
        alert("Please enter detail text");
        return;
    }
    
    alert("Detail added: " + detailText);
    detailInput.value = "";
}