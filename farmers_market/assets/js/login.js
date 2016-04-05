$(document).on('submit','#logintest',function(e){
  e.preventDefault();
  $.ajax({
       type:'POST',
       url:'action/',
       data: {
              'username':  document.getElementById("login-name").value ,// from form
              'password' : document.getElementById("login-pass").value ,
              'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
              },
              success: function(data){
                var data =  JSON.parse(data);
                console.log(data["userid"]);
                if(data["userid"] != 0){
                  localStorage.setItem("userid", data["userid"]);
                  window.location.href = "../home";
                }
                else{
                  alert("Invalid username");
                }

                      }
  });
});
