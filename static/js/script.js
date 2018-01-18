$(document).ready(function(){
  $(".toggle-details").click(function(){
      $(this).text(function(i, text){
        return text === "Show Details" ? "Hide Details" : "Show Details";
      })
      $(".collapse").collapse('toggle');
  });
  
});