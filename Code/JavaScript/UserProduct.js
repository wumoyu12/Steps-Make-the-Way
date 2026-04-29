window.addEventListener("load",addListener);

function addListener()
{
	document.getElementById("btnadd").addEventListener("click",CheckPrice);
}

function CheckPrice()
{
	var thequantity;
	thequantity = document.getElementById("howmany").value;
	Check(thequantity);
} 

function Check(quantity)
{
	msg = "";
	checkDecimal = quantity%1;
	if(quantity == "" || quantity <= 0 || checkDecimal !== 0)
	{
		msg = "U";
	}
	if(msg == "")
	{
		alert("Product is added");
		Submit();
	}
	else
	{
		alert("Missing/Invalid quantity!");
	}
}

function Submit()
{
	document.getElementById("theUserProductForm").submit();
}	
