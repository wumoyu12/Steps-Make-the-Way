window.addEventListener("load",InitControls);
window.addEventListener("load",addListener);

function InitControls()
{
	document.getElementById("txtproductname").textContent = "";
	document.getElementById("txtproductprice").textContent = "";
	document.getElementById("txtdescription").textContent = "";
	document.getElementById("txtproductname").focus();
}

function addListener()
{
	document.getElementById("btnadd").addEventListener("click",GetInfo);
	document.getElementById("btnview").addEventListener("click",ViewImage);
}

function GetInfo()
{
	var thename,theprice,thedescription;
	theimage = document.getElementById("Selectimg").value;
	thename = document.getElementById("txtproductname").value;
	theprice = document.getElementById("txtproductprice").value;
	thedescription = document.getElementById("txtdescription").value;
	CheckAllInfo(thename,theprice,thedescription);
} 

function CheckAllInfo(name,price,description)
{
	msg = "";
	if(description == "")
	{
		msg = "D";
		document.getElementById("txtdescription").focus();
	}
	if(price == "")
	{
		msg = "P";
		document.getElementById("txtproductprice").focus();
	}
	if(name == "")
	{
		msg = "N";
		document.getElementById("txtproductname").focus();
	}
	if(msg == "")
	{
		Submit();
	}
	else
	{
		alert("Missing Information / Invalid format");
	}
		
}

function Submit()
{
	document.getElementById("ProductForm").submit();
}	

function ViewImage()
{
	theimage = document.getElementById("Selectimg").value;
	productimg = document.getElementById("productimg");
	productimg.src = "/static/" + theimage;
}
