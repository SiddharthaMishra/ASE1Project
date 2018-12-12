$(document).ready(function(){



	$('.msg_head').click(function(){
		var chatbox = $(this).parents().attr("rel") ;
		$('[rel="'+chatbox+'"] .msg_wrap').slideToggle('slow');
		return false;
	});

	$('.close').click(function(){

		var chatbox = $(this).parents().parents().attr("rel") ;
		$('[rel="'+chatbox+'"]').hide();
		//update require
	  
		return false;
	});

	$('textarea').keypress(
    function(e){

        if (e.keyCode == 13) {
            var msg = $(this).val();
			$(this).val('');
			if(msg.trim().length != 0){
			var chatbox = $(this).parents().parents().parents().attr("rel") ;
			$('<div class="msg-right">'+msg+'</div>').insertBefore('[rel="'+chatbox+'"] .msg_push');
			$('.msg_body').scrollTop($('.msg_body')[0].scrollHeight);
			}
			b=msg.replace(/\s/g, '')
			a=b.toLowerCase();
		
			
			if(a.includes('hi')==true ||a.includes('hai')==true|| a.includes('hello')==true){
				var w='Hi user,how can i help u'
				$('<div class="msg-left">'+w+'</div>').insertBefore('[rel="'+chatbox+'"] .msg_push');
				$('.msg_body').scrollTop($('.msg_body')[0].scrollHeight);
			}
			if(a.includes('signup')==true || a.includes('join')==true){
				
				var w="U can find it on the navbar at the top";
				

				$('<div class="msg-left" id="login" on>'+w+'</div>').insertBefore('[rel="'+chatbox+'"] .msg_push');

				$('.msg_body').scrollTop($('.msg_body')[0].scrollHeight);
				$("#sign")[0].click();
			}
			if(a.includes('login')==true){
				
				var w="U can find it on the navbar at the top";
				

				$('<div class="msg-left" id="login" on>'+w+'</div>').insertBefore('[rel="'+chatbox+'"] .msg_push');

				$('.msg_body').scrollTop($('.msg_body')[0].scrollHeight);
				$("#login")[0].click();
			}
			if(a.includes('securestore')==true){
				
				var w="SECURE STORE is our website,you can stores ur files securely";
				

				$('<div class="msg-left" id="login" on>'+w+'</div>').insertBefore('[rel="'+chatbox+'"] .msg_push');

				$('.msg_body').scrollTop($('.msg_body')[0].scrollHeight);
				$("#login")[0].click();
			}
			if(a.includes('charge')==true||a.includes('price')==true||a.includes('money')==true||a.includes('money')==true){
				var w='U will be given 15GB data ,for more u need to pay'
				$('<div class="msg-left">'+w+'</div>').insertBefore('[rel="'+chatbox+'"] .msg_push');
				$('.msg_body').scrollTop($('.msg_body')[0].scrollHeight);
			}
			
		   if(a.includes('price')==false&&a.includes('money')==false&&a.includes('money')==false &&a.includes('hai')==false&& a.includes('hello')==false && a.includes('hi')==false && a.includes('signup')==false && a.includes('join')==false && a.includes('login')==false && a.includes('charge')==false){
				var w='Sorry we couldnt understand, We will come back to u soon'
				$('<div class="msg-left">'+w+'</div>').insertBefore('[rel="'+chatbox+'"] .msg_push');
				$('.msg_body').scrollTop($('.msg_body')[0].scrollHeight);
			   }
			} 
    });

});
