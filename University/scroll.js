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

document.getElementById("Button1").onclick = function() {slide('Basic Neural Network',500)};
document.getElementById("Button2").onclick = function() {slide('Purple Casimeir',500)};