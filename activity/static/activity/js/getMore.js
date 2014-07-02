// JavaScript Document

var i=6;	//设定全局变量 i 初始值为 6

function getMore() {	//定义函数

    $.ajax({
        url: '/news/',
        type: "POST",
        dataType: "json",
        //data: i,

        success: function (msg) {

            var len = msg.length;

            for (var j = 0; j < len; j++) {
                var title = msg[j].fields.title;
                var content = msg[j].fields.content;
                var img = msg[j].fields.pic;
                $("#list").append(' <div class="floatb"><div class="imgbox"><img src="{% static '+img+' %}"></img></div><div class="titbox">'+title+'</div><div class="contbox">'+content+'</div><div class="morebox">...更多>></div></div>');
            }

            
        },

        error: function (xmlHttpRequest, textStatus, errorThrown) {
            alert(xmlHttpRequest.status);
            alert(xmlHttpRequest.Readystate);
            alert(textStatus);
        }
    });

    i = i + 2;
    var csrftoken = $.cookie('csrftoken');


};