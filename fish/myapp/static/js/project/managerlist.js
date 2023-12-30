(function($) {
  $(".load_data").click(function(){
    const url=`/personel/brief/getInfo?makan=${$("#asset_id").val()}`;
    $.ajax({
      url:url,
      type:'get',
      success:function(data){
        
        $("#thead_company").empty();
        $("#thead_company").html(data.header);
        $("#tbody-company").empty();
        $("#tbody-company").html(data.result);



      }
    });
});



})(jQuery);
