
$(document).ready(function() {		// doc ready

  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

  $.ajaxSetup({
  		beforeSend: function(xhr, settings) {
  				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
  						xhr.setRequestHeader("X-CSRFToken", csrftoken);
  				}
  		}
  });


	$('.delete').click(function() {
		var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

		$('#sub').fadeOut('slow');
		//$('#delete_div').css('visibility','visible');  // warum geht fade nicht?
		//$('#delete_div').fadeIn('slow');
		var login = this.id.substr(4,20);
		Check = confirm('Wollen Sie den Benutzer "'+login+'" wirklich löschen?');
		if (Check == true) {
          var data = {
						'login' : login,
						'csrf_token' : csrftoken,
  				}
          var lname = $('#'+login);
          var sname = lname.find('span[name]');
          var success = false;

			var li = jQuery('#loadingicon');
			li.css('visibility', 'visible');

			$.ajax({
				url: prefix+"/konto/unterkonten/delete/",
				type: "POST",
				data: data,
				dataType: "text",
				tryCount: 0,
				retryLimit: 1,
			  })
				.done(function(rtext) {
					alert(rtext);
					lname.css('display','none');
					$('#outmsg').html(rtext);

				})
				.fail(function(rtext) {
					rtext = rtext.substr(5);
					$('#outerrmsg').html(rtext);

				})
				.always(function(xhr, status) {
					console.log('ajax done');
				});
				return false;
			}; // if check
		}); 	 // .delete

    }); // submit login

	});		// document ready
