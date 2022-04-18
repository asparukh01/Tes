$(document).ready(function() {
    $("#register").click(function (event) {
        $.post(`http://127.0.0.1:8000/api_v1/auth/users/`,
            {
                username: $('#username').val(),
                first_name: $('#first_name').val(),
                last_name: $('#last_name').val(),
                email: $('#email').val(),
                password: $('#password').val(),
                telephone: $('#telephone').val()
            });
    });
});