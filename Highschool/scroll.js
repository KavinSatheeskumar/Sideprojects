function slide(elemID, delay){
	var yEnd = document.getElementById(elemID).getBoundingClientRect().y;
	for(let x=0;x<delay;x++){
		setTimeout(
			function(){
				window.scrollBy(0,yEnd/delay);
			}
			,x
		)
	}
}

document.getElementById("Button1").onclick = function() {slide('Electron Levels',500)};
document.getElementById("Button2").onclick = function() {slide('A Weird Map on the Complex Plane',500)};
document.getElementById("Button3").onclick = function() {slide('Charges in a box',500)};
document.getElementById("Button4").onclick = function() {slide('Dragon Curve',500)};
document.getElementById("Button5").onclick = function() {slide('Complex Functions',500)};
document.getElementById("Button6").onclick = function() {slide('Terria',500)};