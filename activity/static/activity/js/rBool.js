var b = 0;

thisURL = document.URL; 
var tOrp = "";
var subTyp = "";

for ( var i = 22; thisURL[i] != '/'; i++ )
{
	tOrp = tOrp + thisURL[i];
} 

i++;

if(tOrp == "group")
{
	while(thisURL[i] != '/')
	{
		subTyp = subTyp + thisURL[i];
		i++;
	}
	
	$.ajax({
        url: '/news/',
        type: "POST",
        dataType: "json",
        data: [
                    { name: "group", value: subTyp },
        ],

        error: function (xmlHttpRequest, textStatus, errorThrown) {
            alert(xmlHttpRequest.status);
            alert(xmlHttpRequest.Readystate);
            alert(textStatus);
        }
    });
	
}
else if(tOrp == "news" || tOrp == "activity" || tOrp == "announce" )
{
	$.ajax({
        url: '/news/',
        type: "POST",
        dataType: "json",
        data: [
                    { name: "type", value: tOrp },
        ],

        error: function (xmlHttpRequest, textStatus, errorThrown) {
            alert(xmlHttpRequest.status);
            alert(xmlHttpRequest.Readystate);
            alert(textStatus);
        }
    });
}
//alert(tOrp);
