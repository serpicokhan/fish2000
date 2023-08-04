
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
  //$("#modal-company").on("submit", ".js-company-create-form",

  // $("#modal-shekayat").on("click", ".view_shekayat", view_shekayat);
  });
