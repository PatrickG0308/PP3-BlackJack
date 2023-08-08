# BlackJack

![Title](./assets/images/gif/gameplay.gif))

This application is a Python based BlackJack game, requesting the user to enter their name
prior to playing the game.

Link to [live site](https://blackjack-pgrant-e8836bcdd18d.herokuapp.com)

## Index - Table of Contents

- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#possible-future-features)

- [UX](#ux)
    - [Site Goals](#site-goals)
    - [User Stories](#user-stories)
    
- [Technology Used](#technologies)

- [Logical flow](#logical-flow) 

- [Testing](#testing) 
    - [Validator Testing](#validator-testing)
    - [Manual Testing](#manual-testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)

- [Deployment](#deployment)

- [Credits](#credits)


##


## Features

The site contains all necessary features of a simple, functioning BlackJack game.

### Existing Features


- **Welcome & Player Name entry**
    - Press 'RUN PROGRAM' to begin the game
    - User will be requested to enter their name (min of 3 letters no spaces)	
    	

    ![start page](/assets/images/screenshots/username.png)

- **Option Menu**
    - After valid player name entry player will be presented with a Options Menu
    - Choices are 
        1. View Instructions
        2. Start Game
          

    ![options menu](/assets/images/screenshots/options.png)

- **View Instructions Option**

    - Lists out 11 instructions on how to play the game
    - Options menu will appear at the end of the instructions


    ![instructions](/assets/images/screenshots/instructions.png)
    
- **Game Area**
    - The main feature of the app
    - Player and Dealer will be dealt 2 cards, one of the dealers cards will remain unseen (X).
    - A total for the Player card value will be displayed `(Value: xx)`
    - Player will be offered the choice to take another card `hit` (h) to allow them to get to target value of 21 or to keep their current card value by choosing `stand` (s)
    - If player chooses another card and the value exceeds 21 they are bust and the dealer wins.
    - If they select another card or stand and are under the value 21 the dealer is then dealt a card, dealer will try to beat players value or bust, this will determine winner of game.

    ![game area](/assets/images/screenshots/fullgame.png)

- **Play Again**
    - Upon completion of a game, player will be offered the choice of play again `y` or finish the game by choosing `n`
    - If player chooses to play again the terminal will clear and a new game will commence.	
    


    ![play again](/assets/images/screenshots/playagain.png)
    

- **Game Complete**
    - Should player choose to finish the game by choosing `n`, the result of the game will appear and a Thank You message to the player will be displayed	
    
    ![game over](/assets/images/screenshots/gameend.png)

- **Error messages** 
   - If Player does not enter the correct number of letters, enters invalid characters or enters a space when entering their name they will receive an error telling them their entry was invalid and the reason why.
   - During the game if the player enters a character other than `(h)` for Hit or `(s)` for Stand they will also receive an error stating Invalid input. Please enter 'h' or 's'.

   ![letter_error](/assets/images/screenshots/letterserror.png)
   ![hit\stand_error](/assets/images/screenshots/hserror.png)


   ## Possible Future Features

- **Playing Cards**
    - Use Ascii to create playing card image, welcome message and congratulations graphic. 


 ## UX

### Site Goals

The goal of this app is to provide a simple game of BlackJack, allowing players the choice to hit or stand to try and beat the dealer.
The game is intended to be played over the course of a few minutes. It does not take up too much of the players's time by playing, functionality or reading instructions.

### User Stories

**As a site visitor I want to:**

- read a brief and simple description of how to play
- be able to play the game with simple click interaction
- view the card value for both player and dealer
- be clearly informed of the result of each game
- have a total of wins and losses at the end of the game

**As the site administrator I want to:**

- be able to make modifications to the game (see [future features](#possible-future-features))
- offer the user the chance to explore the code for the site 

## Technologies
- Heroku
    - Used to deploy and host the application
- Python
    - Code used to create the application
- CodeAnywhere
    - The app was developed using Visual Studio Code IDE https://app.codeanywhere.com/
- GitHub
    - Source code is hosted on GitHub and deployed using Heroku.
- Git
    - Used for version control
- Colorama
    - Adding colored terminal text to the game (https://pypi.org/project/colorama/) 
- Screen Recorder
    - Capture game play for title gif
    - https://chrome.google.com/webstore/detail/screen-recorder/hniebljpgcogalllopnjokppmgbhaden
- ezgif
    - Used to create the title gif (https://ezgif.com/)