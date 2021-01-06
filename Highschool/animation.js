var canvas = document.querySelector('canvas');

var scale_constant = 20;
var fade_num = 30;
var start_colour = [255,0,0];
var end_colour = [00,0,80];
var dot_num = 6;
var spin_radius = parseInt((innerHeight + innerWidth)/(scale_constant)) * (1/10);
var dot_radius = parseInt((innerHeight + innerWidth)/(scale_constant)) * (1/50);

canvas.width = window.innerWidth/scale_constant;
canvas.height = window.innerHeight/scale_constant;

var c = canvas.getContext('2d');

window.addEventListener('resize',
	function(event){
		canvas.width = window.innerWidth/scale_constant;
		canvas.height = window.innerHeight/scale_constant;
		spin_radius = parseInt((innerHeight + innerWidth)/(scale_constant)) * (1/10);
		dot_radius = parseInt((innerHeight + innerWidth)/(scale_constant)) * (1/50);
});

window.addEventListener('scroll',
	function(event){
		angle = ((window.scrollY/125) * (Math.PI/180) * 10);
});

var angle = 0

var fade = [];
for(x=0;x<fade_num;x++){
	fade.unshift(0);
}

function fade_func(a,n){
	return ((a/n)*(a/n));
}

function screen_draw(){
	requestAnimationFrame(screen_draw);
	c.clearRect(0,0,innerWidth/2,innerHeight/2);

	fade.unshift(angle);
	fade.pop();

	for(x=0;x<fade_num;x++){
		var p = fade_func(x,fade_num);
		for(i=0;i<dot_num;i++){
			col = "rgba(" +  
				parseInt(start_colour[0]*p + end_colour[0]*(1-p)) + 
				", " + 
				parseInt(start_colour[1]*p + end_colour[1]*(1-p))  + 
				", " +  
				parseInt(start_colour[2]*p + end_colour[2]*(1-p))  + 
				", " + p + ")";

			c.fillStyle = col;
			c.strokeStyle = col;
			c.beginPath();
			c.arc(innerWidth/(2*scale_constant) + spin_radius*Math.cos(-fade[fade_num - x - 1] + i * (2 * Math.PI/dot_num)),
				 innerHeight/(2*scale_constant) - spin_radius*Math.sin(-fade[fade_num - x - 1] + i * (2 * Math.PI/dot_num)),
				 dot_radius,0,Math.PI * 2,false);
			c.stroke();
			c.fill();
		}
	}
}

screen_draw();