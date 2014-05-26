// JavaScript Document

var i=0;	//设定全局变量 i 初始值为 0

function getMore() {	//定义函数
	i++;	// i=i+1
	$("#list").append(	//在id为list的元素中插入 需要jQuery 
	'<div class="floatb">第' + i +'个框</div>'	//第i个框，html语言用''括起来
	);
};