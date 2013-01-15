$(function(){	
	$('#id_get').click(function(e){
		e.preventDefault();
		GET();
	});
	$('#id_put').click(function(e){
		e.preventDefault();
		PUT();
	});
	$('#id_post').click(function(e){
		e.preventDefault();
		POST();
	});
	$('#id_get_actual_on').click(function(e){
		e.preventDefault();
		GET_ActualOn();
	});
	$('#id_check').click(function(e){
		e.preventDefault();
		CheckAPIProcess();
	});
	$('#id_clear').click(function(e){
		e.preventDefault();
		result_holder.html('<legend>Result Elements</legend>');
	});
	
	var result_holder = $('#result');
	
	function Open(method, params){
		var ajax_params = {
			url: '/open',
			async: false,
			type: method,
			data: params,
			success: function(data, status){
				result_holder
					.prepend('<hr class="line">')
					.prepend(Wapper.Url(params.host+params.url))
					.prepend('<br class="clear" />')
					.prepend(Wapper.Data(data))
					.prepend(Wapper.Status(status))
					.prepend(Wapper.Div(method))
					.prepend(Wapper.Div(new Date().toLocaleTimeString()));
			},
			error: function(xhr, status){
				result_holder
					.prepend('<hr class="line">')
					.prepend(Wapper.Url(params.host+params.url))
					.prepend('<br class="clear" />')
					.prepend(Wapper.Data(xhr.status + xhr.statusText))
					.prepend(Wapper.Status(status))
					.prepend(Wapper.Div(method))
					.prepend(Wapper.Div((new Date()).toLocaleTimeString()));
			}
		};
		$.ajax(ajax_params);
	}
	
	function GET_ActualOn(){
		data = GetData();
		data.url = ActualOnUrl(data.url)
		Open('GET', data);
	}
	
	function GET(){
		Open('GET', GetData());
	}
	
	function PUT(){
		Open('PUT', GetData());
	}
	function POST(){
		Open('POST', GetData())
	}
	
	function CheckAPIProcess(){
		GET_ActualOn();
		PUT();
		GET_ActualOn();
		GET();
	}
	
	function GetData(){
		var data = {}
		$('input[type=text]').each(function(){
			var ele = $(this);
			data[ele.attr('name')] = ele.val()
		});
		return data;
	}
	
	function ActualOnUrl(url){
		var items = url.split('?');
		return items[0] + '/actual_on?' + items[1];
	}
	
	var Wapper = {
		Div: function(value){return '<div class="wapper">'+value+'</div>'},
		Data: function(value){return '<div class="wapper red">'+value+'</div>'},
		Status: function(value){return '<div class="wapper status">'+value+'</div>'},
		Url: function(value){return '<p class="res_url">'+value+'</p>'}
	}
	
	function Action(self, method, data, e){
		e.preventDefault();
		var url = self.parent().find('#url').text();
		data.url = url
		$.ajax({
			url: '/action',
			type: method,
			data: data,
			success: function(data){
				self.parent().find('.div_res')
					.addClass('res_style')
					.prepend('<hr class="line">')
					.prepend(data);
			}
		});
	}
	
	$('.put_action').click(function(e){
		Action($(this), 'PUT', {}, e);
	});
	$('.get_action').click(function(e){
		Action($(this), 'GET', {}, e);
	});
	$('.post_action').click(function(e){
		Action($(this), 'POST', {}, e);
	});
	$('.actual_on_action').click(function(e){
		Action($(this), 'GET', {type: 'actual_on'}, e);
	});
	
	$('.del_url').click(function(e){
		e.preventDefault();
		var self = $(this);
		var url = self.parent().find('#url').text();
		$.ajax({
			url: '/action',
			type: 'GET',
			data: {url: url, type: 'delete'},
			success: function(data){
				self.parent().next().remove();
				self.parent().remove();
			}
		});
	});
	
	$('li').each(function(){
		var text = $(this).text();
		if ( $.trim(text) == ""){
			$(this).remove();
		}
	});
});