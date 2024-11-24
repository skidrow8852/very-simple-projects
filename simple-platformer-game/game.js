let config = {
    type: Phaser.AUTO,
    scale: {
        mode: Phaser.Scale.FIT,
        width: 800,
        height: 600
    },
    backgroundColor: 0xffffcc,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: {
                y: 1000,
            },
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update,
    }
}

let game = new Phaser.Game(config);
let playerSpeed = 200;
let playerJumpSpeed = 700;
let score = 0;
let scoreText;

function preload() {
    this.load.image("ground", "assets/topground.png");
    this.load.image("sky", "assets/background.png");
    this.load.image("apple", "assets/apple.png");
    this.load.image("finish", "assets/finish.png");  // Ensure the image is loaded
    this.load.spritesheet("dude", "assets/dude.png", { frameWidth: 32, frameHeight: 48 });
    this.load.image("enemy", "assets/enemy.png");
    this.load.image("ray", "assets/ray.png");
}

function create() {
    W = game.config.width;
    H = game.config.height;

    // Background
    let background = this.add.tileSprite(0, 0, W, H, 'sky');
    background.setOrigin(0, 0);
    background.displayWidth = W * 5;
    background.displayHeight = H;
    background.depth = -2;

    // Create rays on top of the background
    let rays = [];
    for (let i = -10; i <= 10; i++) {
        let ray = this.add.sprite(W / 2, H - 100, 'ray');
        ray.displayHeight = 1.2 * H;
        ray.setOrigin(0.5, 1);
        ray.alpha = 0.2;
        ray.angle = i * 20;
        ray.depth = -1;
        rays.push(ray);

        this.tweens.add({
            targets: rays,
            props: {
                angle: {
                    value: "+=20"
                }
            },
            duration: 8000,
            repeat: -1
        })
    }

    // Ground
    let ground = this.add.tileSprite(0, H - 128, W * 5, 128, 'ground');
    ground.setOrigin(0, 0);

    // Player
    this.player = this.physics.add.sprite(100, 100, 'dude', 4);
    this.player.setBounce(0.5);
    this.player.setCollideWorldBounds(true);
    this.player.body.setGravityY(0);

    // Player animations
    this.anims.create({
        key: 'left',
        frames: this.anims.generateFrameNumbers('dude', { start: 0, end: 3 }),
        frameRate: 10,
        repeat: -1
    });
    this.anims.create({
        key: 'center',
        frames: [{ key: 'dude', frame: 4 }],
        frameRate: 20,
    });
    this.anims.create({
        key: 'right',
        frames: this.anims.generateFrameNumbers('dude', { start: 5, end: 8 }),
        frameRate: 10,
        repeat: -1
    });

    this.cursors = this.input.keyboard.createCursorKeys();

    // Fruits
    let fruits = this.physics.add.group({
        key: 'apple',
        repeat: 10,
        setScale: { x: 0.2, y: 0.2 },
        setXY: { x: 10, y: 0, stepX: 150 }
    });
    fruits.children.iterate(f => f.setBounceY(Phaser.Math.FloatBetween(0.4, 0.7)));

    // Platforms
    let platforms = this.physics.add.staticGroup();
    createPlatforms(platforms);
    platforms.add(ground);

    // Finish Line
    this.finishLine = this.physics.add.sprite(W * 4.5, H - 150, 'finish');
    this.finishLine.setImmovable(true);

    // Enemies
    this.enemies = this.physics.add.group();
    createEnemies(this.enemies, platforms);

    // Colliders
    this.physics.add.collider(platforms, fruits);
    this.physics.add.collider(platforms, this.player);
    this.physics.add.collider(platforms, this.enemies);  // Collider between platforms and enemies
    this.physics.add.overlap(this.player, fruits, eatFruits, null, this);
    this.physics.add.overlap(this.player, this.finishLine, winGame, null, this);
    this.physics.add.collider(this.player, this.enemies, hitEnemy, null, this);

    // Score Display
    scoreText = this.add.text(10, 10, `Score: ${score}`, {
        fontSize: '20px',
        fill: '#000',
        backgroundColor: '#fff',
        padding: { x: 10, y: 5 },
        borderRadius: 5
    }).setScrollFactor(0).setDepth(1);

    // Camera
    this.cameras.main.setBounds(0, 0, W * 5, H);
    this.physics.world.setBounds(0, 0, W * 5, H);
    this.cameras.main.startFollow(this.player, true, true);
    this.cameras.main.setZoom(1.2);

    // After enemies are placed, enable gravity for the player
    this.time.delayedCall(500, () => {
        this.player.body.setGravityY(1000);  // Enable gravity for the player
    });
}

function update() {
    if (this.cursors.left.isDown) {
        this.player.setVelocityX(-playerSpeed);
        this.player.anims.play('left', true);
    } else if (this.cursors.right.isDown) {
        this.player.setVelocityX(playerSpeed);
        this.player.anims.play('right', true);
    } else {
        this.player.setVelocityX(0);
        this.player.anims.play('center');
    }

    if (this.cursors.up.isDown && this.player.body.touching.down) {
        this.player.setVelocityY(-playerJumpSpeed);
    }

    // Constrain enemies to their platform bounds and make them move only on the X axis
    this.enemies.getChildren().forEach(enemy => {
        enemy.setVelocityY(0);  // Ensure enemies only move along the X-axis
    });
}

function eatFruits(player, fruit) {
    fruit.disableBody(true, true);
    score += 10; 
    scoreText.setText(`Score: ${score}`);
}

function winGame(player, finishLine) {
    this.add.text(this.player.x - 100, 200, 'You Win!', {
        fontSize: '32px',
        fill: '#fff'
    });
    this.physics.pause();
    this.player.setTint(0x00ff00);
}

function hitEnemy(player, enemy) {
    this.add.text(250, 200, 'Game Over!', {
        fontSize: '32px',
        fill: '#ff0000'
    });
    this.physics.pause();
    this.player.setTint(0xff0000);

    let tryAgainText = this.add.text(250, 250, 'Press R to Try Again', {
        fontSize: '20px',
        fill: '#fff'
    }).setScrollFactor(0);

    // Restart the game on pressing R
    this.input.keyboard.once('keydown-R', () => {
        this.scene.restart();
        score = 0; // Reset score
    });
}

// Generate platforms dynamically
function createPlatforms(platforms) {
    for (let i = 1; i <= 10; i++) {
        // Place platforms randomly, but make sure they are above the ground
        let platformX = Phaser.Math.Between(200 * i, 200 * i + 100);
        let platformY = Phaser.Math.Between(200, 400);
        platforms.create(platformX, platformY, 'ground').setScale(1, 0.5).refreshBody();
    }
}

// Generate enemies with random velocities and positions
function createEnemies(enemies, platforms) {
    // Iterate through all platforms
    platforms.getChildren().forEach(platform => {
        // Skip the ground platform (assume it has the lowest Y value)
        let xPos = Phaser.Math.Between(100, W - 100);  // Random horizontal position
        let enemy = enemies.create(xPos, -50, 'enemy').setScale(0.1, 0.1).setCollideWorldBounds(true);
        
        // Add gravity so the enemy falls
        enemy.setGravityY(10000);  // Adjust gravity for how fast they fall
        
        // Add a random horizontal velocity
        enemy.setVelocityX(Phaser.Math.Between(-100, 100)); 
        
        // Make the enemy fall down to the platform height
    });
}
