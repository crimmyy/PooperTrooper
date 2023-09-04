''' 
Citations:
    https://weblog.jamisbuck.org/2011/2/3/maze-generation-sidewinder-algorithm
    https://www.baeldung.com/cs/maze-generation
    https://academy.cs.cmu.edu/docs
    https://www.tutorialsteacher.com/python/math-module
    https://www.w3schools.com/python/ref_math_radians.asp
    https://www.geeksforgeeks.org/python-math-cos-function/#
    https://www.w3schools.com/python/ref_math_sin.asp
    https://www.w3schools.com/python/ref_math_atan2.asp 
    https://www.pngitem.com/middle/hbRoJJm_transparent-
        turd-png-super-poop-transparent-png-download/ 
    https://www.pinterest.com/pin/38773246782173497/
    https://www.reddit.com/r/BattleForDreamIsland/
    comments/l5qwcr/pee_drop_the_recolor_poll_winner/ 
    https://www.vecteezy.com/vector-art/11674685-
        brain-seamless-pattern-texture-anatomy-background 
    https://www.instagram.com/p/CV2tuUQoZLH/ 
    https://www.pinterest.com/pin/99008891799499613/
    https://www.pinterest.com/pin/429601251957737534/ 
    https://www.fontspace.com/witcher-knight-font-f83741
    https://www.pinterest.com/pin/63261569759219585/
    https://www.pngwing.com/en/free-png-bmvwj
    https://www.pngwing.com/en/free-png-bksnh/download
    https://www.pinterest.com/pin/15270086234254872/
    https://www.pinterest.com/pin/688839705518506531/
    https://www.pinterest.com/pin/168251736073093319/
    https://www.pinterest.com/pin/44684221294142926/
    https://www.pngwing.com/en/free-png-maupqspeech 

'''
from cmu_graphics import *
import random
import math
import copy
from PIL import Image

def onAppStart(app):
    #initialize world
    app.onStepCounter = 0
    app.gameOverBool = False
    app.setMaxShapeCount(100000)
    app.currScore = 0
    app.highscore = 0
    app.gameStart = False
    app.gameInstructions = False
    #load images
    app.imageList = [Image.open("images/poop.png"), 
                    Image.open("images/intestine.jpeg"), 
                    Image.open("images/wiz1.png"), 
                    Image.open("images/bathroom.jpg"),
                    Image.open('images/crazy.png'),
                    Image.open('images/fireball.png'),
                    Image.open('images/following.png'),
                    Image.open('images/pee.png'),
                    Image.open('images/powerhealth.png'),
                    Image.open('images/powerspeed.png'),
                    Image.open('images/health.png'),
                    Image.open('images/emptyHealth.png'),
                    Image.open('images/score.png'),
                    Image.open('images/gameStart.png'),
                    Image.open('images/gameOver.png'),
                    Image.open('images/instructions.png')]
    
    app.image = app.imageList[0]
    app.image2 = app.imageList[1]
    app.imageWiz = app.imageList[2]
    app.imageBathroom = app.imageList[3]
    app.crazy = app.imageList[4]
    app.fireball = app.imageList[5]
    app.following = app.imageList[6]
    app.pee = app.imageList[7]
    app.powerHealth = app.imageList[8]
    app.powerSpeed = app.imageList[9]
    app.imageHealth = app.imageList[10]
    app.imageEmptyHealth = app.imageList[11]
    app.imageScore = app.imageList[12]
    app.imageGameStart = app.imageList[13]
    app.imageGameOver = app.imageList[14]
    app.instructions = app.imageList[15]

    app.imageWidth, app.imageHeight = (app.image.width, 
                                       app.image.height)
    app.image2Width, app.image2Height = (app.image2.width, 
                                         app.image2.height)
    app.imageWizWidth, app.imageWizHeight = (app.imageWiz.width, 
                                             app.imageWiz.height)
    app.imageBathroomWidth, app.imageBathroomHeight = (app.imageBathroom.width, 
                                                       app.imageBathroom.height)
    app.crazyWidth, app.crazyHeight = (app.crazy.width, 
                                       app.crazy.height)
    app.fireballWidth, app.fireballHeight = (app.fireball.width, 
                                             app.fireball.height)
    app.followingWidth, app.followingHeight = (app.following.width, 
                                               app.following.height)
    app.peeWidth, app.peeHeight = (app.pee.width, 
                                   app.pee.height)
    app.powerHealthWidth, app.powerHealthHeight = (app.powerHealth.width, 
                                                  app.powerHealth.height)
    app.powerSpeedWidth, app.powerSpeedHeight = (app.powerSpeed.width, 
                                                  app.powerSpeed.height)
    app.imageHealthWidth, app.imageHealthHeight = (app.imageHealth.width, 
                                                  app.imageHealth.height)
    app.imageScoreWidth, app.imageScoreHeight = (app.imageScore.width,
                                                  app.imageScore.height)
    app.gameStartWidth, app.gameStartHeight = (app.imageGameStart.width,
                                               app.imageGameStart.height)
    app.image = CMUImage(app.image)
    app.image2 = CMUImage(app.image2)
    app.imageWiz = CMUImage(app.imageWiz)
    app.imageBathroom = CMUImage(app.imageBathroom)
    app.crazy = CMUImage(app.crazy)
    app.fireball = CMUImage(app.fireball)
    app.following = CMUImage(app.following)
    app.pee = CMUImage(app.pee)
    app.powerHealth = CMUImage(app.powerHealth)
    app.powerSpeed = CMUImage(app.powerSpeed)
    app.imageHealth = CMUImage(app.imageHealth)
    app.imageEmptyHealth = CMUImage(app.imageEmptyHealth)
    app.imageScore = CMUImage(app.imageScore)
    app.imageGameStart = CMUImage(app.imageGameStart)
    app.imageGameOver = CMUImage(app.imageGameOver)
    app.instructions = CMUImage(app.instructions)
    #initialize collision animation
    app.collisionRadius = 0
    app.collisionTicksLeft = 50
    app.collisionOpacity = 100  
    app.ouchLabelOpacity = 100
    app.collisionColor = None
    app.collisionAngle = random.randint(0, 360)
    app.colors = ['red', 'green', 'blue', 'yellow', 'violet', 'orange']

    #initialize maze
    app.mazeDifficulty = 5
    app.mazeStartRow = app.mazeDifficulty -1
    app.maze = Maze(app.mazeDifficulty, app.mazeStartRow, app.mazeStartRow)
    app.maze.mazeGenerator()
    app.mazeBool = app.maze.boolConverter()
    app.cellSize = 410 / app.maze.size

    #initialize character and gun
    app.poopColor = rgb(70,0,0)
    app.poopSpeed = 6
    app.poopPositionX = app.cellSize
    app.poopR = 150 // (app.mazeDifficulty)
    app.poopPositionY = (app.mazeDifficulty * app.cellSize) +  1.25 * app.poopR
    app.lineAngle = 0
    app.lineLength = 200 // (app.mazeDifficulty)
    app.health = 3
    app.gunLimit = 6
    app.shootGun = False
    app.reloadCounter = 0
    app.reloadGun = False

    #initialize bullet list and powerups
    app.bullets = []
    app.bullet2 = []
    app.bullet3 = []
    app.powerUp1 = PowerUp1(app)
    app.powerUp2 = PowerUp2(app)

    #magic orb :D
    app.magicRadius = 0
    app.magicTicksLeft = 50
    app.magicOpacity = 100  
    app.magicAngle = random.randint(0, 360)

def restartGame(app):
    # re-initialize world
    app.onStepCounter = 0
    app.gameOverBool = False
    app.currScore = 0
    app.highscore = app.highscore
    #re-initialize maze
    app.mazeDifficulty = 5
    app.mazeStartRow = app.mazeDifficulty -1
    app.maze = Maze(app.mazeDifficulty, app.mazeStartRow, app.mazeStartRow)
    app.maze.mazeGenerator()
    app.mazeBool = app.maze.boolConverter()
    app.cellSize = 410 / app.maze.size

    #re-initialize character and gun
    app.poopPositionX = app.cellSize
    app.poopR = 150 // (app.mazeDifficulty)
    app.lineAngle = 0
    app.lineLength = 200 // (app.mazeDifficulty)
    app.poopPositionY = (app.mazeDifficulty * app.cellSize) +  1.25 * app.poopR
    app.health = 3
    app.gunLimit = 6
    app.shootGun = False
    app.reloadCounter = 0
    app.reloadGun = False
    app.bullets = []
    app.bullet2 = []
    app.bullet3 = []
    app.powerUp1 = PowerUp1(app)
    app.powerUp2 = PowerUp2(app)

def restartApp(app):
    #initialize world
    app.onStepCounter = 0
    app.gameOverBool = False
    app.currScore = app.currScore
    app.highscore = app.highscore
    app.gameStart = True

    #initialize collision animation
    app.collisionRadius = 0
    app.collisionTicksLeft = app.collisionTicksLeft
    app.collisionOpacity = app.collisionOpacity
    app.ouchLabelOpacity = app.ouchLabelOpacity
    app.collisionColor = None
    app.collisionAngle = random.randint(0, 360)
    app.colors = ['red', 'green', 'blue', 'yellow', 'violet', 'orange']

    #initialize maze
    app.mazeDifficulty = app.mazeDifficulty + 2
    app.mazeStartRow = app.mazeDifficulty -1
    app.maze = Maze(app.mazeDifficulty, app.mazeStartRow, app.mazeStartRow)
    app.maze.mazeGenerator()
    app.mazeBool = app.maze.boolConverter()
    app.cellSize = 410 / app.maze.size

    #restart character and gun
    app.poopPositionX = app.cellSize
    app.poopR = 150 // (app.mazeDifficulty)
    app.poopPositionY = (app.mazeDifficulty * app.cellSize) +  1.25 * app.poopR
    app.lineLength = 200 // (app.mazeDifficulty)
    app.health = app.health
    app.gunLimit = app.gunLimit
    app.shootGun = False
    app.reloadCounter = 0
    app.reloadGun = False
    app.bullets = []
    app.bullet2 = []
    app.bullet3 = []
    app.powerUp1 = PowerUp1(app)
    app.powerUp2 = PowerUp2(app)

#game visual
def redrawAll(app):
    if app.gameInstructions:
        drawInstructions(app)
    #gameplay
    if app.gameStart:
        drawMaze(app)
        drawPoop(app)
        drawReload(app)
        drawHealth(app)
        drawScore(app)
        orbDraw(app)
        if app.powerUp1 is not None:
            app.powerUp1.draw(app)
        if app.powerUp2 is not None:
            app.powerUp2.draw(app)
        for bullet in app.bullets:
                bullet.draw(app)
        for bullet2 in app.bullet2:
            bullet2.draw(app)
        for bullet3 in app.bullet3:
            bullet3.draw(app)
        for gun in app.gun:
            gun.draw(app)

        if app.gameOverBool:
            drawGameOver(app)

    #splash screen
    else:
        #wizard duel picture that I referenced for splash screen
        #then I referenced pee picture and drew over poop picture on Procreate
        #with an font I found online
        drawImage(app.imageGameStart,0,0, 
                  width = app.gameStartWidth//2, 
                  height  = app.gameStartHeight//2)
                #https://www.pinterest.com/pin/429601251957737534/ 

                #https://www.pngitem.com/middle/hbRoJJm_transparent-
                #turd-png-super-poop-transparent-png-download/ 

                #https://www.reddit.com/r/BattleForDreamIsland/
                # comments/l5qwcr/pee_drop_the_recolor_poll_winner/ 

                #https://www.fontspace.com/witcher-knight-font-f83741
        


#game logic
def onKeyPress(app, key):
    if key == 'space': 
        app.gameInstructions = True
    if key == 'space' and app.gameInstructions:
        app.gameStart = True
    if key == 'space' and app.gameOverBool:
        restartGame(app)
    if key == 'm':
        restartApp(app)
    if key == 'r':
        app.reloadCounter = 200
        app.reloadGun = True

def onKeyHold(app, key):
    #character movement
    poopMove(app,key)

def onStep(app):
    #gamestart
    if app.gameStart:
        app.onStepCounter +=1
        enemySpawn(app)
        collisionTimer(app)
        gunLogic(app)
        powerUpLogic(app)
        bulletCollision(app)
        levelLogic(app)
        
def onMousePress(app, mouseX, mouseY):
    #gun logic
    if app.gunLimit != 0:
        app.shootGun = True
        app.gunLimit -=1

def onMouseMove(app, mouseX, mouseY):
    #gun point angle
    app.lineAngle = math.degrees(math.atan2(mouseY - 
                                app.poopPositionY, 
                                            mouseX - 
                                app.poopPositionX))
    #https://www.w3schools.com/python/ref_math_atan2.asp

#character visual functions
def drawPoop(app):
    newWidth, newHeight = (app.imageWidth * (app.poopR * 0.002), 
                           app.imageHeight* (app.poopR * 0.002))
    #poop picture
    drawImage(app.image,app.poopPositionX- (newWidth//2), 
              app.poopPositionY - (newHeight//2),
              width=newWidth,
              height=newHeight)
            #https://www.pngitem.com/middle/hbRoJJm_transparent-turd-
            # png-super-poop-transparent-png-download/ 
    drawGun(app)
    

def drawGun(app):
    gunX = (app.poopPositionX + app.lineLength * 
          math.cos(math.radians(app.lineAngle)))
    gunY = (app.poopPositionY + app.lineLength *
          math.sin(math.radians(app.lineAngle)))
        #https://www.w3schools.com/python/ref_math_radians.asp
        #https://www.geeksforgeeks.org/python-math-cos-function/#
        #https://www.w3schools.com/python/ref_math_sin.asp

    drawLine(app.poopPositionX, app.poopPositionY + (app.poopR//2), 
             gunX, gunY + (app.poopR//2), lineWidth = (app.poopR//3), 
             fill = 'yellow')

def drawReload(app):
    for i in range(6):
        x = app.width - (i * 45) - 40
        y = 250
        if i < app.gunLimit:
            fillColor = 'yellow'
        elif i < app.gunLimit + app.reloadCounter // 33:
            fillColor = 'grey'
        else:
            fillColor = None
        drawCircle(x, y, 20, fill=fillColor, border='black', borderWidth = 3)

def drawHealth(app):
    #health picture
    #health picture with removed color through Procreate
    #https://www.pngwing.com/en/free-png-maupqspeech  
    newWidth = app.imageHealthWidth //10
    newHeight = app.imageHealthHeight //10
    if app.health == 6:
        drawImage(app.imageHealth, app.width - 300, 0, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 200, 0, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 100, 0, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 300, 100, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 200, 100, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 100, 100, 
                  width = newWidth, 
                  height = newHeight)

    if app.health == 5:
        drawImage(app.imageHealth, app.width - 300, 0, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 200, 0, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 100, 0, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 300, 100, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 200, 100, 
                  width = newWidth, 
                  height = newHeight)

    if app.health == 4:
        drawImage(app.imageHealth, app.width - 300, 0, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 200, 0, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 100, 0, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 300, 100, 
                  width = newWidth, 
                  height = newHeight)

    if app.health == 3:
        drawImage(app.imageHealth, app.width - 300, 0, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 200, 0, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 100, 0, 
                  width = newWidth, 
                  height = newHeight)
        
    if app.health == 2:
        drawImage(app.imageHealth, app.width - 300, 0, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageHealth, app.width - 200, 0, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageEmptyHealth, app.width - 100, 0, 
                  width = newWidth, 
                  height = newHeight)
        collisionDraw(app)
        
        
    if app.health == 1:
        drawImage(app.imageHealth, app.width - 300, 0, 
                  width = newWidth, 
                  height = newHeight)
        drawImage(app.imageEmptyHealth, app.width - 200, 0, 
                  width = newWidth,
                  height = newHeight)
        drawImage(app.imageEmptyHealth, app.width - 100, 0, 
                  width = newWidth, 
                  height = newHeight)
        collisionDraw(app)

#game visuals
def drawInstructions(app):
    drawImage(app.instructions,0,0,
              width = app.gameStartWidth//2, 
              height  = app.gameStartHeight//2)
def drawGameOver(app):
        #wizard picture that I referenced for game over screen
        #then I drew over the poop picture on Procreate
        #with an font I found online
    drawImage(app.imageGameOver,0,0, 
              width = app.gameStartWidth//2, 
              height  = app.gameStartHeight//2)
            #https://www.pinterest.com/pin/63261569759219585/

            #https://www.pngwing.com/en/free-png-bmvwj

            #https://www.pngwing.com/en/free-png-bksnh/download

    drawLabel(f"{app.currScore}", 280 , 250, 
                        fill = 'black', bold = True, size = 34)
    drawLabel(f"{app.highscore}", app.width - 280, 250, 
                      fill = 'black', bold = True, size = 34)
def drawScore(app):
    drawLabel(f'Score:', app.width - 430, 30, 
                  size = 50, bold = True)
    drawLabel(f'{app.currScore}', app.width - 430, 80, 
                  size = 50, bold = True)

#misc. visual function
def orbDraw(app):
    for i in range(3):
        radius = max(app.magicRadius + random.randint(0, 80), 1) 
        points = random.randint(4, 9)
        drawStar(1100, app.height//2,radius,points,
                fill= random.choice(app.colors) ,border= 'black', borderWidth=2,
                opacity= random.randint(4, 70),rotateAngle=app.magicAngle)

#character movement logic
def poopMove(app,key):
        currX = app.poopPositionX
        currY = app.poopPositionY
        nextCellRow = int((app.poopPositionY) // app.cellSize)
        nextCellCol = int((app.poopPositionX) // app.cellSize)
        if not app.mazeBool[nextCellRow][nextCellCol]:
            if 'w' in key and not app.mazeBool[nextCellRow][nextCellCol]:
                    app.poopPositionY -= app.poopSpeed
            if 's' in key and not app.mazeBool[nextCellRow][nextCellCol]:
                    app.poopPositionY += app.poopSpeed
            if 'd' in key and not app.mazeBool[nextCellRow][nextCellCol]:
                    app.poopPositionX += app.poopSpeed
            if 'a' in key and not app.mazeBool[nextCellRow][nextCellCol]:
                    app.poopPositionX -= app.poopSpeed
        nextCellRow = int((app.poopPositionY) // app.cellSize)
        nextCellCol = int((app.poopPositionX) // app.cellSize)
        if app.mazeBool[nextCellRow][nextCellCol]:
            app.poopPositionX = currX
            app.poopPositionY = currY

#win logic
def levelLogic(app):
            if ((app.cellSize * (2* app.mazeDifficulty)-1) - 
                (app.cellSize//6)
                <= app.poopPositionX <= 
                app.cellSize * (2 * app.mazeDifficulty)  and
                ((app.mazeDifficulty + 0.5) * app.cellSize -(app.cellSize//6)
                <= app.poopPositionY <= 
                (app.mazeDifficulty + 0.5) * app.cellSize +(app.cellSize//6))):
                app.currScore += 1000
                restartApp(app)

#shoot logic
def gunLogic(app):
    if app.shootGun:
        gunX = (app.poopPositionX + app.lineLength 
                *math.cos(math.radians(app.lineAngle)))
        gunY = (app.poopPositionY + app.lineLength 
                * math.sin(math.radians(app.lineAngle)))
        #https://www.w3schools.com/python/ref_math_radians.asp
        #https://www.geeksforgeeks.org/python-math-cos-function/#
        #https://www.w3schools.com/python/ref_math_sin.asp

        gun = PlayerGun(gunX, gunY, app.lineAngle)
        app.gun.append(gun)
        app.shootGun = False
    
    for gun in app.gun:
        gun.x += gun.speed * math.cos(math.radians(gun.angle))
        gun.y += gun.speed * math.sin(math.radians(gun.angle))
        #https://www.w3schools.com/python/ref_math_radians.asp
        #https://www.geeksforgeeks.org/python-math-cos-function/#
        #https://www.w3schools.com/python/ref_math_sin.asp

    #reload logic
    if app.reloadGun:
        app.reloadCounter -= 3
        if app.reloadCounter <= 0:
            app.gunLimit = 6
            app.reloadGun = False
            app.reloadCounter = 0

#spawning and movement enemy logic
def enemySpawn(app):
    #fireball spawner
    if app.onStepCounter % (300//app.mazeDifficulty) == 0:
        app.bullets.append(Bullets(1100, app.height // 2, 
                app.poopPositionX, app.poopPositionY, app.mazeDifficulty))
        
    #crazy spawner
    if app.onStepCounter % (700//app.mazeDifficulty) == 0:
        app.bullet2.append(Bullet2(
            app.cellSize * (2 * app.mazeDifficulty),
            (app.mazeDifficulty * app.cellSize) + 1.25 * app.poopR,
            app.mazeDifficulty))
        
    for bullet2 in app.bullet2:
            bullet2.move(app)

    #homing spawner
    if app.onStepCounter % (500//app.mazeDifficulty) == 0:
        app.bullet3.append(Bullet3(1100, app.height // 2, 
        app.poopPositionX, app.poopPositionY, app.mazeDifficulty * 1.8))
    
    for bullet3 in app.bullet3:
        bullet3.poopX = app.poopPositionX
        bullet3.poopY = app.poopPositionY
        bullet3.move()

#powerup collision logic
def powerUpLogic(app):
    #health powerup
    if app.powerUp1 is not None:
        powerUpRow = app.powerUp1.row
        powerUpCol = app.powerUp1.col
        playerRow = int(app.poopPositionY // app.cellSize)
        playerCol = int(app.poopPositionX // app.cellSize)
        if powerUpRow == playerRow and powerUpCol == playerCol:
            if app.health < 6:
                app.health += 1
            app.powerUp1 = None

    #speed powerup
    if app.powerUp2 is not None:
        powerUpRow = app.powerUp2.row
        powerUpCol = app.powerUp2.col
        playerRow = int(app.poopPositionY // app.cellSize)
        playerCol = int(app.poopPositionX // app.cellSize)
        if powerUpRow == playerRow and powerUpCol == playerCol:
            app.poopSpeed += 2
            app.powerUp2 = None

#bullet collision logic
def bulletCollision(app):
    bulletsCopy = copy.copy(app.bullets)
    bullet2Copy = copy.copy(app.bullet2)
    bullet3Copy = copy.copy(app.bullet3)
    gunCopy = copy.copy(app.gun)
    for bullet in bulletsCopy:
        #fireball movement
        dx = bullet.poopX - bullet.x
        dy = bullet.poopY - bullet.y
        d = dx**2 + dy**2
        if d != 0:
            di = bullet.speed / d ** 0.5
            bullet.dx = dx * di
            bullet.dy = dy * di
        else:
            bullet.dx = 0
            bullet.dy = 0
        bullet.x += bullet.dx
        bullet.y += bullet.dy
        #player and fireball collision checker
        dx = bullet.x - app.poopPositionX
        dy = bullet.y - app.poopPositionY
        d = dx **2 + dy **2
        s = bullet.r + app.poopR
        if d <= s ** 2:
            app.health -= 1
            if app.health == 0:
                if app.currScore > app.highscore:
                    app.highscore = app.currScore
                app.gameOverBool = True
            app.bullets.remove(bullet)
            resetCollisionVariables(app)
        
        #gun and fireball collision checker
        for gun in gunCopy:
            dx = gun.x - bullet.x
            dy = gun. y- bullet.y
            d = dx**2 + dy**2
            s = bullet.r + gun.r
            if d<= s**2:
                app.bullets.remove(bullet)
                app.currScore += 100

    #player and crazy collision checker
    for bullet in bullet2Copy:
        dx = bullet.x - app.poopPositionX
        dy = bullet.y - app.poopPositionY
        d = dx **2 + dy **2
        s = bullet.r + app.poopR
        if d <= s ** 2:
            app.health -= 1
            if app.health == 0:
                if app.currScore > app.highscore:
                    app.highscore = app.currScore
                app.gameOverBool = True
            app.bullet2.remove(bullet)
            resetCollisionVariables(app)
        #gun and crazy collision checker
        for gun in gunCopy:
            dx = gun.x - bullet.x
            dy = gun. y- bullet.y
            d = dx**2 + dy**2
            s = bullet.r + gun.r
            if d<= s**2:
                app.bullet2.remove(bullet)
                app.currScore += 100

    #player and homing collision checker
    for bullet in bullet3Copy:
        dx = bullet.x - app.poopPositionX
        dy = bullet.y - app.poopPositionY
        d = dx **2 + dy **2
        s = bullet.r + app.poopR
        if d <= s ** 2:
            app.health -= 1
            if app.health == 0:
                if app.currScore > app.highscore:
                    app.highscore = app.currScore
                app.gameOverBool = True
            app.bullet3.remove(bullet)
            resetCollisionVariables(app)
        #gun and homing collision checker
        for gun in gunCopy:
            dx = gun.x - bullet.x
            dy = gun. y- bullet.y
            d = dx**2 + dy**2
            s = bullet.r + gun.r
            if d<= s**2:
                app.bullet3.remove(bullet)
                app.currScore += 100

#fireball enemy class
class Bullets(object):
    def __init__(self, x, y, poopX, poopY, speed):
        self.x = x 
        self.y = y
        self.poopX = poopX
        self.poopY = poopY
        self.speed = speed 
        self.r = 20
        dx = self.poopX - self.x
        dy = self.poopY - self.y
        d = dx ** 2 + dy ** 2
        if d != 0:
            di = self.speed / d** 0.5
            self.dx = dx * di
            self.dy = dy * di
        else:
            self.dx = 0
            self.dy = 0

    def draw(self,app):
        #fireball puffle picture
        drawImage(app.fireball, 
                  self.x - ((app.fireballWidth * (app.poopR * 0.003))//2), 
                  self.y - ((app.fireballHeight * (app.poopR * 0.003))//1.5), 
                  width = app.fireballWidth * (app.poopR * 0.003), 
                  height = app.fireballHeight * (app.poopR * 0.003))
                #https://www.pinterest.com/pin/15270086234254872/
    
    def update(self):
        self.x += self.dx
        self.y += self.dy

#crazy enemy class
class Bullet2(object):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.r = 10
        self.d = self.randD()

    def randD(self):
        return (random.choice([-1, 1]), random.choice([-1, 1]))

    def draw(self, app):
        #crazy puffle picture
        drawImage(app.crazy, 
                  self.x  - ((app.crazyWidth * (app.poopR * 0.003))//2), 
                  self.y - ((app.crazyHeight * (app.poopR * 0.003))//2),
                  width = app.crazyWidth * (app.poopR * 0.003), 
                  height = app.crazyHeight * (app.poopR * 0.003))
                #https://www.pinterest.com/pin/168251736073093319/

    def move(self, app):
        currX = self.x 
        currY = self.y
        nextX = self.x + self.d[0] * self.speed
        nextY = self.y + self.d[1] * self.speed
        nextX -= self.d[0] * 0.1
        nextY -= self.d[1] * 0.1
        nextCellRow = int(nextY // app.cellSize)
        nextCellCol = int(nextX // app.cellSize)
        if app.mazeBool[nextCellRow][nextCellCol]:
            self.x = currX
            self.y = currY
            self.d = self.randD()
        else:
            self.x = nextX
            self.y = nextY

#homing enemy class
class Bullet3(object):
    def __init__(self, x, y, poopX, poopY, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.r = 15
        self.poopX = poopX
        self.poopY = poopY

    def draw(self, app):
        #homing puffle picture
        drawImage(app.following,
                   self.x - ((app.followingWidth * (app.poopR * 0.003))//2),
                    self.y - ((app.followingHeight * (app.poopR * 0.003))//1.9), 
                     width = app.followingWidth * (app.poopR * 0.003), 
                     height = app.followingHeight * (app.poopR * 0.003))
                    #https://www.pinterest.com/pin/688839705518506531/

    def move(self):
        dx = self.poopX - self.x
        dy = self.poopY - self.y
        d = (dx**2 + dy**2)**0.5
        if d != 0:
            di = self.speed / d
            self.dx = dx * di
            self.dy = dy * di
        else:
            self.dx = 0
            self.dy = 0
        self.x += self.dx
        self.y += self.dy

class PowerUp1(object):
    def __init__(self, app):
        self.size = app.cellSize // 2
        self.row, self.col = self.randPosition(app)

    def randPosition(self, app):
        cleared = []
        for row in range(app.mazeDifficulty * 2):
            for col in range(app.mazeDifficulty * 2):
                if not app.mazeBool[row][col]:
                    cleared.append((row, col))
        if cleared:
            return random.choice(cleared)

    def draw(self, app):
            #health puffle picture
            drawImage(app.powerHealth, 
                    self.col * app.cellSize + app.cellSize // 4,
                    self.row * app.cellSize + app.cellSize // 4,
                    width = app.powerHealthWidth * (app.poopR * 0.003), 
                    height = app.powerHealthWidth * (app.poopR * 0.003))
                    #https://www.pinterest.com/pin/44684221294142926/

class PowerUp2(object):
    def __init__(self, app):
        self.size = app.cellSize // 2
        self.row, self.col = self.randPosition(app)

    def randPosition(self, app):
        cleared = []
        for row in range(app.mazeDifficulty * 2):
            for col in range(app.mazeDifficulty * 2):
                if not app.mazeBool[row][col]:
                    cleared.append((row, col))
        if cleared:
            return random.choice(cleared)

    def draw(self, app):
            #bunny puffle picture
            drawImage(app.powerSpeed, 
                    self.col * app.cellSize + app.cellSize // 4,
                    self.row * app.cellSize + app.cellSize // 4,
                    width = app.powerHealthWidth * (app.poopR * 0.003), 
                    height = app.powerHealthWidth * (app.poopR * 0.003))
                #https://www.pinterest.com/pin/99008891799499613/

#maze visualizing function
def drawMaze(app):
    drawRect(0,0,500,app.height, fill = rgb(90,90,70))
    #bathroom picture
    drawImage(app.imageBathroom, 450, -200)
            #https://www.instagram.com/p/CV2tuUQoZLH/ 

    #battle wizard picture
    drawImage(app.imageWiz, 800, 200, 
            width = app.imageWizWidth * 1.5, 
            height = app.imageWizHeight * 1.5)
            #https://www.pinterest.com/pin/38773246782173497/
    newWidth, newHeight = ((app.image2Width * 0.45) - (app.mazeDifficulty), 
                           (app.image2Height * 0.45) - (app.mazeDifficulty))
    
    #intestine background picture
    drawImage(app.image2,0,0, width=newWidth,height=newHeight)
            #https://www.vecteezy.com/vector-art/11674685-
            # brain-seamless-pattern-texture-anatomy-background 
    for row in range(len(app.mazeBool)):
        for col in range(len(app.mazeBool[0])):
            if app.mazeBool[row][col]:
                drawRect((app.cellSize * col), (app.cellSize * row), 
                         app.cellSize, app.cellSize, 
                        fill=gradient(rgb(250,170,170), 
                                      rgb(230,100,100), 
                                      rgb(180, 40, 50),
                        start='center'))
            if row == app.mazeDifficulty  and col == 0:
                drawRect((app.cellSize * col), (app.cellSize * row), 
                         app.cellSize, app.cellSize, 
                         fill=gradient(rgb(250,170,170), 
                                       rgb(250,10,100), 
                                       rgb(50, 4, 50)))
            if row == app.mazeDifficulty  and col == 2*app.mazeDifficulty:
                drawRect((app.cellSize * col), (app.cellSize * row), 
                         app.cellSize, app.cellSize, 
                         fill=gradient(rgb(250,170,170), 
                                       rgb(250,10,100), 
                                       rgb(50, 4, 50)))

#maze logic
class Maze(object):
    #pseudo code and algorithm idea citations
    #https://weblog.jamisbuck.org/2011/2/3/maze-generation-sidewinder-algorithm
    #https://www.baeldung.com/cs/maze-generation
    def __init__(self, size, row, col):
        self.size = size
        self.row = row
        self.col = col
        self.maze = []
        for x in range(size):
            rowList = []
            for y in range(size):
                rowList.append(set())
            self.maze.append(rowList)
    
    def neighbors(self, row, col):
        d = [(0,-1), (0,1), (1,0), (-1,0)]
        neighbors = []
        for drow, dcol in d:
            row2 = row + drow
            col2 = col + dcol
            if (0 <= row2 < self.size) and (0 <= col2 < self.size):
                neighbor = (row2, col2)
                if len(self.maze[neighbor[0]][neighbor[1]]) == 0:
                    neighbors.append(neighbor)
        return neighbors

    def mazeGenerator(self, row = None, col = None, visited = None):
        if row is None:
            row = self.row
            col = self.col
        if visited is None:
            visited = set()
        visited.add((row, col))
        neighbors = self.neighbors(row,col)

        while neighbors:
            nextCell = random.choice(neighbors)
            nextRow, nextCol = nextCell
            if nextCell not in visited:
                self.maze[row][col].add(nextCell)
                self.maze[nextRow][nextCol].add((row, col))
                self.mazeGenerator(nextRow, nextCol, visited)
            neighbors = self.neighbors(row, col)

    def boolConverter(self):
        mazeGrid = []
        for i in range(self.size * 2 + 1):
            mazeGrid.append([True] * (self.size * 2 + 1))

        for row in range(self.size * 2 + 1):
            for col in range(self.size * 2 + 1):
                if row % 2 == 1 and col % 2 == 1:
                    mazeGrid[row][col] = False

        for row in range(self.size):
            for col in range(self.size):
                if (row, col + 1) in self.maze[row][col]:
                    mazeGrid[row * 2 + 1][col * 2 + 2] = False
                if (row + 1, col) in self.maze[row][col]:
                    mazeGrid[row * 2 + 2][col * 2 + 1] = False
        return mazeGrid

#gun class
class PlayerGun(object):
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.speed = 10
        self.r = 4
        self.angle = angle
        
    def draw(self,app):
        #pee drawing
        drawImage(app.pee, 
                  self.x - ((app.peeWidth * (app.poopR * 0.002))//2), 
                  self.y - ((app.peeWidth * (app.poopR * 0.002))//2), 
                  width = app.peeWidth * (app.poopR * 0.002),
                  height = app.peeHeight * (app.poopR * 0.002))
                #https://www.reddit.com/r/BattleForDreamIsland/
                # comments/l5qwcr/pee_drop_the_recolor_poll_winner/ 
    
    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))
        #https://www.w3schools.com/python/ref_math_radians.asp
        #https://www.geeksforgeeks.org/python-math-cos-function/#
        #https://www.w3schools.com/python/ref_math_sin.asp
    app.gun = []

#collision animation functions
def collisionTimer(app):
            if app.collisionTicksLeft > 0:
                app.collisionTicksLeft -= 2.5
                collisionTime(app)
            if app.collisionTicksLeft % 10 == 0:
                collisionAttributes(app)

def resetCollisionVariables(app):
    app.collisionTicksLeft = 50
    app.collisionRadius = 0
    app.collisionOpacity = 100
    app.ouchLabelOpacity = 100
    app.collisionColor = None
    app.collisionAngle = random.randint(0, 360)
    
def collisionTime(app):
    app.collisionRadius = 35 - app.collisionTicksLeft
    app.collisionOpacity = app.collisionTicksLeft
    if app.collisionOpacity == 0:
        app.ouchLabelOpacity = 0

def collisionAttributes(app):
    app.collisionColor = random.choice(app.colors)

def collisionDraw(app):
    for i in range(3):
        radius = max(app.collisionRadius + random.randint(-20, 20), 1) 
        points = random.randint(4, 9)
        color = random.choice(app.colors)

        drawStar(app.poopPositionX + (1.5*app.poopR), 
                 app.poopPositionY,radius,points,
                fill = color, 
                border = 'black', 
                borderWidth=2,
                opacity = app.collisionOpacity,
                rotateAngle = app.collisionAngle)
        
    drawLabel('Ouch!', app.poopPositionX + (1.5*app.poopR), app.poopPositionY, 
                        size = (app.collisionRadius+ 14)//1.5,
                        fill ='white', 
                        opacity = app.ouchLabelOpacity,
                        border = 'black', 
                        borderWidth = 1.7, bold = True)

def main():
    runApp()
main()
