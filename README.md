# CSC290 POSt-Man
CSC 290 Group assignment repo for "POSt-Man" game.


## Game Description

"POSt-Man" is a University of Toronto themed Pacman game. Players attempt to achieve a GPA (score) of 4.0 by collecting points, while avoiding bad grades (ghosts) that pursuit them.

It takes a classic game and redesigns it to better appeal to Unversity students who study Computer Science, especially students in UTM.
With the nostalgic gameplay of the original Pacman, and a new and refreshed visual and gameplay design, we, the 4.0 Squad, hope that students and peers can find our game interesting and challenge themselves by trying out the game and make POSt!


## Table of Contents

- [Installation](https://github.com/itsninaricci29/CSC290Pacdude#Installation-Guide)
  - [For Windows](https://github.com/itsninaricci29/CSC290Pacdude#For-Windows)
  - [For Mac](https://github.com/itsninaricci29/CSC290Pacdude#For-Mac)
  - [For Linux](https://github.com/itsninaricci29/CSC290Pacdude#For-Linux)
- [How to Play](https://github.com/itsninaricci29/CSC290Pacdude#How-to-Play)
  - [Launch Instructions](https://github.com/itsninaricci29/CSC290Pacdude#Launch-Instructions)
  - [Controls](https://github.com/itsninaricci29/CSC290Pacdude#Controls)
  - [Gameplay Tips](https://github.com/itsninaricci29/CSC290Pacdude#Gameplay-Tips)
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
![Gameplay Screenshot](Users/16474/Pictures/gamepic.png)

## Out of Scope Features

Here is a list of features that didn't make it to our final version of the game due to time constraints and lack of additional skills
- A power-up system, that could increase the movement speed of the player, or allow them to eat ghosts etc.
- Different behavioral AI, to make the ghosts feel unique and add additional depth to the gameplay.
- Shortcuts around the map to quickly traverse from one side to the other.
- SoundFX and BGM to immerse the player
- Sprite animations for the player's and ghosts' actions
- Multiple map designs/levels

As this project is open source, we encourage any developer to try and improve the game by adding these features listed above, and even add some unique features of their own to make "POSt-Man" the best version it can be!

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

Wrote the description section, the out of scope features and gameplay section, added some additional points under gameplay tips. Provided additional methods such as getValue() and the move() methods in the Food class. Designed and created the map design of the game as a txt file. Designed and created all of the sprites and images used in the game, including sprites for the barriers, points, ghosts and pacman (the player) itself.

## Licening 
