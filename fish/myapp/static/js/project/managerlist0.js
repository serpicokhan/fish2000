(function($) {
  function printDiv(divId) {
  const divElement = $(`#${divId}`);
  if (divElement.length > 0) {
    const newWindow = window.open();
    newWindow.document.write(`<html lang="fa"><head><title>چاپ</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="keywords" content="" />
   <meta name="author" content="" />
   <meta name="robots" content="" />
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <meta name="description" content="پنل مدیریتی - داشبورد 1" />
   <meta property="og:title" content="پنل مدیریتی - داشبورد 1" />
   <meta property="og:description" content="پنل مدیریتی - داشبورد 1" />
   <meta property="og:image"  />
   <meta name="format-detection" content="telephone=no">
   <title>پنل مدیریتی - داشبورد 1</title>
   <!-- Favicon icon -->
   <link rel="icon" type="image/png" sizes="16x16" href="/static/images/favicon.png">
      <link rel="icon" type="image/png" sizes="16x16" href="/static/images/favicon.png">
    <link href="/static/vendor/jqvmap/css/jqvmap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="/static/vendor/chartist/css/chartist.min.css">
    <!-- Vectormap -->
    <link href="/static/vendor/jqvmap/css/jqvmap.min.css" rel="stylesheet">
    <link href="/static/vendor/bootstrap-select/dist/css/bootstrap-select.min.css" rel="stylesheet">
    <link href="/static/vendor/owl-carousel/owl.carousel.css" rel="stylesheet">
    <link href="/static/vendor/fullcalendar/css/fullcalendar.min.css" rel="stylesheet" type="text/css"/>
    <link href="/static/2.0/lineicons.css" rel="stylesheet">
    <link href="/static/css/style.css" rel="stylesheet">
    <link href="/static/vendor/dropzone/dist/dropzone.css" rel="stylesheet" type="text/css"/>
    <script src="/static/js/jquery-2.1.1.js"></script>

     <link href="/static/vendor/persianDatepicker/persianDatepicker.css" rel="stylesheet" type="text/css"/>
    <link href="/static/vendor/Persian-DateRangePicker-master/daterangepicker.css" rel="stylesheet" type="text/css"/>
    <link href="/static/vendor/Persian-DateRangePicker-master/datepicker-theme.css" rel="stylesheet" type="text/css"/>
    <link href="/static/vendor/JalaliDatePicker-main/jalalidatepicker.css" rel="stylesheet" type="text/css"/>
    <link href="/static/vendor/sweetalert2/dist/sweetalert2.min.css" rel="stylesheet" type="text/css"/>



<link href="/static/vendor/sweetalert2/dist/sweetalert2.min.css" rel="stylesheet" type="text/css"/>
<link href="/static/vendor/toastr/css/toastr.min.css" rel="stylesheet" type="text/css"/>
<link rel="stylesheet" href="/static/css/persian-datepicker.css">
      </head><body style='direction: rtl;'>`);

    const divClone = divElement.clone();
    newWindow.document.write(divClone.wrap('<div/>').parent().html());

    newWindow.document.write('</body></html>');
    newWindow.print();
  }
}
$("#printbtn").click(function(){
  printDiv('datarow');
});
  $(".load_data").click(function(){
    const url=`/personel/brief/getInfo/All?date=${$("#datepicker-default").val().replaceAll('/','-')}`;
    $.ajax({
      url:url,
      type:'get',
      beforeSend:function(){
        $("#preloader").show();
        $("#main-wrapper").hide();
      },
      success:function(data){

        // $("#thead_company").empty();
        // $("#thead_company").html(data.header);

        $("#datarow").empty();
        var str="";
        for(var i in data){
          console.log(data[i].result);
          str+=data[i].result;
        }
        $("#datarow").html(str);

        // $("#tbody-company").html(data.result);

        $("#preloader").hide();
        $("#main-wrapper").show();




      }
    });
});



})(jQuery);
