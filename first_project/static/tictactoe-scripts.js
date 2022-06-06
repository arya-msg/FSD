/* Code done by Arya M*/
var clickCount = 0
var doubleClickCount = 0
var clickedCell = ""
var clickedValue = ""


function onClickFn() {

    clickCount = clickCount + 1;
    document.getElementById("alerts").innerHTML = "";
    clickedCell = event.target.id;
    clickedValue = document.getElementById(clickedCell).value;

    if (clickedValue == "X" || clickedValue == "O") {


        alert("The cell is not empty")


        clickCount = clickCount - 1;

    } else {
        if (clickCount % 2 == 0) {
            document.getElementById(clickedCell).value = "O";
        } else {
            document.getElementById(clickedCell).value = "X";
        }
        clickedValue = document.getElementById(clickedCell).value;
    }
    doubleClickCount = 0;

}


function onDoubleClickFn() {

    document.getElementById("alerts").innerHTML = "";
    clickedCell = event.target.id;
    clickedValue = document.getElementById(clickedCell).value;

    if (doubleClickCount == 1 && clickCount > 0) {
        document.getElementById("alerts").innerHTML = "Further undoing is no permitted. Sorry :(";
    } else {
        doubleClickCount = 1
        document.getElementById(clickedCell).value = "";
        if (clickedValue == "X") {
            clickedValue = "O"
        } else {
            clickedValue = "X"
        }
        clickCount = clickCount - 1
    }

}

function resetFn() {
    document.getElementById("alerts").innerHTML = "";
    clickCount = 0
    doubleClickCount = 0
    clickedCell = ""
    clickedValue = ""
    document.getElementById("cell_11").value = "";
    document.getElementById("cell_12").value = "";
    document.getElementById("cell_13").value = "";
    document.getElementById("cell_21").value = "";
    document.getElementById("cell_22").value = "";
    document.getElementById("cell_23").value = "";
    document.getElementById("cell_31").value = "";
    document.getElementById("cell_32").value = "";
    document.getElementById("cell_33").value = "";

}

function checkResultFn() {

    document.getElementById("alerts").innerHTML = "";
    var val_11 = document.getElementById("cell_11").value;
    var val_12 = document.getElementById("cell_12").value;
    var val_13 = document.getElementById("cell_13").value;
    var val_21 = document.getElementById("cell_21").value;
    var val_22 = document.getElementById("cell_22").value;
    var val_23 = document.getElementById("cell_23").value;
    var val_31 = document.getElementById("cell_31").value;
    var val_32 = document.getElementById("cell_32").value;
    var val_33 = document.getElementById("cell_33").value;
    if (clickedCell == "cell_11") {
        if ((clickedValue == val_11 && clickedValue == val_12 && clickedValue == val_13) ||
            (clickedValue == val_11 && clickedValue == val_21 && clickedValue == val_31) ||
            (clickedValue == val_11 && clickedValue == val_22 && clickedValue == val_33)) {

            if (clickedValue == "X") {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 1 Won The Game. Congrats... :)";
            } else {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 2 Won The Game. Congrats... :)";
            }
        }

    } else if (clickedCell == "cell_12") {
        if ((clickedValue == val_11 && clickedValue == val_12 && clickedValue == val_13) ||
            (clickedValue == val_12 && clickedValue == val_22 && clickedValue == val_32)) {

            if (clickedValue == "X") {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 1 Won The Game. Congrats... :)";
            } else {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 2 Won The Game. Congrats... :)";
            }
        }
    } else if (clickedCell == "cell_13") {
        if ((clickedValue == val_11 && clickedValue == val_12 && clickedValue == val_13) ||
            (clickedValue == val_13 && clickedValue == val_23 && clickedValue == val_33) ||
            (clickedValue == val_13 && clickedValue == val_22 && clickedValue == val_31)) {

            if (clickedValue == "X") {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 1 Won The Game. Congrats... :)";
            } else {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 2 Won The Game. Congrats... :)";
            }
        }
    } else if (clickedCell == "cell_21") {
        if ((clickedValue == val_11 && clickedValue == val_21 && clickedValue == val_31) ||
            (clickedValue == val_12 && clickedValue == val_22 && clickedValue == val_23)) {

            if (clickedValue == "X") {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 1 Won The Game. Congrats... :)";
            } else {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 2 Won The Game. Congrats... :)";
            }
        }
    } else if (clickedCell == "cell_22") {

        if ((clickedValue == val_11 && clickedValue == val_22 && clickedValue == val_33) ||
            (clickedValue == val_13 && clickedValue == val_22 && clickedValue == val_31) ||
            (clickedValue == val_12 && clickedValue == val_22 && clickedValue == val_32) ||
            (clickedValue == val_21 && clickedValue == val_22 && clickedValue == val_23)) {

            if (clickedValue == "X") {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 1 Won The Game. Congrats... :)";
            } else {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 2 Won The Game. Congrats... :)";
            }
        }

    } else if (clickedCell == "cell_23") {
        if ((clickedValue == val_13 && clickedValue == val_23 && clickedValue == val_33) ||
            (clickedValue == val_21 && clickedValue == val_22 && clickedValue == val_23)) {

            if (clickedValue == "X") {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 1 Won The Game. Congrats... :)";
            } else {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 2 Won The Game. Congrats... :)";
            }
        }
    } else if (clickedCell == "cell_31") {

        if ((clickedValue == val_11 && clickedValue == val_21 && clickedValue == val_31) ||
            (clickedValue == val_31 && clickedValue == val_22 && clickedValue == val_13) ||
            (clickedValue == val_31 && clickedValue == val_32 && clickedValue == val_33)) {

            if (clickedValue == "X") {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 1 Won The Game. Congrats... :)";
            } else {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 2 Won The Game. Congrats... :)";
            }
        }
    } else if (clickedCell == "cell_32") {
        if ((clickedValue == val_12 && clickedValue == val_22 && clickedValue == val_32) ||
            (clickedValue == val_31 && clickedValue == val_32 && clickedValue == val_33)) {

            if (clickedValue == "X") {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 1 Won The Game. Congrats... :)";
            } else {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 2 Won The Game. Congrats... :)";
            }
        }
    } else if (clickedCell == "cell_33") {

        if ((clickedValue == val_13 && clickedValue == val_23 && clickedValue == val_33) ||
            (clickedValue == val_11 && clickedValue == val_22 && clickedValue == val_33) ||
            (clickedValue == val_31 && clickedValue == val_32 && clickedValue == val_33)) {

            if (clickedValue == "X") {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 1 Won The Game. Congrats... :)";
            } else {
                document.getElementById("alerts").innerHTML = "Hurray!!! Player 2 Won The Game. Congrats... :)";
            }
        }
    }
    if (clickCount == 9) {

        document.getElementById("alerts").innerHTML = "It is a Tie :( Better luck next time .";
    }
}
