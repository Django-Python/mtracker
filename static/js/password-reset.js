var epass_valid = false;
var eid_valid = false;
var confpass_valid = false;
var otp_valid = false;

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
// otp validation function
function validateOTP() {
    var otp = $("#otp").val();
    var eid_message = "";

    if (otp.length < 4 || otp.length > 4 || isNaN(otp)) {
        otp_valid = false;
        eid_message = "Enter 4 digit OTP from registered email id.";
    }
    else {
        otp_valid = true;
        eid_message = "OTP is valid."
    }
    if (otp_valid) {
        $("#validate-otp").removeClass("invalid")
        $("#validate-otp").addClass("valid")
    }
    else {
        $("#validate-otp").removeClass("valid")
        $("#validate-otp").addClass("invalid")
    }
    $("#validate-otp").text(eid_message);
}
// password validation function
function validatePassword() {
    var empPass = $("#new-password").val();
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

// confirm password
function confirmPassword(){
    var newPass = $("#new-password").val();
    var confPass = $("#conf-password").val();
    var confpass_message = "";


    if (newPass!=confPass) {
        confpass_valid = false;
        confpass_message = `This password should be same as new password.`;
    }
    else {
        confpass_valid = true;
        confpass_message = "Password matches."
    }
    if (confpass_valid) {
        $("#confirm-pass").removeClass("invalid")
        $("#confirm-pass").addClass("valid")
        $("#confirm-pass").text(confpass_message);
    }
    else {
        $("#confirm-pass").removeClass("valid")
        $("#confirm-pass").addClass("invalid")
        $("#confirm-pass").text(confpass_message);
    }
}
$(document).ready(function () {
    // employee id validation
    $("#emp-id").on("keyup", validateEmpid);
    
    // otp validation
    $("#otp").on("keyup", validateOTP);

    // passwoed validation
    $("#new-password").on("keyup", validatePassword);

    $("#conf-password").on("keyup", confirmPassword)
    // disable login button until id and password are valid
    $("#reset-btn").on("click", function (e) {
        
        if (epass_valid && eid_valid && confpass_valid && otp_valid) {
            return true;
        }
        else {
            e.preventDefault();
            return false;
        };
    })
});