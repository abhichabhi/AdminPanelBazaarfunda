function updateHomeBanner(frmVariable) { 
	
	var sliderBanner=new Array();
	var arrIndex=0;
	var TBanner = ""
	var PBanner = ""
	var MediaBanner = ""
	for(var i=0;i<frmVariable.elements.length;i++){
		if (frmVariable.elements[i].name=='TBanner') {
			TBanner = frmVariable.elements[i].value
		}
		if (frmVariable.elements[i].name=='PBanner') {
			PBanner = frmVariable.elements[i].value
		}
		if (frmVariable.elements[i].name=='SBanner') {
			SBanner = frmVariable.elements[i].value
			if (SBanner != "" && SBanner != "new") {
				sliderBanner[arrIndex] = SBanner;
				arrIndex ++;
			}
		}

		if (frmVariable.elements[i].name=='MediaBanner') {
			MediaBanner = frmVariable.elements[i].value
		}
		if (frmVariable.elements[i].name=='MediaLink') {
			MediaLink = frmVariable.elements[i].value
		}
		
	}

	$domain = location.host
	$url = "http://"  + $domain + "/banner/home/submit"
	$url = $url + "?TBanner=" + TBanner + "&PBanner=" + PBanner + "&sliderBanner=" + sliderBanner + "&MediaLink=" + MediaLink + "&MediaBanner=" + MediaBanner
	console.log(httpGet($url))

}

function updateListingBanner(frmVariable) { 
	TBannerLinkList = new Array();
	tBannerLinkIndex = 0
	TBannerLocList = new Array();
	tBannerLocIndex = 0
	category = location.search.split('category=')[1]?location.search.split('category=')[1]:"0";
	for(var i=0;i<frmVariable.elements.length;i++) {
		if (frmVariable.elements[i].name == 'newCategory') {
			category = frmVariable.elements[i].value
			break;
		}
	}

	TBannerList = extractedValues('TBanner', frmVariable)
	console.log(TBannerList)
	hotbrandsList = extractedValues('hotbrands', frmVariable)
	compareItemsIDList = extractedValues('compareItemsID', frmVariable)
	economicbrandsList = extractedValues('economicbrands', frmVariable)
	responseJson = {}
	responseJson['compareitems'] = compareItemsIDList
	responseJson['hotbrands'] = hotbrandsList
	responseJson['economicbrands'] = economicbrandsList
	responseJson['topbanner'] = TBannerList
	dataJSON = {}
	dataJSON['data'] = responseJson
	dataJSON['category'] = category
	$domain = location.host
	$url = "http://"  + $domain + "/banner/listing/submit"
	httpAjaxPost($url, JSON.stringify(dataJSON))
	
	return false;
}

function extractedValues(name, frmVariable) {
	link = name + "Link"
	loc = name + "Location"
	newLink = link + "New"
	newLocation = loc + "New"
	TBannerLinkList = new Array();
	tBannerLinkIndex = 0
	TBannerLocList = new Array();
	tBannerLocIndex = 0

	for(var i=0;i<frmVariable.elements.length;i++){

		if (frmVariable.elements[i].name == link){

			if (frmVariable.elements[i].value != '' && frmVariable.elements[i].value != "new") {
				
				TBannerLinkList[tBannerLinkIndex] = frmVariable.elements[i].value
			tBannerLinkIndex ++;
			}
		}
		if (frmVariable.elements[i].name == loc){
			if (frmVariable.elements[i].value !='' && frmVariable.elements[i].value != "new") {
				
				TBannerLocList[tBannerLocIndex] = frmVariable.elements[i].value
			tBannerLocIndex ++;
			}
		}
		if (frmVariable.elements[i].name == newLink){
			if (frmVariable.elements[i].value != '' && frmVariable.elements[i].value != "new") {
				TBannerLinkList[tBannerLinkIndex] = frmVariable.elements[i].value
			tBannerLinkIndex ++;
			}			
		}
		if (frmVariable.elements[i].name == newLocation){
			if (frmVariable.elements[i].value != '' && frmVariable.elements[i].value != "new") {
				TBannerLocList[tBannerLocIndex] = frmVariable.elements[i].value
			tBannerLocIndex ++;
			}
		}		
	}
	dictList = new Array();
	for (i=0;i< tBannerLocIndex; i++){
		dict = {}
		dict['link'] = TBannerLinkList[i]
		dict['location'] = TBannerLocList[i]
		
		dictList[i] = dict
	}
	return dictList
}


function httpGet(theUrl)
        {
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.open( "GET", theUrl, false );
            xmlHttp.send( null );
            return xmlHttp.responseText;
        }
function httpAjaxPost(urlAddress, jsonData) {
	jQuery.ajax({
            url: urlAddress,
            type: 'PUT',
            headers: {
		        "Content-Type": "application/json"
		    },
            data: jsonData,
            success: function() { alert('Entry Successfully'); }
        });
}