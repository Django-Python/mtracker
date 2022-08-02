// mobile navbar
$(document).ready(function () {
    $('.sidenav').sidenav();
});

// date-time picker 
$(document).ready(function () {
    $('.datepicker').datetimepicker({
        minDate: new Date(),
        format:'m/d/Y, h:i:s A'
    });
});


// task type dropdwn
$(document).ready(function () {
    $('select').formSelect();
});

// disable manual task ntering
$('#task-name').on('change', function() {
    var taskName=$('#task-name').find(":selected").text();
    if(taskName=="Others"){
        $("#task-name-manual").prop('disabled', false);
    }
    else{
        $("#task-name-manual").prop('disabled', true);
    }
});

$('#add_summary_btn').on('click', function() {
    var summary = $('#input-summary').val();
    if(summary!=""){
        $('#task-list').prepend('<li>'+summary+' ('+new Date().toLocaleString()+')</li>');
        $('#input-summary').val('');
    }

})