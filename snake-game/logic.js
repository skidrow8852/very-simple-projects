let canvas = document.getElementById("canvas");
let pen = canvas.getContext('2d');
let w = 800;
let h = 800;
let rect = {
        x : 20,y : 20, w : 30, h : 30, speed : 10
    }
let game_over = false;
let cell_size = 30;
let showPopup = false;
let score = 0;
let food = getRandomFood();
let food_image = new Image();
food_image.src = 'assets/apple.png';
let snake = {
        init_len:5,
        color:'red',
        cells : [],
        direction: 'right',
        
        createSnake : function() {
            for(var i = this.init_len; i>0;i--){
                this.cells.push({x : i, y : 0})
            }
        },
        drawSnake : function() {
            for(var i = 0; i < this.cells.length;i++){
                pen.fillStyle = "blue"
                pen.fillRect(this.cells[i].x*cell_size, this.cells[i].y*cell_size,cell_size - 1,cell_size - 1)
            }
           
        },

        updateSnake : function(){
            let headX = this.cells[0].x;
            let headY = this.cells[0].y;

            if(headX == food.x && headY == food.y){
                food = getRandomFood();
                score++;

            }else{
                this.cells.pop();
            }
            
          
            let nextX;
            let nextY;
            if(this.direction == 'right'){
                nextX = headX + 1;
                nextY = headY;
              
            }

            else if(this.direction == 'left'){
                nextX = headX - 1;
                nextY = headY;
                
            }

            else if(this.direction == 'down'){
                nextX = headX;
                nextY = headY + 1;
                
            }
            else {
                nextX = headX;
                nextY = headY - 1;
                
            }
              this.cells.unshift({x : nextX,y : nextY})
                if(nextX * cell_size > w - cell_size || nextX * cell_size - cell_size < 0 || nextY * cell_size + cell_size > h || nextY * cell_size < 0) {
                    game_over = true;
                }
                }
    }

function init () {
    // draw a graphic on the canvas
    snake.createSnake()
     document.addEventListener('keydown', function(e) {
            code =  e.key ;

 
        if(code == 'ArrowUp') 
           snake.direction = 'up'
        else if(code == 'ArrowDown')
            snake.direction = 'down'
         else if(code ==  'ArrowLeft')
            snake.direction = 'left'
        else
            snake.direction = 'right'
       
         });

}

function draw(){
    pen.clearRect(0,0,w,h)
    snake.drawSnake();
    pen.fillStyle = "red"
    pen.drawImage(food_image,food.x*cell_size,food.y*cell_size,cell_size,cell_size);

}


function getRandomFood(){
    let foodX = Math.round(Math.random()*(w-cell_size) / cell_size);
    let foodY = Math.round(Math.random()*(h-cell_size) / cell_size);

    let food = {
        x : foodX,
        y : foodY,
        color : "red"
    }

    return food;
}

function update(){
    snake.updateSnake();
}

const popUp = () => {
let ele = document.getElementById("div");
ele.style.display = "block"
let h3 = document.getElementById("score");
h3.textContent = `Score : ${score}`;
}

const tryAgain = () => {
    let ele = document.getElementById("div");
    ele.style.display = "none";

    // Reset game variables
    game_over = false;
    score = 0;
    showPopup = false;

    // Reinitialize snake and food
    snake.cells = [];
    snake.direction = 'right';
    snake.createSnake();
    food = getRandomFood();

    // Restart the game loop
    clearInterval(interval);
    interval = setInterval(gameLoop, 100);
};


function gameLoop(){
    if(game_over){
        clearInterval(interval)
        showPopup = true;
    }

    if(showPopup){
        popUp()
    }
    draw();
    update();
    
}

init();
let interval = setInterval(gameLoop,100)


