function js(fileUrl) {
	// var oHead = document.getElementsByTagName('HEAD').item(0);
	// var oScript = document.createElement("script");
	// oScript.type = "text/javascript";
	// oScript.src = fileUrl;
	// oHead.appendChild(oScript);
	console.info("get url:"+fileUrl);
	getUrl(fileUrl,urlcontent);
}

function getUrl(url, fn) {
    var req = new XMLHttpRequest();
    req.open("GET", url, true);
    console.debug("getUrl:", url);
    req.onreadystatechange = function() {
        if ((req.readyState == 4) && (req.status == 200)) {
            if (fn) fn(req.responseText);
        }
    };
    req.send(null);
}

function HTMLDecode(txt) {
	var temp = document.createElement("div");
	temp.innerHTML = txt;
	var output = temp.innerText || temp.textContent;
	temp = null;
	return output;
}

function urlcontent(data) {
	taobaotext = HTMLDecode(data);
	console.info(taobaotext);
	var propertys = taobaotext.split('\n');
	proprty = document.getElementById('J_Question').getElementsByTagName('em')[0].innerText;

	for (var i = 0; i < propertys.length; i++) {
		if (propertys[i].indexOf(proprty) >= 0) {
			taobaotext = propertys[i];
			break;
		}
	}
	document.title = 'end';
	var result = taobaotext.replace(proprty, '').replace(":", "").substr(1);
	console.info(result);
	setAnswer(result);
}

function setAnswer (answer) {
	document.getElementById('J_AnswerInput').value = answer;
	document.getElementById('J_Answer').getElementsByTagName('a')[0].click();	
	setTimeout(function() {
		document.getElementsByClassName("try-btn-submit")[0].click();
	}, 2000);
}

document.title = 'begin load';

if(document.getElementById('J_Question').getElementsByTagName('em')[0].innerText=="试用品申请成功后需提交")
{
	setAnswer("报告");
}
else
{
	var taobaohref = escape(document.getElementById('J_Question').getElementsByTagName('a')[0].href);
	js("http://127.0.0.1:7702/taobao/" + taobaohref);

}