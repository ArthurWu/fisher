$(function(){
	$('#id_reflash').click(function(e){
		e.preventDefault();
		loadTestResults();
	});

	$('#id_total').click(function(){$('ul.unstyled li').show();});
	$('#id_red').click(function(){filterResult('error');});
	$('#id_gray').click(function(){filterResult('warring');});
	$('#id_green').click(function(){filterResult('success');});

	function filterResult(flag){
		$('ul.unstyled li').each(function(){
			var self = $(this);
			if (self.hasClass(flag))
			{
				self.show();
			}
			else
			{
				self.hide();
			}
		});
	}
});

function loadTestResults(){
	var request_url = '/test-results';
	var template = '<li class="{{if green}}success{{/if}} {{if gray}}warring{{/if}} {{if red}}error{{/if}}"><a target="_blank" href="${url}">${url}</a></li>';
	$.getJSON(request_url, function(data){
		$('#id_total').append(data.length);
		$('#id_red').append(red(data));
		$('#id_gray').append(gray(data));
		$('#id_green').append(green(data));
		$.tmpl(template, data).appendTo('#id_results');
	});
}

function red(data)
{
	var res = $.grep(data, function(el){
		return el.red;
	});
	return res.length;
}
function gray(data)
{
	var res = $.grep(data, function(el){
		return el.gray;
	});
	return res.length;
}
function green(data)
{
	var res = $.grep(data, function(el){
		return el.green;
	});
	return res.length;
}