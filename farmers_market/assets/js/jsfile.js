$(document).ready(function(){
  function hello(){
    //var id = localStorage.getItem("userid");
    //localStorage.removeItem("userid");
    //if(localStorage.getItem("userid"))
    console.log(session.get('user_id',''));
  }
  hello();
});
