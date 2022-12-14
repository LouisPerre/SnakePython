# Pygame Snake #

This project is a part of my course on python at IIM

## ✨ Launch the game ✨ ##
To launch the game clone the entire repo and run this command 
```commandline
python ./main.py
```

This game use simple input like :
```commandline
'W', 'Z', 'UP' To go up
'S', 'DOWN' To go down
'A', 'Q', 'LEFT' To go left
'D', 'RIGHT' To go right
```

The goal is to eat as much apple as you can.

### ⚙ How it was made ⚙ ###

This project was built with pygame which allows many things like image manipulation, vector, sound </br>
You can do a lot with this library so don't hesitate to go look at the docs and learn

I made 5 Classes to manipulate all my game like that :
```commandline
FruitClass -> Draw and generate fruit 
GameClass -> Launch the game and update the screen
MainClass -> Every technical aspect of this game (Collision check, Update mouvement, Draw every element, game over
ScoreClass -> Show the dead screen with the highest score and store yours inside a csv file
SnakeClass -> Add block, draw, move the snake and update the graphics of this little guy
```