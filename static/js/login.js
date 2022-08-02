var epass_valid = false;
var eid_valid = false;

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

// password validation function
function validatePassword() {
    var empPass = $("#emp-pass").val();
    var minNumberofChars = 6;
    var maxNumberofChars = 16;
    var regularExpression = /^(?=.*[\d])(?=.*[!@#$%^&*])[\w!@#$%^&*]{6,16}$/;
    var epass_message = "";

    if (empPass.length < minNumberofChars || empPass.length > maxNumberofChars) {
        epass_valid = false;
        epass_message = `Password length should be ${minNumberofChars} to ${maxNumberofChars} characters only.`;
    }
    else if (!regularExpression.test(empPass)) {
        epass_valid = false;
        epass_message = "Password should contain atleast one number and one special character"
    }
    else {
        epass_valid = true;
        epass_message = "Password is valid."
    }
    if (epass_valid) {
        $("#validate-pass").removeClass("invalid")
        $("#validate-pass").addClass("valid")
        $("#validate-pass").text(epass_message);
    }
    else {
        $("#validate-pass").removeClass("valid")
        $("#validate-pass").addClass("invalid")
        $("#validate-pass").text(epass_message);
    }

}
$(document).ready(function () {
    // employee id validation
    $("#emp-id").on("keyup", validateEmpid);

    // passwoed validation
    $("#emp-pass").on("keyup", validatePassword);

    // disable login button until id and password are valid
    $("#login-btn").on("click", function (e) {
        
        if (epass_valid && eid_valid) {
            return true;
        }
        else {
            e.preventDefault();
            return false;
        };
    })
});