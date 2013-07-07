

function openUrl(url) {
	chrome.tabs.create({
		'url': url,
		"active": false
	});
}

function onRequest(request, sender, sendResponse) {
	console.info(request);
	openUrl(request.url);
}
chrome.runtime.onMessage.addListener(onRequest);