# CSC290 POSt-Man
CSC 290 Group assignment repo for "POSt-Man" game.


## Game Description

Is UofT drowning you with loads of assignments and tests? But you would rather enjoy playing a fun game? Then Post-Man is the game for you!

Post-Man is a UofT themed game based on the original game “PacMan”. Post-Man is implemented using Python which fully utilizes a python library called PyGame to produce a fully functioning UI. A simple interface has been designed for a unique user experience. 

This real-time game requires the user to use the directional keys on their keyboard to move the player. The player has three lives for the duration of the game meaning if the player encounters a bad assignment, a life is taken away.  The player’s main goal is to acquire a certain GPA (score) of 4.0 by collecting powerups while avoiding bad assignments to ensure entry into the Computer Science POST. 

So do you have what it takes to make Computer Science POST?


## Table of Contents

- [Installation](https://github.com/itsninaricci29/CSC290Pacdude#Installation-Guide)
  - [For Windows](https://github.com/itsninaricci29/CSC290Pacdude#For-Windows)
  - [For Mac](https://github.com/itsninaricci29/CSC290Pacdude#For-Mac)
  - [For Linux](https://github.com/itsninaricci29/CSC290Pacdude#For-Linux)
- [How to Play](https://github.com/itsninaricci29/CSC290Pacdude#How-to-Play)
  - [Launch Instructions](https://github.com/itsninaricci29/CSC290Pacdude#Launch-Instructions)
  - [Controls](https://github.com/itsninaricci29/CSC290Pacdude#Controls)
  - [Gameplay Tips](https://github.com/itsninaricci29/CSC290Pacdude#Gameplay-Tips)
- [Documentation and Directory Structure](https://github.com/itsninaricci29/CSC290Pacdude#Documentation-and-Directory-Structure)
- [Authors](https://github.com/itsninaricci29/CSC290Pacdude#Authors)
- [Addendum](https://github.com/itsninaricci29/CSC290Pacdude#Addendum)

## Installation Guide

### For Windows

1. Install the latest non-legacy release of python from https://www.python.org/downloads/. Ensure that you download the *exe* or *msi* installer. The website will usually present you with the download appropriate for your system.

2. Install the latest release of pygame from https://www.pygame.org/download.shtml. Ensure that you download the *exe* or *msi* installer, under the windows section of the page. Alternatively, run the command `pip install pygame` in the terminal.

3. Download the game's zip file and extract it from the repository webpage, or clone the repository with `https://github.com/itsninaricci29/CSC290Pacdude.git`. 

### For Mac

1. Install the latest non-legacy release of python from https://www.python.org/downloads/. Ensure that you download the *dmg* or *pkg* installer. The website will usually present you with the download appropriate for your system.

2. Install the latest release of pygame from https://www.pygame.org/download.shtml. Ensure that you download the *dmg* or *pkg* installer, under the macintosh section of the page. Alternatively, run the command `pip install pygame` in the terminal.

3. Download the game's zip file and extract it from the repository webpage, or clone the repository with `https://github.com/itsninaricci29/CSC290Pacdude.git`. 

### For Linux

1. Install the latest non-legacy release of python from https://www.python.org/downloads/. Ensure that you download the *dmg* or *pkg* installer. The website will usually present you with the download appropriate for your system. Alternatively, run the command `apt-get install python` for debian based distributions or `pacman -S python` for Arch-Linux based distrobutions in the terminal. 

2. Install the latest release of pygame by running the command `pip install pygame`. Alternatively, download the tarball from https://www.pygame.org/download.shtml if you wish to compile from source.

3. Download the game's zip file and extract it from the repository webpage, or clone the repository with `https://github.com/itsninaricci29/CSC290Pacdude.git`. 

### How to Play

##### Launch Instructions

Ensure that python and pygame are downloaded, and system variables contains the directory of the python interpreter.
Then, run the main.py file to start the game. This will immediately put you into a new game of POSt-Man.

##### Controls

Use the arrow Keys to move.

##### Gameplay Tips

- Collect points (yellow circles) to increase the current score.
- You win the game by achieving a score of 4.0.
- You lose the game if the player character touches a ghost.
- The ghosts will chase the player around the map for the duration of the game.
- Avoid getting cornered by multiple ghosts, as escape would be almost impossible.

##### Gameplay

- The game is set in a maze similar to the original Pacman, but with UTM themed elements.
- Key differences from the original Pacman game:
  - No shortcuts on the sides of the map
  - All 4 ghosts have identical AI, meaning that they will behave the same way
  - No power-ups that allows the player to eat the ghosts
  - A redesigned map
  
 These differences were made to switch up the old formula and give the game a new take.

##### Gameplay Screenshot
![gamepic](https://user-images.githubusercontent.com/55632420/70191370-7de95200-16c6-11ea-8045-c7d6b30a867d.PNG)

From the Screenshot above we are able to easily idenify:

![point](https://user-images.githubusercontent.com/55632420/70193790-42eb1c80-16ce-11ea-91d4-b112f2219bb6.PNG)
-The points which will increase you CGPA.

![ghost](https://user-images.githubusercontent.com/55632420/70193792-454d7680-16ce-11ea-96ec-fe5e0598a81c.PNG)
-The ghosts which should be avioded at all costs.

![player](https://user-images.githubusercontent.com/55632420/70191645-6d85a700-16c7-11ea-9888-51b5d1953d88.PNG) 
-The player centered right in the middle.

![wall](https://user-images.githubusercontent.com/55632420/70191674-89894880-16c7-11ea-8674-903b952b283c.PNG) 
-Walls which represent the bourdaries.

## Out of Scope Features

Here is a list of features that didn't make it to our final version of the game due to time constraints and lack of additional skills
- A power-up system, that could increase the movement speed of the player, or allow them to eat ghosts etc.
- Different behavioral AI, to make the ghosts feel unique and add additional depth to the gameplay.
- Shortcuts around the map to quickly traverse from one side to the other.
- SoundFX and BGM to immerse the player
- Sprite animations for the player's and ghosts' actions
- Multiple map designs/levels

As this project is open source, we encourage any developer to try and improve the game by adding these features listed above, and even add some unique features of their own to make "POSt-Man" the best version it can be!

## Documentation and Directory Structure:
The documentation of the major classes, methods can be found in the Wiki page of this repository, over [here](https://github.com/itsninaricci29/CSC290Pacdude/wiki/Welcome-to-the-POSt-Man-Documentation)

## Authors

POSt-man was created as the final project for the second year course CSC290 at the University of Toronto Mississauga. The authors for POSt-Man include:

-	Patrick Yevych
-	Nina Ricci Lu
- Mayra Nihal
-	Alex Quach
- Saad Qadri

## Addendum 

### Patrick 

Wrote the installation instructions section (including the subsections: for windows, for mac, for linux). Wrote the how to play section (including the subsections: launch instructions, controls, gameplay tips). Wrote the table of contents elements for those sections. Programmed the functions is_game_over(), execute(), chase_pacman(), is_touching(), check_left(), check_right(), check_down(), check_up(), move_left(), move_right(), move_down(), move_up(). Created the barrier, food and pacman classes and their member variables.

### Alex

Wrote the out of scope features and gameplay section, added some additional points under gameplay tips. Provided additional methods such as getValue() and the move() methods in the Food class. Designed and created the map design of the game as a txt file. Designed and created all of the sprites and images used in the game, including sprites for the barriers, points, ghosts and pacman (the player) itself.

### Nina

For the README, I wrote a detailed description of the game outlining what the game is and its rules. As for the code, I wrote an interface class Actor that contains the method move(). I also fully implemented the subclass Player()  that inherits the move() method. For the Game class, I implemented an initializer that initialized all the variables that are essential in this class. I also implemented the method load_map which requires a text file that represents a level of the game containing unique symbols. I also created a Main.py that initializes the Game() and runs the main application.

### Saad

Displayed the Gameplay Screenshot section, which illustrated the visuals of our game including what each of them represents and wrote the licensing information. Created the initial map.txt which is basically the map used in our level created to add and remove methods for each of the various actor classes, added a map setup method which sets up the visuals components of our game, added a method to check if the game has been won and if the game is over, added the on_init(), on_event and close_game() method as well to further help with running our game.

### Mayra
For the README, I added the Authors section as well as the Documentation and Directory Structure section. Additionally, I wrote the entire project documentation page that is located on this repository's Wiki page, which includes the major classes and methods, as well as how to extend our game. For code, I added code that was required for the game logic part, such as the Player's num_lives attribute, and the is_dead method. The num_lives attribute keeps track of how many lives the Player has, and the is_dead method returns whether the player is still alive. I also added to the Player's move() method, which enables the player to make a move depending on if is_dead returns false or not. Moreover, I also added the move() method inside the Barrier class that overrides the move method from Barrier's superclass (called Actor). The reasoning behind this was so that a Barrier object would not move at any point throughout the game.

## License Information
-The MIT License (MIT)

-Copyright © [2019] [Saad Qadri, Nina Ricci Lu, Mayra Nihal, Alex Quach, Patrick Yevych]

-You can find a copy of the License at https://mit-license.org/

-License for them is in Public Domain


