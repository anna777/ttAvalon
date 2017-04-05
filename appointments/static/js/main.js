function initDateFields() {
  var date = '.dateinput';
  var icon = '<span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>'

  	$(date).wrap('<div class="input-group date col-sm-4"></div>');
  	$(icon).insertAfter(date);

  	$(date).datetimepicker({
  		'format': 'YYYY-MM-DD',
  	}).on('dp.hide', function(event){
  		$(this).blur();
  	});

  }

$(document).ready(function(){
initDateFields();

});
