

function login() {	//定义函数
	var name = $("#username").val();
	var pass = $("#password").val();
    $.ajax({
        url: '/login/',
        type: "POST",
        dataType: "json",
        data: [
                    { name: "username", value: name },
					{ name: "password", value: pass },
        ],

        success: function (msg) {
			$("#tip1").append(msg.message);
			if(msg.message == "success"){window.location.reload();}
        },

        error: function (xmlHttpRequest, textStatus, errorThrown) {
            alert(xmlHttpRequest.status);
            alert(xmlHttpRequest.Readystate);
            alert(textStatus);
        }
    });

}