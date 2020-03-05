function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(document).ready(function() {		// doc ready

  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

  $.ajaxSetup({
  		beforeSend: function(xhr, settings) {
  				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
  						xhr.setRequestHeader("X-CSRFToken", csrftoken);
  				}
  		}
  });


	$('.sel').click(function() {
		var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    console.log(csrftoken);
		var login = this.id.substr(4,20);
		//Check = confirm('Wollen Sie "'+login+'" übernehmen?');
    Check = true;
		if (Check == true) {
          var data = {
						'login' : login,
						'csrf_token' : csrftoken,
  				}
          var success = false;

			var li = jQuery('#loadingicon');
			li.css('visibility', 'visible');

			$.ajax({
				url: "/cat/coll/add/",
				type: "POST",
				data: data,
				dataType: "text",
				tryCount: 0,
				retryLimit: 1,
			  })
				.done(function(rtext) {
					$('#outmsg').html(rtext);

				})
				.fail(function(rtext) {
					$('#outerrmsg').html(rtext);

				})
				.always(function(xhr, status) {
					console.log('ajax done');
				});
				return false;
			}; // if check
		}); 	 // .sel

});		// document ready
