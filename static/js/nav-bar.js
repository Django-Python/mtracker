// place nav bar on top
// $(function () {
//     $("#nav-placeholder").load("nav-bar.html");
// });

$.get("nav-bar.html", function(data){
    // console.log(data)
    $("#nav-placeholder").replaceWith(data);
});

