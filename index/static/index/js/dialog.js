// JavaScript Document
function dialoglgin() {	//定义函数 
	var j = $.layer({
		type : 1,
		title : '登陆',
		closeBtn : [1 , true],
		border : [0],
		area : ['455px','371px'],
		page : {dom : '#login'}
	});
};

function dialogcu() {	//定义函数 
	var m = $.layer({
		type : 1,
		title : '创建用户',
		closeBtn : [1 , true],
		border : [0],
		area : ['455px','371px'],
		page : {dom : '#creatuser'}
	});	
	
};



function clickMore () {
	
	$.ajax({
    	url: '/test1/',
        type: "POST",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
                
        success: function (msg) {
                 	
					var len=msg.length;
					
					for (var i=0;i<len;i++)
						{
							$("#result").append('<li id="">' +
                            this.Id + ' - ' + '<strong>' +
                            this.Name + '</strong>' + ' — ' + '<span class="page_message">' +
                            this.Comment + '</span></li>');
						}
					
					var fff=msg[i].pk;
                    $('#result').append(fff);
                 },
				 
        error: function (xmlHttpRequest, textStatus, errorThrown) {
               		alert(xmlHttpRequest.status);
               		alert(xmlHttpRequest.Readystate);
               		alert(textStatus);
               }
     });
                         
};