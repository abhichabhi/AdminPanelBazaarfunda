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
			 console.log(frmVariable.elements[i].value)
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
	console.log(TBanner)
	console.log(PBanner)
	console.log(sliderBanner)
	console.log(MediaLink)
	console.log(MediaBanner)
	$domain = location.host
	$url = "http://"  + $domain + "/banner/home/submit"
	$url = $url + "?TBanner=" + TBanner + "&PBanner=" + PBanner + "&sliderBanner=" + sliderBanner + "&MediaLink=" + MediaLink + "&MediaBanner=" + MediaBanner
	console.log(httpGet($url))

}

function httpGet(theUrl)
        {
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.open( "GET", theUrl, false );
            xmlHttp.send( null );
            return xmlHttp.responseText;
        }