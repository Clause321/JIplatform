function creat() {	//定义函数
	var name = $("#username1").val();
	var pass1 = $("#password1").val();
	var pass2 = $("#password2").val();
    $.ajax({
        url: '/register/',
        type: "POST",
        dataType: "json",
        data: [
                    { name: "username", value: name },
					{ name: "password1", value: pass1 },
					{ name: "password2", value: pass2 },
        ],

        success: function (msg) {
			if( msg.username ){
			$("#tip21").append(msg.username[0].message);
			}
			if( msg.password1 ){
			$("#tip22").append(msg.password1[0].message);
			}
			if( msg.password2 ){
			$("#tip23").append(msg.password2[0].message);
			}
			if(msg.message == "success"){window.location.reload();}
        },

        error: function (xmlHttpRequest, textStatus, errorThrown) {
            alert(xmlHttpRequest.status);
            alert(xmlHttpRequest.Readystate);
            alert(textStatus);
        }
    });

}