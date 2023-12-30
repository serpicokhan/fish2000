(function($) {
  $(".load_data").click(function(){
    const url=`/personel/brief/getInfo?makan=${$("#asset_id").val()}`;
    $.ajax({
      url:url,
      type:'get',
      beforeSend:function(){
        $("#preloader").show();
        $("#main-wrapper").hide();
      },
      success:function(data){

        $("#thead_company").empty();
        $("#thead_company").html(data.header);
        $("#tbody-company").empty();
        $("#tbody-company").html(data.result);
          $("#preloader").hide();
          $("#main-wrapper").show();




      }
    });
});



})(jQuery);
