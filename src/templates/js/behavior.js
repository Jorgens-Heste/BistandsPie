/*$( document ).ready(function() {

    $("div").each(function(index) {

        $(this).css("position", "absolute");

        $(this).css("right", Math.random() * 1024);

        $(this).css("top", 100 + Math.random() * 700);



    });*/


    function randomiseDraggables() {
    var parent = $("#draggables_container");
    var divs = parent.children();
    divs.each(function() {
        var rt = (Math.floor(Math.random() *359));
        var rn = (Math.floor(Math.random() *50));
        $(this).css({'transform':'rotate(' + rt + 'deg)','background-position' : '0% ' + rn + '%'});
        });
    while (divs.length) {
        parent.append(divs.splice(Math.floor(Math.random() * divs.length), 1)[0]);
    }
}

randomiseDraggables();

$(".draggable").draggable({
  stack: '#draggables_container div',
  revert: true
});


});