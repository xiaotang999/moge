var asd = {
	"0" : {"color" : "red", "shengxiao" : " "},
	"1" : {"color" : "red", "shengxiao" : "狗"},
	//
	"2" : {"color" : "red", "shengxiao" : "鸡"},
	"3" : {"color" : "blue", "shengxiao" : "猴"},
	"4" : {"color" : "blue", "shengxiao" : "羊"},
	"5" : {"color" : "green", "shengxiao" : "马"},
	"6" : {"color" : "green", "shengxiao" : "蛇"},
	"7" : {"color" : "red", "shengxiao" : "龙"},
	"8" : {"color" : "red", "shengxiao" : "兔"},
	"9" : {"color" : "blue", "shengxiao" : "虎"},
	"10" : {"color" : "blue", "shengxiao" : "牛"},
	"11" : {"color" : "green", "shengxiao" : "鼠"},
	"12" : {"color" : "red", "shengxiao" : "猪"},
	"13" : {"color" : "red", "shengxiao" : "狗"},
	//
	"14" : {"color" : "blue", "shengxiao" : "鸡"},
	"15" : {"color" : "blue", "shengxiao" : "猴"},
	"16" : {"color" : "green", "shengxiao" : "羊"},
	"17" : {"color" : "green", "shengxiao" : "马"},
	"18" : {"color" : "red", "shengxiao" : "蛇"},
	"19" : {"color" : "red", "shengxiao" : "龙"},
	"20" : {"color" : "blue", "shengxiao" : "兔"},
	"21" : {"color" : "green", "shengxiao" : "虎"},
	"22" : {"color" : "green", "shengxiao" : "牛"},
	"23" : {"color" : "red", "shengxiao" : "鼠"},
	"24" : {"color" : "red", "shengxiao" : "猪"},
	"25" : {"color" : "blue", "shengxiao" : "狗"},
	//
	"26" : {"color" : "blue", "shengxiao" : "鸡"},
	"27" : {"color" : "green", "shengxiao" : "猴"},
	"28" : {"color" : "green", "shengxiao" : "羊"},
	"29" : {"color" : "red", "shengxiao" : "马"},
	"30" : {"color" : "red", "shengxiao" : "蛇"},
	"31" : {"color" : "red", "shengxiao" : "龙"},
	"32" : {"color" : "green", "shengxiao" : "兔"},
	"33" : {"color" : "green", "shengxiao" : "虎"},
	"34" : {"color" : "red", "shengxiao" : "牛"},
	"35" : {"color" : "red", "shengxiao" : "鼠"},
	"36" : {"color" : "blue", "shengxiao" : "猪"},
	"37" : {"color" : "blue", "shengxiao" : "狗"},
	//
	"38" : {"color" : "green", "shengxiao" : "鸡"},
	"39" : {"color" : "green", "shengxiao" : "猴"},
	"40" : {"color" : "red", "shengxiao" : "羊"},
	"41" : {"color" : "blue", "shengxiao" : "马"},
	"42" : {"color" : "blue", "shengxiao" : "蛇"},
	"43" : {"color" : "green", "shengxiao" : "龙"},
	"44" : {"color" : "green", "shengxiao" : "兔"},
	"45" : {"color" : "red", "shengxiao" : "虎"},
	"46" : {"color" : "red", "shengxiao" : "牛"},
	"47" : {"color" : "blue", "shengxiao" : "鼠"},
	"48" : {"color" : "blue", "shengxiao" : "猪"},
	"49" : {"color" : "green", "shengxiao" : "狗"},
}
function writer(data){
	document.getElementsByClassName("up1")[0].innerHTML = data[0];
	document.getElementsByClassName("up1")[0].style.background = asd[data[0]]["color"];
	document.getElementsByClassName("down1")[0].innerHTML = asd[data[0]]["shengxiao"];

	document.getElementsByClassName("up2")[0].innerHTML = data[1];
	document.getElementsByClassName("up2")[0].style.background = asd[data[1]]["color"];
	document.getElementsByClassName("down2")[0].innerHTML = asd[data[1]]["shengxiao"];

	document.getElementsByClassName("up3")[0].innerHTML = data[2];
	document.getElementsByClassName("up3")[0].style.background = asd[data[2]]["color"];
	document.getElementsByClassName("down3")[0].innerHTML = asd[data[2]]["shengxiao"];

	document.getElementsByClassName("up4")[0].innerHTML = data[3];
	document.getElementsByClassName("up4")[0].style.background = asd[data[3]]["color"];
	document.getElementsByClassName("down4")[0].innerHTML = asd[data[3]]["shengxiao"];

	document.getElementsByClassName("up5")[0].innerHTML = data[4];
	document.getElementsByClassName("up5")[0].style.background = asd[data[4]]["color"];
	document.getElementsByClassName("down5")[0].innerHTML = asd[data[4]]["shengxiao"];

	document.getElementsByClassName("up6")[0].innerHTML = data[5];
	document.getElementsByClassName("up6")[0].style.background = asd[data[5]]["color"];
	document.getElementsByClassName("down6")[0].innerHTML = asd[data[5]]["shengxiao"];

	document.getElementsByClassName("up7")[0].innerHTML = data[6];
	document.getElementsByClassName("up7")[0].style.background = asd[data[6]]["color"];
	document.getElementsByClassName("down7")[0].innerHTML = asd[data[6]]["shengxiao"];
}
document.getElementById("close1").onclick = function(){
	document.getElementById("piaochuan1").style.display = "none"
}
document.getElementById("close2").onclick = function(){
	document.getElementById("piaochuan2").style.display = "none"
}