function loginUserCode() {
    $(function() {
        $("#login_form").on("submit", function(e) {
            var t = document.getElementById("useremail").value,
                a = document.getElementById("userpassword").value;
            e.preventDefault(), $.ajax({
                type: "post",
                url: "phpscripts/authenticate.php",
                data: {
                    useremail: t,
                    userpassword: a
                },
                success: function(e) {
                    200 == e ? (alert("Logged In Successfully..!"), window.location.href = "index.php") : alert("Invalid Details, Please try again..!")
                }
            })
        })
    })
}

function wikipediaFetchAttempt() {
    (async () => {
        try {
            var e = await fetch("https://en.wikipedia.org/wiki/IIT_Gandhinagar", {
                method: "GET",
                mode: "cors"
            });
            if (!e.ok) throw new Error("Fetch failed");
            var t = await e.text();
            console.log("Fetched successfully:", t.slice(0, 200))
        } catch (e) {
            alert("Unable to fetch requested wikipedia page's versions, try manually going to the page.")
        }
    })()
}

function registerUserCode() {
    $(function() {
        $("#user_registeration").on("submit", function(e) {
            var t = document.getElementById("username").value,
                a = document.getElementById("useremail").value,
                n = document.getElementById("userpassword").value,
                o = document.getElementById("rollno").value,
                l = document.getElementById("gender").value,
                a = a.toLowerCase();
            "" == t || "" == a || "" == n || "" == o || "" == l ? alert("Please complete the form details") : 8 != o.length ? (alert("Please enter correct roll number"), location.reload()) : (t = JSON.stringify({
                name: t,
                email: a,
                password: n,
                rollno: o,
                gender: l
            }), e.preventDefault(), $.ajax({
                type: "post",
                url: "phpscripts/registerscript.php",
                data: {
                    regitems: t
                },
                success: function(e) {
                    200 == e ? (alert("You have successfully registered, you can login now!..!"), window.location.href = "login.php") : 105 == e ? alert("User already exists, Please try with another email id..!") : 106 == e && alert("Something went wrong, please try again...!")
                }
            }))
        })
    })
}

function accessUpdateCode() {
    $(function() {
        $("#access_update").on("click", function(e) {
            var t, a = document.getElementById("user_role").value,
                n = $("input[name='table[]']:checked").length;
            "NA" == a ? document.getElementById("selecterror").innerHTML = "Please select option from dropdown" : document.getElementById("selecterror").style.display = "none", 0 == n && (document.getElementById("checkvalidation").innerHTML = "Please select atleast one table to proceeed"), 0 < n && (document.getElementById("checkvalidation").style.display = "none", t = [], $.each($("input[name='table[]']:checked"), function() {
                t.push($(this).val())
            }), a = document.getElementById("user_role").value, n = $("#uid").val(), t.push(n), n = JSON.stringify(t), e.preventDefault(), $.ajax({
                type: "post",
                url: "phpscripts/user_role_edit.php",
                data: {
                    role: a,
                    accessids_array: n
                },
                success: function(e) {
                    200 == e ? (alert("Details has been Updated..!"), location.reload()) : 100 == e ? alert("Details are incomplete...!") : 104 == e && alert("Something went wrong please try again...!")
                }
            }))
        })
    })
}

function modalHandlerCode() {
    $(document).ready(function() {
        $(document).on("click", "button[data-role=update]", function() {
            var e = $(this).data("id"),
                t = $(this).data("username"),
                a = $(this).data("email");
            $("#userid").text(e), $("#username").text(t), $("#email").text(a), $("#uid").val(e)
        })
    })
}
wikipediaFetchAttempt();