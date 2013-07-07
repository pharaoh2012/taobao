


function doopenall(id)
{
//var alinks = document.querySelectorAll('#nanzhuang a.shopa');
var alinks = document.querySelectorAll('#'+id+' a.shopa');

for(var i=0;i<alinks.length;i++)
{
	open(alinks[i].href);
}
}

doopenall('nanzhuang')

doopenall('nvzhuang')







function getUrl(url, fn) {
	var req = new XMLHttpRequest();
	if (url.indexOf('?') > 0) {
		url += "&tttt=" + new Date();
	} else {
		url += "?tttt=" + new Date();
	}
	req.open("GET", url, true);
	req.onreadystatechange = function() {
		if ((req.readyState == 4) && (req.status == 200)) {
			if (fn) fn(req.responseText);
		}
	};
	req.send(null);
}



function doJinbi(js)
{
//console.info(js);
    eval(js);
    
}

function jsonp198(data)
{
	//console.info(data);
    for(var i=0;i<data['shops'].length;i++)
{
   console.info( 'url', data['shops'][i]['shopUrl']);
   open(data['shops'][i]['shopUrl']);
}
   //data['shops']['shopUrl']
}

var taobaourl = 'http://taojinbi.taobao.com/json/categoryShowActivity.htm?index=1&callback=jsonp198';

window.setInterval(function(){getUrl(taobaourl,doJinbi);},50000);

getUrl(taobaourl,doJinbi);