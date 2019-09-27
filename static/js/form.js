
$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				newtext : $('#main-text').val()
				
			},
			type : 'POST',
			url : '/'
		})
		.done(function(data) {

		
		});

		event.preventDefault();

	});

});
