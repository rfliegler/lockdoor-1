$(function(){
  $("tr").each(function(){
    var col_val = $(this).find("td:eq(1)").text();
    if (col_val == "none"){
      $(this).addClass('selected');  //the selected class colors the row green//
    } else {
      $(this).addClass('bad');
    }
  });
});
