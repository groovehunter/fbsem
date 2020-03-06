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
		var tid = this.id.substr(4,20);
    var data = {
			'tid' : tid,
			'csrf_token' : csrftoken,
    }

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
          var imgtag = $('#img_'+tid).html();
					$('#outmsg').html(rtext);
          $('#to_add').append(imgtag);
          console.log('ajax success - img tag copied');
				})
				.fail(function(rtext) {
          console.log('FAIL');
					$('#outerrmsg').html(rtext);
				})
				.always(function(xhr, status) {
					console.log('ajax done');
				});
				return false;
		}); 	 // .sel

});		// document ready
