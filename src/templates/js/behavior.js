$( document ).ready(function() {

    positionstop = [
        456,
        343,
        703,
        343,
        243,
        100,
        598,
        600,
        456,
        123,
        738,
        900,
        060,
        600,
        340,
        219,
        987,
        375,
        467,
        700,
        390,
        403,
        900]

    positionsright = [
        150,
        263,
        700,
        657,
        409,
        550,
        345,
        435,
        761,
        367,
        156,
        145,
        573,
        634,
        492,
        235,
        984,
        478,
        298,
        120,
        50,
        276,
        760]

    var counter = 0;

    $("div").each(function(index) {

        $(this).css("position", "absolute");

        $(this).css("right", positionsright[counter]);

        $(this).css("top", positionstop[counter]);

        counter ++;

    })


});