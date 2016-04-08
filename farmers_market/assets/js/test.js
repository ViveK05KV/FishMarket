$(document).ready(function() {
    $("#test").submit(function(event){
      $.ajax({
           type:"POST",
           url:"deleteitem/",
           data: {
                  'item_id':  document.getElementById("item_id").value ,// from form
                  },
                  success: function(){
                              console.log("Ok");
                              window.location.href = "/fish/one/showcart/";
                          }
      });
      return false; //<---- move it here
    });

});
