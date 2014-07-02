// JavaScript Document

var i=6;	//设定全局变量 i 初始值为 6

function getMore() {	//定义函数

    $.ajax({
        url: '/news/',
        type: "POST",
        contentType: "application/json; charset=utf-8",
        dataType: "json",

        success: function (msg) {

            var len = msg.length;

            var j=0;
            for (var j = 0; j < len; j++) {
                $("#list").append(' <div class="floatb"><div class="imgbox">图片</div><div class="titbox">标题</div><div class="contbox">内容</div><div class="morebox">...更多>></div></div>');
            }
            for (var j = 0; j < len; j++) {
                $("#list").append(' <div class="floatb"><div class="imgbox">图片</div><div class="titbox">标题</div><div class="contbox">内容</div><div class="morebox">...更多>></div></div>');
            }

            var fff = msg[j].pk;
            $('#list').append(fff);
        },

        error: function (xmlHttpRequest, textStatus, errorThrown) {
            alert(xmlHttpRequest.status);
            alert(xmlHttpRequest.Readystate);
            alert(textStatus);
        }
    });

    i = i + 2;
	
	
};