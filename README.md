<h1>Star Trek Battleships</h1>

![picture of the project in a responsive context](documentation/responsive.PNG)

## Overview

<p>Star Trek Battleships is a single player, python terminal game where players can play a classic battleships style game by placing their ships and then taking turns firing at the computer board.</p>

The game can be found deployed on Heroku with this [Link](https://star-trek-battleships-ae86cac7948c.herokuapp.com/) or by pasting the folloing into your web browser https://star-trek-battleships-ae86cac7948c.herokuapp.com/

## How to play

<h3>To start the game:</h3>

- The player will be promted to place all 5 ships of diffent lengths.
- First they will choose if the ship will be horizontal or vertical.
- Then they will choose a row number and collumn letter to place the ship in.
- The first cell of the ship will be placed in the cell they chose, with the
remaing cells stretching either horizontally or vertically depending on what 
the player chose.
- Ships cannot be placed on top of eachother or in a position that they would
overlap the board.
- Once all ships are placed the player will chose which row and column they
want to fire at.
- If all computer ships are destroyed then the player wins.
- If all player ships are destroyed then the computer wins.

link to the game https://star-trek-battleships-ae86cac7948c.herokuapp.com/

## User Stories
<h3>First Time Visitor Goals:</h3>

- As a first-time visitor, I want to easily understand the main purpose of the game and what it does.
- As a first-time visitor, I want to easily navigate the controls of the game.
- As a first-time visitor, I want to quickly start the game since that's what I'm here for.

<h3>Returning Visitor Goals:</h3>

- As a returning visitor, I want to try my luck again.
- As a returning visitor, I want to see the same familiar game layout so I can get straight into a new game.

## Features

<h3>When the game is loaded:</h3>

- The user can see a welcome message with promps on how to get started.
<br>

![Picture of the welcome message](documentation/welcome.PNG)

- The Board will be printed and the player will choose where to place their ships
<br>
- The computer will also randomly place thier ships

![Picture of how to place ships](documentation/placehips.PNG)

- If the player enters nothing, enters something invalid or enters a position that overlaps with other ships or the edge of the board, they will be asked to try again.
<br>

![Picture of what happens if entry is invalid](documentation/invalid.PNG)

- Once all ships are placed the user can see their board and the computer board and will be asked to choose a row and column to fire at on the computer board.
<br>
- The computer will fire at random locations after each player turn. The computer cannot fire where they have fired already.

![Picture of user chooses where to fire](documentation/choosecelltofireat.PNG)

- Once either the computer or the player has destroyed all ships (17 hits) the game is over

![Picture of the player winning the game](documentation/congratulations.PNG)
![Picture of the player winning the game](documentation/defeat.PNG)

## Flowchart

- The flowchart represents the logic of the application:

![Picture of the player winning the game](documentation/lucidflowchart.PNG)


## Technologies Used

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/) was used to anchor the project and direct all application behavior
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) was used to construct the elements involved in building the mock terminal in the browser
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) was used provide the start script needed to run the Code Institute mock terminal in the browser
- [VSCode](https://code.visualstudio.com/) was used as the main tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the project.
- [Heroku](https://dashboard.heroku.com/apps) was used to deploy the project.

## Imports

- [random](https://docs.python.org/3/library/random.html) was used for the computer to randomly place ships and randomly fire across the player board.

Third part import:
- [colorama](https://pypi.org/project/colorama/) was used to add some colour to the project.


## Bugs

Solved bugs:
- Had many issues with the input errors where if the user entered something
unexpected it could crash the whole program.
- one was due to the user entering nothing, and then nothing cannot be converted
into an integer and since the break/except criteria was not met it cause an infinity loop.
- Similarly if the user entered anything but a letter for column, this could then not be passed through the numbers_to_letters function and crashed the program.
these bugs were fixed by using try/except statements where another other that what was expected will simply ask for the valid data again.


## Testing



## Deployment

### Deployment to GitHub Pages

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the [GitHub repository](https://github.com/Allwrightben/starquiz), navigate to the Settings tab 
  - From the source section drop-down menu, select the **Main** Branch, then click "Save".
  - The page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

  The live link can be found [here](https://allwrightben.github.io/starquiz/)

## Contact

Ben Allwright<br>
ben.allwright@learningpeople.co.uk

Feel free to reach out if you have any questions or feedback! Thank you for visiting<br> https://github.com/Allwrightben/starquiz

## Credits

- <h3>Inspiration</h3>

  - The Love Math project and JavaScript modules gave me a lot of inspiration.
  - My mentor Juliia I must say has been amazing, far beyond what I would have expected :)

- <h3>Media</h3>

- The website features one background image sourced from https://unsplash.com/



