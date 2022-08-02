
// date-time picker 
$(document).ready(function () {
    $('.datepicker').datetimepicker({
        minDate: new Date(),
        format: 'm/d/Y, h:i:s A'
    });
});


// task type dropdwn
$(document).ready(function () {
    $('select').formSelect();
});

// disable manual task entering
$('#task-name').on('change', function () {
    var taskName = $('#task-name').find(":selected").text();
    if (taskName == "Others") {
        $("#task-name-manual").prop('disabled', false);
    }
    else {
        $("#task-name-manual").prop('disabled', true);
    }
});

$('#add_summary_btn').on('click', function () {
    var summary = $('#input-summary').val();
    if (summary != "") {
        $('#task-list').prepend('<li>' + summary + ' (' + new Date().toLocaleString() + ')</li>');
        $('#input-summary').val('');
    }

})


// validation
var eid_valid = false;
var ename_valid = false;
var email_valid = false;

function validateEmpName(){
    var empName = $("#emp-name").val();
    var nameRegex = /^[a-zA-Z\s.]+$/;
    var ename_message = "";

    if(!nameRegex.test(empName)) {
        ename_valid = false;
        ename_message = "Please enter alphabets only.";
    }
    else {
        ename_valid = true;
        ename_message = "Employee Name is valid."
    }
    if (ename_valid) {
        $("#validate-name").removeClass("invalid")
        $("#validate-name").addClass("valid")
    }
    else {
        $("#validate-name").removeClass("valid")
        $("#validate-name").addClass("invalid")
    }
    $("#validate-name").text(ename_message);
}
function validateEmpEmail(){
    var email = $("#emp-email").val();
    var email_regex = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var email_message = "";

    if (!email_regex.test(email)) {
        email_valid = false;
        email_message = "Please enter valid email id.";
    }
    else {
        email_valid = true;
        email_message = "Email id is valid."
    }
    if (email_valid) {
        $("#validate-email").removeClass("invalid")
        $("#validate-email").addClass("valid")
    }
    else {
        $("#validate-email").removeClass("valid")
        $("#validate-email").addClass("invalid")
    }
    $("#validate-email").text(email_message);
}

// employee id validation function
function validateEmpid() {
    var empId = $("#emp-id").val();
    var eid_message = "";

    if (empId.length < 6 || empId.length > 6 || isNaN(empId)) {
        eid_valid = false;
        eid_message = "Please enter 6 digit employee id number.";
    }
    else {
        eid_valid = true;
        eid_message = "Employee id is valid."
    }
    if (eid_valid) {
        $("#validate-eid").removeClass("invalid")
        $("#validate-eid").addClass("valid")
    }
    else {
        $("#validate-eid").removeClass("valid")
        $("#validate-eid").addClass("invalid")
    }
    $("#validate-eid").text(eid_message);
}
$(document).ready(function () {
    // employee id validation
    $("#emp-id").on("keyup", validateEmpid);

    // employee name validation
    $("#emp-name").on("keyup", validateEmpName);

    // email validation 
    $("#emp-email").on("keyup", validateEmpEmail);

    // disable login button until id and password are valid
    $("#task-submit-btn").on("click", function (e) {

        if (eid_valid && email_valid && ename_valid) {
            return true;
        }
        else {
            e.preventDefault();
            return false;
        };
    })
});