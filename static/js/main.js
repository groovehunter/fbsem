/**
 * verschiedene einfache js helper functions
*/


/* alle checkboxen auf check (boolean) setzen 
wird aufgerufen von select_all 
*/
function do_all( check ) {
    var chb = document.getElementsByTagName("input");
    for (i=1; i<chb.length; i++) {
    	if ( chb[i].name.substr(0,3) == 'obj' ) {
    		chb[i].checked = check;
    	}
    }
    document.getElementById("sel_all1").checked = check;
    document.getElementById("sel_all2").checked = check;
    return false;
}

/* alle checkboxen setzen gemaess der box mit id=sel_all */
//function select_all(this) {
function select_all(n) {
    var cur = document.getElementById("sel_all"+n).checked;
	if (n==1) {
		document.getElementById('sel_all2').checked = cur;
	} else {
		document.getElementById('sel_all1').checked = cur;
	}
//    var cur = this.checked;
    do_all(cur);
}


    //var eid = elem.getAttribute("id");
    //var mid = eid.substring(5);

function tobot( mid, check ) {
    var chb = document.getElementsByTagName("input");
    //var check = !chb[mid].checked;
    for (i=mid; i<chb.length; i++) {
	chb[i].checked = check;
    }
    
}
function totop( mid, check ) {
    var chb = document.getElementsByTagName("input");
    //var check = !chb[mid].checked;
    for (i=1; i<=mid; i++) {
	chb[i].checked = check;
    }
}


function mytest() {
    //var cal = new CalendarPopup('div2');
    var cal = new PopupWindow('div2');
    cal.setSize(150, 175);
    cal.x = 100;
    cal.y = 100;
//    cal.use_gebi = false;
    cal.populate('content test');
    cal.showPopup('anchor1');
    //alert('TEST');
}


function submitform( params ) {
    var form = document.my;

    for(var key in params) {
        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", params[key]);
        form.appendChild(hiddenField);
    }
    form.submit();
}


/* Weitere Optionen einblenden bzw ausblenden */
function show( elemid ) {
    var more = document.getElementById( elemid );
    if ( more.style.visibility == 'visible') {
	more.style.visibility = 'hidden';
    } else {
	more.style.visibility = 'visible';
    }
}

function showmore( mode ) {
    var more = document.getElementById( 'more' );
	more.style.visibility = mode;
}


function isbrowser(t) {
    u = navigator.userAgent;
    var ua = u.toLowerCase();
    if ( ua.indexOf(t) > -1 ) {
	return true;
    }
}

function setrowread(t) {
	t.parentNode.parentNode.style.setProperty('font-weight','normal','');
	return true;
}



