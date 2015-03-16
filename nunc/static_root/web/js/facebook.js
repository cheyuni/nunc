window.fbAsyncInit = function() {
  FB.init({
    appId      : '525170764238004',
	status     : true, // check login status
	xfbml      : true,
	version    : 'v2.2'
	});

  FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
};

(function(d, s, id){
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) {return;}
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/sdk.js";
  fjs.parentNode.insertBefore(js, fjs);
 }(document, 'script', 'facebook-jssdk'));


function checkLoginState() {
  FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
}


function logout() {
  FB.logout(function(response) {
      window.location.href = '/logout';
    });
}

function nunc_login() {
  FB.api('/me', function(response) {
      $("#email").val(response.email);
      $("#first_name").val(response.first_name);
      $("#last_name").val(response.last_name);
      $("#id").val(response.id);
      $("#name").val(response.name);
      $("#login-form").submit();
    });

}
