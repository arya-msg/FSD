var total = 6
var count = 0
var row = 1
var exp_word_list = ["APPLE", "HAPPY", "EARTH", "AGILE" , "FOCUS", "DREAM"]
var lett_1 = "";
var lett_2 = "";
var lett_3 = "";
var lett_4 = "";
var lett_5 = "";
var letters = /^[A-Za-z]+$/;
var act_word = ""

$(document).ready(function() {
    var randInt = Math.floor(Math.random() * (5- 0 + 1)) + 0;

    var exp_word = exp_word_list[randInt];
    exp_word = exp_word.toUpperCase();
    var exp_word_arry = [exp_word.charAt(0).toUpperCase(), exp_word.charAt(1).toUpperCase(),
        exp_word.charAt(2).toUpperCase(), exp_word.charAt(3).toUpperCase(), exp_word.charAt(4).toUpperCase()
    ];
    $("#trl_cnt").val("6/6");
    $(".row2").prop('disabled', true);
    $(".row3").prop('disabled', true);
    $(".row4").prop('disabled', true);
    $(".row5").prop('disabled', true);
    $(".row6").prop('disabled', true);
    $(".row6").prop('disabled', true);


    $(".button").click(function() {

        lett_1 = $("#cell_" + row + "1").val().toUpperCase();
        lett_2 = $("#cell_" + row + "2").val().toUpperCase();
        lett_3 = $("#cell_" + row + "3").val().toUpperCase();
        lett_4 = $("#cell_" + row + "4").val().toUpperCase();
        lett_5 = $("#cell_" + row + "5").val().toUpperCase();

        if (!lett_1.match(letters)) {
            alert(lett_1 + " is not an english letter.");
        } else if (!lett_2.match(letters)) {
            alert(lett_2 + " is not an english letter.");
        } else if (!lett_3.match(letters)) {
            alert(lett_3 + " is not an english letter.");
        } else if (!lett_4.match(letters)) {
            alert(lett_4 + " is not an english letter.");
        } else if (!lett_5.match(letters)) {
            alert(lett_5 + " is not an english letter.");
        } else {
            act_word_array = [lett_1, lett_2, lett_3, lett_4, lett_5];
            act_word = lett_1 + lett_2 + lett_3 + lett_4 + lett_5;
            $("#trials").text("Attempts Remaining: "+String( 6-row) + "/6");
            $(".row"+row).prop('disabled', true);
            if (act_word == exp_word) {
                for (var i = 0; i < 5; i++) {
                   var cell = String(i + 1);
                    $("#cell_" + row + cell).css("background-color", "green");
                    $("#cell_" + row + cell).css("color", "white");
                }
                $("#alerts").text("Hurray!!! You Won The Game In " + row + " Attempts. Congrats.. :)");
                $(".button").prop('disabled', true);
            } else {
                for (var i = 0; i < 5; i++) {
                    if (act_word_array[i] == exp_word_arry[i]) {
                       var cell = String(i + 1);
                        $("#cell_" + row + cell).css("background-color", "green");
                        $("#cell_" + row + cell).css("color", "white");
                    } else {
                        var isFound = false;
                        for (var j = 0; j < 5; j++) {
                            if (act_word_array[i] == exp_word_arry[j]) {
                                isFound = true;
                            }
                        }
                        if (isFound) {
                            var cell = String(i + 1);
                            $("#cell_" + row + cell).css("background-color", "olive");
                            $("#cell_" + row + cell).css("color", "white");
                        } else {
                            var cell = String(i + 1);
                            $("#cell_" + row + cell).css("background-color", "black");
                            $("#cell_" + row + cell).css("color", "white");
                        }

                    }


                }
                row = row + 1;
                $(".row" + row).prop('disabled', false);
            }
        }

    });
});
