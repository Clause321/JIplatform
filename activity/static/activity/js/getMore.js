// JavaScript Document

var aaa=6;	//设定全局变量 i 初始值为 6

function getMore() {	//定义函数

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
                    { name: "aaa", value: aaa },
					{ name: "group", value: tOrp},
        ],

        success: function (msg) {

            var len = msg.length;

            for (var j = 0; j < len; j++) {
                var title = msg[j].fields.title;
                var content = msg[j].fields.content;
                var img = msg[j].fields.pic;
                $("#list").append(function(n) { return '<div class="floatb"><div class="imgbox"><img src="/media/' +img+ '"></img></div><div class="titbox">'+title+'</div><div class="contbox">'+content+'</div><div class="morebox">...更多>></div></div>' });
            }

            aaa = aaa + len;

        },

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
                    { name: "aaa", value: aaa },
					{ name: "type", value: subTyp },
        ],

        success: function (msg) {

            var len = msg.length;

            for (var j = 0; j < len; j++) {
                var title = msg[j].fields.title;
                var content = msg[j].fields.content;
                var img = msg[j].fields.pic;
                $("#list").append(function(n) { return '<div class="floatb"><div class="imgbox"><img src="/media/' +img+ '"></img></div><div class="titbox">'+title+'</div><div class="contbox">'+content+'</div><div class="morebox">...更多>></div></div>' });
            }

            aaa = aaa + len;

        },

        error: function (xmlHttpRequest, textStatus, errorThrown) {
            alert(xmlHttpRequest.status);
            alert(xmlHttpRequest.Readystate);
            alert(textStatus);
        }
    });
}


    //var csrftoken = $.cookie('csrftoken');


};