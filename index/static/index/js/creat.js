function creat() {	//定义函数
	var name = $("#username").val();
	var pass1 = $("#password1").val();		
	var pass2 = $("#password1").val();
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
			$("#tip2").append(msg);
        },

        error: function (xmlHttpRequest, textStatus, errorThrown) {
            alert(xmlHttpRequest.status);
            alert(xmlHttpRequest.Readystate);
            alert(textStatus);
        }
    });

}