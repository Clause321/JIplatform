// JavaScript Document


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
