windowwidth = window.innerWidth || document.body.clientWidth || document.documentElement.clientWidth;
if (windowwidth < 400 && windowwidth > 299) {setDim300();}
function setDim300() {
    var imagecontainer = document.getElementsByClassName("image-container");
    var links = document.getElementById("links");
    var instruction = document.getElementById("instruction");
    var welcometext = document.getElementById("welcometext");
    var checkallb = document.getElementById("checkall");
    var button = document.getElementById("button");
    var leftdiv = document.getElementsByClassName("leftdiv");
    var rightdiv = document.getElementsByClassName("rightdiv");
    var bottomdiv = document.getElementsByClassName("bottomdiv");
    leftdiv[0].style.left = "14.3%";
    leftdiv[0].style.border = "1.5px solid rgba(0, 0, 139, 0.61)"
    rightdiv[0].style.left = "31.3%";
    rightdiv[0].style.border = "1.5px solid rgba(0, 0, 139, 0.61)";
    imagecontainer[0].style.height = "90px";
    links.style.fontSize = "12px";
    links.style.borderRadius = "10px";
    links.style.border = "1px solid blue";
    links.style.padding = "5px";
    links.style.overflowX = "auto";
    instruction.style.fontSize = "12px";
    welcometext.style.fontSize = "17px";
    checkallb.style.padding = "5px";
    checkallb.style.borderRadius = "5px";
    checkallb.style.fontSize = "12px";
    checkallb.style.width = "60%";
    button.style.padding = "10px";
    button.style.borderRadius = "5px";
    button.style.fontSize = "14px";
    button.style.width = "70%";
}
circlepos = document.getElementsByClassName("circle");
setInterval(moves, 3000);
function moves() {
    var pos = 0;
    for (var h = 0; h < circlepos.length; h++) {
        circlepos[h].style.top = "56.4%";
        circlepos[h].style.left = "24.5%";
    }
    var moveInterval = setInterval(movecircles, 5);
    document.getElementsByClassName("leftdiv")[0].style.display = "none";
    document.getElementsByClassName("rightdiv")[0].style.display = "none";
    document.getElementsByClassName("bottomdiv")[0].style.display = "block";
    function movecircles() {
        if (pos == 313) {
            move2();
            clearInterval(moveInterval);
        } else {
            pos += 1;
            if (pos == 46) {
                document.getElementsByClassName("bottomdiv")[0].style.display = "none";
                for (var l=0; l < circlepos.length; l++) {circlepos[l].style.top = "39.2%";}    
            }
            for (var i=0; i < circlepos.length; i++) {
                var finalpos = ((((circlepos[i].style.top).replace("%","")/1)*10) - (0.1*10))/10;
                circlepos[i].style.top = finalpos + "%";
            }
        }
    }
}
function move2() {
    var pos2 = 0;
    var moveInterval2 = setInterval(movecircles2, 10);
    function movecircles2() {
        if (pos2 == 52) {
            clearInterval(moveInterval2);
        } else {
            pos2 += 1;
            if (pos2 == 37) {
                document.getElementsByClassName("leftdiv")[0].style.display = "block";
                document.getElementsByClassName("rightdiv")[0].style.display = "block";
                for (n = 0; n < circlepos.length; n++) {
                    if (n == 0) {circlepos[n].style.left = "31.6%"}
                    else {circlepos[n].style.left = "17.0%"}
                }
            }
            for (var j=0; j < circlepos.length; j++) {
                if (j == 0) {
                    var finalpos2 = ((((circlepos[j].style.left).replace("%","")/1)*10) + (0.1*10))/10;
                    circlepos[j].style.left = finalpos2 + "%";
                } else {
                    var finalpos2 = ((((circlepos[j].style.left).replace("%","")/1)*10) - (0.1*10))/10;
                    circlepos[j].style.left = finalpos2 + "%";
                }
            }
        }
    }
}