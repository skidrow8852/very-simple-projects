function load_images(){
    enemy_image = new Image;
    enemy_image.src = "assets/v1.png";
    
    player_img = new Image;
    player_img.src = "assets/superhero.png";
    
    gem_image = new Image;
    gem_image.src = "assets/gem.png";
    
    
}

let showPopup = false;

function init(){
    //define the objects that we will have in the game
    canvas = document.getElementById("canvas");
    W = 700;
    H = 400;
    
    canvas.width = W;
    canvas.height = H;
    
    // create a context 
    pen = canvas.getContext('2d');
    game_over = false;
    
    e1 = {
		x : 150,
		y : 50,
		w : 60,
		h : 60,
		speed : 20,
	};
	e2 = {
		x : 300,
		y : 150,
		w : 60,
		h : 60,
		speed : 30,
	};
	e3 = {
		x : 450,
		y : 20,
		w : 60,
		h : 60,
		speed : 40,
	};
    
    enemy = [e1,e2,e3];
    
    player = {
		x : 20,
		y : H/2,
		w : 60,
		h : 60,
		speed : 20,
        moving  : false,
        health : 100,
	};
    
	gem = {
		x : W-100,
		y : H/2,
		w : 60,
		h : 60,
	};
    //listen to events on the canvas
    canvas.addEventListener('mousedown',function(){
        player.moving = true;
    });
    canvas.addEventListener('mouseup',function(){
        player.moving = false;
    });
    
}

function isOverlap(rect1,rect2){
    if (rect1.x < rect2.x + rect2.w &&
   rect1.x + rect1.w > rect2.x &&
   rect1.y < rect2.y + rect2.h &&
   rect1.y + rect1.h > rect2.y) {
    return true
    }
    
    return false;
    
}

function draw(){
    
    //clear the canvas area for the old frame
    pen.clearRect(0,0,W,H);
    
    pen.fillStyle = "red";
    
    //draw the gem
    pen.drawImage(player_img,player.x,player.y,player.w,player.h);
    pen.drawImage(gem_image,gem.x,gem.y,gem.w,gem.h);
    
    
    for(let i=0;i<enemy.length;i++){
        pen.drawImage(enemy_image,enemy[i].x,enemy[i].y,enemy[i].w,enemy[i].h);
    }
    
    pen.fillStyle = "white";
    pen.fillText("Score "+player.health,10,10);
    
}

const popUp = () => {
    let ele = document.getElementById("div");
    ele.style.display = "block"
    let h3 = document.getElementById("score");
    h3.textContent = `Score : ${player.health}`;
}

function tryAgain() {
    let ele = document.getElementById("div");
    ele.style.display = "none";

    // Reset game variables
    game_over = false;
    showPopup = false;

    // Reset player and enemies
    player = {
        x: 20,
        y: H / 2,
        w: 60,
        h: 60,
        speed: 20,
        moving: false,
        health: 100,
    };

    e1 = { x: 150, y: 50, w: 60, h: 60, speed: 20 };
    e2 = { x: 300, y: 150, w: 60, h: 60, speed: 30 };
    e3 = { x: 450, y: 20, w: 60, h: 60, speed: 40 };
    enemy = [e1, e2, e3];

    gem = { x: W - 100, y: H / 2, w: 60, h: 60 };

    // Restart the game loop
    clearInterval(interval);
    interval = setInterval(gameloop, 100);
}


function update(){
    
    //if the player is moving 
    if(player.moving==true){
        player.x += player.speed;
        player.health += 20;
    }
    
    for(let i=0;i<enemy.length;i++){
        if(isOverlap(enemy[i],player)){
            player.health -= 50;
            if(player.health <0){
                game_over = true;
                showPopup = true;
                popUp()
            }
        }
    }
    
   
    
    //overlap overlap
    if(isOverlap(player,gem)){
        
    let ele = document.getElementById("div");
    ele.style.display = "block"
    let h3 = document.getElementById("score");
    h3.textContent = `YOU WON!`;
        game_over = true;
        return;
    }
    
    //move the box downwards
    //update each enemy by same logic
    for(let i=0;i<enemy.length;i++){
        enemy[i].y += enemy[i].speed;
        if(enemy[i].y>H-enemy[i].h || enemy[i].y <0){
            enemy[i].speed *= -1;
        }   
    }
    
}

function gameloop(){
    if(game_over==true){
        clearInterval(interval);
    }
    draw();
    update();
}

load_images();
init();
var interval = setInterval(gameloop,100);