$( document ).ready(function() {



    var newpositions = [
    {right: 1300, top: 700},
    {right: 400, top: 800},
    {right: 1000, top: 500},
    {right: 400, top: 200},
    {right: 500, top: 1050},
    {right: 1075, top: 700},
    {right: 500, top: 450},
    {right: 100, top: 800},
    {right: 150, top: 500},
    {right: 1000, top: 950},
    {right: 1350, top: 900},
    {right: 750, top: 300},
    {right: 1350, top: 200},
    {right: 700, top: 600},
    {right: 1025, top: 250},
    {right: 150, top: 175},
    {right: 0, top: 0},
    {right: 0, top: 0},
    {right: 0, top: 0},
    {right: 0, top: 0},
    {right: 0, top: 0},
    {right: 0, top: 0},
    {right: 0, top: 0},
    {right: 0, top: 0},
    {right: 0, top: 0},
    {right: 0, top: 0}]

    var counter = 0;

    $(".green, .red, .blue, .question").each(function(index) {

        $(this).css("position", "absolute");


        verticalposition = newpositions[counter]["top"];
        horisontalposition = newpositions[counter]["right"];

        $(this).css("top", verticalposition);
        $(this).css("right", horisontalposition);

        counter ++;

    }
    );

});

