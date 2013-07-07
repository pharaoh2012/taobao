


function docollection()
{

if(document.location.host=="favorite.taobao.com") 
{
	document.title='ok0';
	setTimeout(function(){ window.close(); },2000);	
	return;
}

if(document.getElementsByClassName('no-collect').length>0)
{
	document.getElementsByClassName('no-collect')[0].click();
	document.title='ok';
	setTimeout(function(){ window.close(); },2000);
}
else if(document.getElementsByClassName('collection').length>0)
{
	document.getElementsByClassName('collection')[0].click();
	document.title='ok1';
	setTimeout(function(){ window.close(); },2000);
}
else{
	document.title='not';
}

}

docollection();

setTimeout(docollection,3000);