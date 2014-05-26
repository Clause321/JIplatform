// JavaScript Document

var i=0;	//设定全局变量 i 初始值为 0

function getMore() {	//定义函数
	i++;	// i=i+1
	$("#list").append(	//在id为list的元素中插入 需要jQuery 
	'<div class="floatb">第' + i +'个框</div>'	//第i个框，html语言用''括起来
	);
};




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

function loginbtn(){
	    var bvalid=0;
		$("#tip1").html("");
		
		if( $("#email1").val().length != 0){
			apos=$("#email1").val().indexOf("@");
			dotpos=$("#email1").val().lastIndexOf(".");
			if (apos<1||dotpos-apos<2){bvalid=1; $("#tip1").html("邮箱格式不正确");}
			else {bvalid=bvalid+0;}	
		
		}
		else{bvalid=1;$("#tip1").html("邮箱不能为空");}
		
		if( $("#password1").val().length < 6 || $("#password1").val().length > 12){
			bvalid=1;
			$("#tip1").html("密码长度在6到12字之间");
		}
		else{bvalid=bvalid+0;}
		
		if(bvalid ==0){
			$("#tip1").html("请等待...");
			$.post(
				/url/,
				{
					email: $("#email1").val(),
					password: $("#password1").val()
				},
				function (data){
					if (data){$("#tip1").html("登陆成功");layer.close(i);}
					else{$("#tip1").html("用户名或密码不正确");}
				}	
			);
		}
};

function cubtn(){
	    var cvalid=0;
		$("#tip2").html("");
		
		if( $("#name").val().length < 1 || $("#name").val().length >15){
			cvalid=1;
			$("#tip2").html("用户名长度在1到15字之间");
		}
		else{cvalid=0;}
		
		if( $("#email2").val().length != 0){
			apos=$("#email2").val().indexOf("@");
			dotpos=$("#email2").val().lastIndexOf(".");
			if (apos<1||dotpos-apos<2){cvalid=1; $("#tip2").html("邮箱格式不正确");}
			else {cvalid=cvalid+0;}	
		
		}
		else{cvalid=1;$("#tip2").html("邮箱不能为空");}
		
		if( $("#password2").val().length < 6 || $("#password2").val().length > 12){
			cvalid=1;
			$("#tip2").html("密码长度在6到12字之间");
		}
		else{cvalid=cvalid+0;}
		
		if(cvalid ==0){
			$("#tip2").html("请等待...");
			$.post(
				/url/,
				{
					name: $("#name").val(),
					email: $("#email2").val(),
					password: $("#password2").val()
				},
				function (data){
					if (data){$("#tip2").html("注册成功");layer.close(j);}
					else{$("#tip2").html("用户名已存在");}
				}	
			);
		}
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