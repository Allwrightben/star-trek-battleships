<h1>Star Trek Battleships</h1>

![picture of the website in a responsive context](assets/images/documentation/mainresponsive.png)

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

![Picture of how to place ships](documentation/placehips.PNG)

- If the player enters nothing, enters something invalid or enters a position that overlaps with other ships or the edge of the board, they will be asked to try again.
<br>

![Picture of what happens if entry is invalid](documentation/invalid.PNG)

- Once all ships are placed The user will be asked to choose a row and column to fire at.
<br>

![Picture of the rules button to the right of the website](assets/images/documentation/starwarsright.png)

![Picture of the rules](assets/images/documentation/rules.png)

- When the user clicks start it will show the first question.
- The user will also see their score in the bottom left.
- The user will also see how many questions they have remaining in the bottom right
<br>

![Picture of the quiz started](assets/images/documentation/start.png)

- All of the buttons on the site offer the user feedback with on-hover animations and pointers.
- within the quiz, the user will get instant feedback for a correct answer.
- The user will also now only be able to click the next button as all the answer buttons are disabled.
- The user will see that their score has increased by 1, and they now only have 9 questions remaining. 
<br>

![Picture of a correct answer](assets/images/documentation/next.png)

- The user will also get feedback for an incorrect answer.
- the user will see that the answer they selected is now red, indicating that it was a wrong answer, and they didn't get a point and they have one less question to answer.
<br>

![Picture of a wrong answer](assets/images/documentation/wrong.png)

- Each time the user selects one of four answers the correct answer will turn green and all other answers will be red.

- Using the site is intuitive and easy to understand.
- The website is responsive.
  - on laptop screen sizes and larger, the website will feature larger text and buttons.
  - on tablet screen sizes and smaller, the website text and buttons will be smaller.

## Technologies Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) was used as the foundation of the site.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/css) was used to add the styles and layout of the site.
- [CSS Flexbox](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox) was used to arrange items symmetrically on the pages.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) was used to create all the logic and visuals necessary to make the quiz work.
- [VSCode](https://code.visualstudio.com/) was used as the main tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the website.
- [GitHub](https://github.com/) was used to host the code of the website.

## Testing

<h3>Compatability</h3>

In order to confirm the correct functionality, responsiveness and appearance:
- The website was tested on Chrome and Edge web browsers, using in-built dev tools.
  - Chrome:
  ![picture of the website being tested in Chrome](assets/images/documentation/chrome1.png)
  ![picture of the website being tested in Chrome](assets/images/documentation/chrome2.png)
  ![picture of the website being tested in Chrome](assets/images/documentation/chrome3.png)
  ![picture of the website being tested in Chrome](assets/images/documentation/chrome4.png)
  ![picture of the website being tested in Chrome](assets/images/documentation/chrome5.png)

  - Edge:
  ![picture of the website being tested in Edge](assets/images/documentation/edge1.png)
  ![picture of the website being tested in Edge](assets/images/documentation/edge2.png)
  ![picture of the website being tested in Edge](assets/images/documentation/edge3.png)
  ![picture of the website being tested in Edge](assets/images/documentation/edge4.png)
  ![picture of the website being tested in Edge](assets/images/documentation/edge5.png)

- The website was also tested using the Chrome extension [Responsive Viewer](https://chromewebstore.google.com/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?pli=1)
    ![picture of responsive viewer on small devices](assets/images/documentation/responsiveviewer1.png)
    ![picture of responsive viewer on larger devices](assets/images/documentation/responsiveviewer2.png) 

- The website's responsiveness was tested using Media Genesis Responsive design checker
https://responsivedesignchecker.com/
<br>

![picture of the responisveness checker](assets/images/documentation/genesis1.png)

![picture of the responisveness checker](assets/images/documentation/genesis2.png)

![picture of the responisveness checker](assets/images/documentation/genesis3.png)

- The HTML file has passed HTML validity checks with W3C.
<br>

![Picture of main page HTML pass](assets/images/documentation/w3c.png)

- The CSS file has also passed CSS validity check with W3C.
<br>

![Picture of CSS File page pass](assets/images/documentation/w3ccss.png)

- The JavaScript was tested for errors using JShint
<br>

![Picture of JShint results](assets/images/documentation/jshint.png)

- Lighthouse
  - The website has been tested for performance, accessibility, best practice and SEO.<br>

![Picture of lighthouse analysis](assets/images/documentation/lighthouse.png)
    

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



