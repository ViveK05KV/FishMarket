$(document).ready(function() {
    $("#item_del").submit(function(event){
      $.ajax({
           type:"POST",
           url:"deleteitem/",
           data: {
                  'item_id':  document.getElementById("item_id").value ,// from form
                  },
                  success: function(){
                              console.log("Ok");
                              //window.location.assign("/fish/one/showcart/");
                              window.location.href = "/fish/one/showcart/";
                          }
      });
      return false; //<---- move it here
    });
    $("#cart_clr").click(function(){
      $.ajax({
           type:"POST",
           url:"emptycart/",
           data: {
                  'item_id':  document.getElementById("item_id").value ,// from form
                  },
                  success: function(){
                              console.log("Ok");
                              //window.location.assign("/fish/one/showcart/");
                              window.location.href = "/fish/one/showcart/";
                          }
      });
      return false; //<---- move it here
    });

    //----------------------------------------------------------------------------------------------------

    $("#whole_counter").text(whole_counter);

    //----------------------------------------------------------------------------------------------------

});
