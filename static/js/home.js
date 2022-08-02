// mobile navbar
$(document).ready(function () {
    $('.sidenav').sidenav();
});

// date-time picker 
$(document).ready(function () {
    $('.datepicker').datetimepicker({
        minDate: new Date()
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