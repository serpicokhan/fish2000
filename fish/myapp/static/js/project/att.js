$(function(){
    var loadnewdata=function(){
        alert(1);
        var rowdata={
            'hdate':$("#selected_date").val()
        }
        $.ajax({
            url: '/personel/LoadDate/',
            method: 'POST',
            data: JSON.stringify(rowdata),
            contentType: 'application/json',
            success: function (data) {
              if (data.form_is_valid) {
               $("#tbody-company").html();
               $("#tbody-body").html(data.resluts);
              }
              else {
                    toastr.error('لطفا مجدد تلاش فرمایید!');
                // $("#purchaseRequest-table tbody").html(data.html_part_list);
                // $("#modal-purchaseRequest .modal-content").html(data.html_part_form);
              }
            }
          });

    }
    $("#selected_date").change(function(){
        loadnewdata();
    });

var senddata=function(){
                    // Create an empty array to store the data
        var dataArray = [];

        // Iterate through each <tr> element with the class "data-row"
        $('.data-row').each(function() {
            var $tds = $(this).find('td'); // Get all <td> elements in the current <tr>
            var id_=$(this).attr('data-url');
            // Create an object to store the data for this row
            var rowData = {
                title2: $('label[name="titletxt"]', this).attr('data-val'), // Get the value of the "out_time_" input
                id:$(this).attr('data-url'),
                hdate:$('#selected_date').val(),
                name: $tds.eq(0).text(), // Get the content of the first <td>
                number: $tds.eq(1).text(), // Get the content of the second <td>
                absentChecked: $(`input[name="absent_${id_}"]`, this).is(':checked'), // Check the status of the "absent_" checkbox
                estehghaghiChecked: $(`input[name="estehghaghi_${id_}"]`, this).is(':checked'), // Check the status of the "estehghaghi_" checkbox
                estelajiChecked: $(`input[name="estelaji_${id_}"]`, this).is(':checked'), // Check the status of the "estelaji_" checkbox
                inTimeValue: $('input[name="in_time_"]', this).val(), // Get the value of the "in_time_" input
                outTimeValue: $('input[name="out_time_"]', this).val(), // Get the value of the "out_time_" input



            };
            
            // Push the rowData object into the dataArray
            dataArray.push(rowData);
        });

        // Convert the dataArray to a JSON string
        var jsonData = JSON.stringify(dataArray);
        console.log(jsonData);

        // Now you have your data in a JSON format
        $.ajax({
            url: '/personel/SaveInfo/',
            method: 'POST',
            data: JSON.stringify(dataArray),
            contentType: 'application/json',
            success: function (data) {
                if (data.form_is_valid) {
                    //alert("taskGroup created!");  // <-- This is just a placeholder for now for testing
                    toastr.success('دریافت اطلاعات با موفقیت انجام شد');
                    window.location='/Hozur/Success';
                  }
                  else {
                        toastr.error('لطفا مجدد تلاش فرمایید!');
                    // $("#purchaseRequest-table tbody").html(data.html_part_list);
                    // $("#modal-purchaseRequest .modal-content").html(data.html_part_form);
                  }
            }
          });
       

                                
}
$('#btn-send').on('click',senddata);
    $('.row-checkbox').click(function () {
        // Uncheck all checkboxes in the same row
        $(this).closest('tr').find('.row-checkbox').not(this).prop('checked', false);
    });
    $('.normal-example').persianDatepicker({autoClose: true,initialValueType: 'gregorian', format: 'YYYY-MM-DD',
    altField: '#gregorianExampleAlt',
    altFormat: 'LLLL',
    calendar:{
        persian: {
            locale: 'fa'
        }
    },
  

});
    $("#nextBtn").click(function(e) {
        e.preventDefault();
        const selectedDate = $("#selected_date").val();
        if (!selectedDate) {
            alert("Please select a date.");
            return;
        }
        $("#selected_date_display").text(selectedDate);
       
        // Set the in_time and out_time fields to "06:00" and "14:00"
        $("input[name^='in_time_']").val("06:00");
        $("input[name^='out_time_']").val("14:00");
    });
    $("#button2").click(function(e) {
        e.preventDefault();
        const selectedDate = $("#selected_date").val();
        if (!selectedDate) {
            alert("Please select a date.");
            return;
        }
        $("#selected_date_display").text(selectedDate);
       
        // Set the in_time and out_time fields to "06:00" and "14:00"
        $("input[name^='in_time_']").val("14:00");
        $("input[name^='out_time_']").val("22:00");
    });
    $("#button3").click(function(e) {
        e.preventDefault();
        const selectedDate = $("#selected_date").val();
        if (!selectedDate) {
            alert("Please select a date.");
            return;
        }
        $("#selected_date_display").text(selectedDate);
       
        // Set the in_time and out_time fields to "06:00" and "14:00"
        $("input[name^='in_time_']").val("22:00");
        $("input[name^='out_time_']").val("06:00");
    });
    var clicked_element=null;

    $("#attendanceForm").submit(function(e) {
        e.preventDefault();
        // Handle form submission here.
        // You can use AJAX to send the data to the server and then display a confirmation message.
        alert("Attendance submitted successfully!");
        // Optionally, you can reset the form and go back to Part 1.
        // $("#attendanceForm")[0].reset();
        // $("#part2").hide();
        // $("#part1").show();
    });
    $(".js-create-hozur2").click(function(){
        console.log($(this).attr("data-url"));
        return $.ajax({
            url: $(this).attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
      
              $("#modal-company").modal({backdrop: 'static', keyboard: false});
      
            },
            success: function (data) {
      
              $("#modal-company .modal-content").html(data.html_hozur_form);
             
            }
      
          });
       
      });
      $("#tbody-company").on("click",".titletxt",function(){
        clicked_element=$(this).closest('tr').data('url');
        return $.ajax({
          url: $(this).attr("data-url"),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
    
            $("#modal-company").modal({backdrop: 'static', keyboard: false});
    
          },
          success: function (data) {
    
            $("#modal-company .modal-content").html(data.html_hozur_form);
           
          }
    
        });
      });
      $("#modal-company").on("input","#chip-search", function() {
        var searchTerm = $(this).val().toLowerCase();
        
        $(".selectable-chip").each(function() {
          var chipName = $(this).data("chip-name").toString().toLowerCase();
          if (chipName.includes(searchTerm)) {
            $(this).show();
          } else {
            $(this).hide();
          }
        });
      });
      $("#modal-company").on("input","#chip-search-title", function() {
        var searchTerm = $(this).val().toLowerCase();
        
        $(".selectable-chip").each(function() {
          var chipName = $(this).data("chip-name").toString().toLowerCase();
          if (chipName.includes(searchTerm)) {
            $(this).show();
          } else {
            $(this).hide();
          }
        });
      });
      var selectedChip = null;
      var selectedId=null;
      $("#modal-company").on("click",".selectable-chip", function() {
        $('.selectable-chip.active').removeClass('active');
        $(this).toggleClass("active");
        var chipName = $(this).data("chip-name");
        selectedChip=chipName;
        selectedId=$(this).data('id');
        // if ($(this).hasClass("active")) {
        //   selectedChips.push(chipName);
        // } else {
        //   var index = selectedChips.indexOf(chipName);
        //   if (index !== -1) {
        //     selectedChips.splice(index, 1);
        //   }
        // }
      });
      
      $("#modal-company").on('click','.js-add-to-table',function(){

        var datas=selectedChip.split(' ');
        $("#tbody-company").append(`<tr data-url=${selectedId} class="data-row">
        <td> ${datas[1]} ${datas[2]}</td>
        <td>${datas[0]}</td>
        <td><label class="form-control titletxt" data-url="/Hozur/GetTitles/">سرشیفت</label></td>
        <td>
          <div class="custom-control custom-checkbox checkbox-success check-lg mr-3">
          <input type="checkbox" class="custom-control-input row-checkbox" checked name="absent_${selectedId}">
          <label class="custom-control-label" for="absent_${selectedId}"></label>
          </div>
        </td>
        <td>
        <div class="custom-control custom-checkbox checkbox-success check-lg mr-3">
        <input type="checkbox" class="custom-control-input row-checkbox" name="estehghaghi_${selectedId}">
        <label class="custom-control-label" for="estehghaghi_${selectedId}"></label>
        </div>
        </td>
        <td>
        <div class="custom-control custom-checkbox checkbox-success check-lg mr-3">
        <input type="checkbox" class="custom-control-input row-checkbox" name="estelaji_${selectedId}">
        <label class="custom-control-label" for="estelaji_${selectedId}"></label>
        </div>
        </td>
       

        <td><input type="time" name="in_time_" step="60"></td>
        <td><input type="time" name="out_time_" step="60"></td>
    </tr>`);
    $("#modal-company").modal("hide");

      });
      $("#modal-company").on('click','.js-title-to-table',function(){
        console.log(clicked_element);
        var $trToFind = $("tr[data-url='" + clicked_element + "']");
        var $label = $trToFind.find("label.titletxt");
        $label.html(selectedChip.split(' ')[1]);
        $label.attr('data-val',selectedChip.split(' ')[0]);
        
        $("#modal-company").modal("hide");

      });
      $("#modal-company").on("click",'selectable-chip', function() {
        if (selectedChip) {
          selectedChip.removeClass("active");
        }
        
        $(this).addClass("active");
        selectedChip = $(this);

        // Display the selected chip in the "Saved Chip" area
        $("#selected-chip").html('<span class="saved-chip">' + $(this).data("chip-name") + '</span>');
      });
    
    
});