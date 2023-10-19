
$(function () {

    $('#main_search').keyup(function(e){
      Search($('#main_search').val());
    });
    var Search =function (search) {

      return $.ajax({
        url: "/Fish/Search/?q="+search,
        type: 'get',
        dataType: 'json',
        beforeSend: function () {

        },
        success: function (data) {
            console.log(data);
            $("#orders").html(data.result);



        }
      });
    }
    $(".btn_personle_search").click(function(e){
      // alert($("#asset_id").val());
      const text=$("#personel_search").val();
      const asset=$("#asset_id").val();
      const manager=$("#manager_id").val();
      // if(manager === 'سرشیفت'){
      //   toastr.error("سر شیفت را مشخص کنید");
      // }
      // else{
      // alert(asset);
      window.location=`/personel/Search/?q=${text}&manager=${manager}&asset=${asset}`;
      // }
      return false;
    });
    var view_shekayat =function (search) {
      btn=$(this);
      return $.ajax({
        url:btn.attr("data_url") ,
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-shekayat .modal-content").html('');
          $("#modal-shekayat").modal({backdrop: 'static', keyboard: false});

        },
        success: function (data) {
            $("#modal-shekayat .modal-content").html(data.html_wo_form);



        }
      });



  };

  $("#table-company").on("click",'.js-profile-delete',function(){
    // sweetAlert("Oops...", "Something went wrong !!", "error") ;
    // swal({ title: "Are you sure dsadas delete ?", text: "You will not be able to recover this imaginary file !!", type: "warning", 
    // showCancelButton: !0, confirmButtonColor: "#DD6B55", confirmButtonText: "Yes, delete it !!", cancelButtonText: "No, cancel it !!",
    //  closeOnConfirm: !1, closeOnCancel: !1 }, 
    //  function (e) { e ? swal("Deleted !!", "Hey, your imaginary file has been deleted !!", "success") : 
    // swal("Cancelled !!", "Hey, your imaginary file is safe !!", "error") });
    
    a=confirm("حدف شود؟");
    if(a){
      // console.log($(this).closest('tr'));
      var url=$(this).attr('data-url');
      var row=$(this).closest('tr');
      $.ajax({
        url:url,
        type:'post',
        success:function(data){
          if(data.valid){
          swal({
            title: "تبدیل به EM",
            text:"",
            type: "info",
            
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "حذف شد",
           
          });
          row.remove();
        }

        }
      });
      
    }
  });
  
$("#asset_id").click(function(){
  alert(123);
  $.ajax({
    url:`personel/GetMamnager?q=${$(this).val()}`,
    success:function(){
      $('#manager_id').html('');
      $('#manager_id').html(data.result);


    }
  });
});
  // $("#modal-shekayat").on("click", ".view_shekayat", view_shekayat);
  });
