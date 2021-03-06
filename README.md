# Tic Tac Toe - Game

**[Live site](https://tic-tac-toe-cipp3.herokuapp.com/)**

---

<span id="top"></span>

## Index

- <a href="#context">Context</a>
- <a href="#ux">UX</a>
  - <a href="#ux-stories">User stories</a>
- <a href="#flowchart">Flow Chart</a>
- <a href="#features">Features</a>
  - <a href="#features-all">Game</a>
  - <a href="#features-future">Still to implement</a>
- <a href="#technologies">Technologies Used</a>
- <a href="#libraries">Libraries Used</a>
- <a href="#testing">Testing</a>
  - <a href="#testing-manual">Manual</a>
  - <a href="#testing-unresolved">Unresolved issues</a>
  - <a href="#testing-bugs">Known bugs</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>

---

<span id="context"></span>

## Context

Tic-tac-toe, noughts and crosses, or Xs and Os is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O.
This has been developed for an online use either against a computer or versus another player as you would in the classic game.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>
<span id="ux"></span>

## UX

<span id="ux-stories"></span>

### User stories

For ease of reference, the means by which a user's expectations have been met are summarised in the tables below:

| As a **User** I want | How this is achieved                                                                                                                                                           
:-|:-
To be able to play the game against friend or computer. | The game has been designed to let the player have option of both playstyles. When no one is around, get to play against computer or against a friend.
To be able to see my score. | The score is being exported each round to google spreadsheet where user can see everyone's scores. User can see their wins, loses, draws and total games played.
A clean and easy navigation throughout the game menu. | The game has been designed on users main input being numbers which guide them through all available options.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="flowchart"></span>

## Game flow chart

To understand how the game functions the following flow chart has been made using [Lucid Charts](https://www.lucidchart.com/pages/)

![Game flow chart](docs/flowchart.png)

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="features"></span>

## Features

<span id="features-all"></span>

**1. User Name**

- Once the program has executed the user is being asked for their name so the data can be exported to spreadsheet with their own ID so score can be tracked.

![Name input](docs/nameinput.png)

**2. Welcome Screen**

- Once the user has input their name, the welcome message gets printed with available options.
- The choice of either finding out how to play the game or starting the game is presented.

![Welcome screen](docs/welcomescreen.png)

**3. How to play**

- Prints to user a short guide of how to play the game.

![How to play](docs/howtoplay.png)

**4. Highscores**

- Prints to user a instructions of how to access the games public highscores.

![Highscores](docs/highscores.png)

**5. Print score**

- Prints to user a their current score throughout the game.

![Print score](docs/printscore.png)

**6. Game Options**

- User gets the option to play either versus their friend or a computer.

![Game options](docs/gameoption.png)

**7. Symbol choice**

- Once the game option has been selected, main player gets to choose their own symbol, either 'X' or an 'O'.

![Symbol choice](docs/symbolchoice.png)

**8. Game Vs Computer**

- User gets to go first and place their symbol on the grid.
- User has a reference grid beside to not forget which grid has which number assigned.
- Once the move has been completed, another grid is printed out with randomly generated number for computer.

![Game vs computer](docs/movevscomputer.png)

**9. Game Vs Player**

- Player ONE gets to go first and place their symbol on the grid.
- Both players have a reference grid beside to not forget which grid has which number assigned.
- Once the move has been completed, another grid is printed to player TWO where they get asked for their own move.
- Once their turn is over, player ONE gets asked for another move.

![Game vs player](docs/movevsplayer.png)

**10. Game over**

- Once one of 8 possible win choices is matched, the user gets a message printed with the result either win, lose or a draw.
- They get the option to exit the program or return to main menu where another game can be started.
- There is unique messages printed depending on either game over scenarios depending if the game was played against computer or another player.

![game over](docs/winvscomp.png)

**11. Game quit**

- If the user decided to quit, a message is being printed with their name.

![game over](docs/gamequit.png)

**12. Google spreadsheet**

- Used to track users total games played, their wins, loses and draws.
- Each player has been given unique ID so there are no duplicates even if the name has been input the same.
- The spreadsheet can be accessed via the following link [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1-Y5ELK0M6UVZzvqhET_WvSjDOCYEe1yWQOn9r_MsIfo/)

<span id="features-future"></span>

## Features left to implement

- An option for the user to choose who goes first in the beginning of the game.

  _The ability to decide whether the user wants the computer or player TWO to go first._

- Online multiplayer with lobbies.

  _The ability to see rooms with players wiating for a match._

- Users scores from google spreadsheet printed under not yet implemented 'high score' section.

  _The ability to see other players scores much quicker than going into spreadsheet._

- If the game was played in two player mode, track scores of the 2nd player.

  _The ability to track 2nd player scores so both of the users can see their score. Possibly under a different sheet._

- Improve computers difficulty.

  _Let computer move to one of the grids closest to users choice in order to block them._

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="technologies"></span>

## Technologies Used

### Languages

- CSS
- JavaScript - Generated from python essentials template.

### Project management

- [GitHub](https://github.com/) - Version control and deployment
- [GitPod](https://gitpod.io/) - IDE used to code the site
- [Heroku](https://www.heroku.com/) - To deploy the program to public

### Online resources

- [Stack Overflow](https://stackoverflow.com/)
- [W3 Schools](https://www.w3schools.com/)

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="libraries"></span>

## Libraries Used

- For this project I have only used two external libraries.
- RANDOM

  _This library was used to generate random move for computer in between 1 and 9._

- GSPREAD

  _This library was used to export data to google spreadsheet._

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing"></span>

## Testing

<span id="testing-manual"></span>

### Manual testing

The following cases were carried out to ensure that the program is functioning as expected:
**ALL PASSED**

- PEP8 Linter

  _The code has been pasted and came back with no errors._
- Features

  _All features have been tested manually to see if all the inputs work as expected._

<span id="testing-unresolved"></span>

### Unresolved Issues

- None

<span id="testing-bugs"></span>

### Known bugs

- None at present

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

## Deployment

There is just one branch of this project and the deployed version of this site is the most current version in the repository. The live site can be accessed via this link here - [Tic Tac Toe](https://tic-tac-toe-cipp3.herokuapp.com/)

### How to deploy

### Heroku
To deploy this page to Heroku from its [GitHub repository](https://github.com/erykslezak/CIPP3) the following steps were taken:

- Log into or register new account at [Heroku](https://www.heroku.com/).
- Click the button **New** in top right corner of the dashboard.
- From the drop-down menu select **Create new app**.
- Enter your apps name in the first field and select your region.
- Click on **Create App** if you are happy with your choices.
- Once you the app is made you will see yourself within **Deploy** tab. Press on **Settings** tab.
- Once you are in the **Settings** tab scroll down till you find **Config Vars**.
- Press the button **Reveal Config Vars** and for 'KEY' field, type in PORT and for the value field type in '8000'.
Press the **Add** button.
- Scroll down to **Buildpacks**. Click the button **Add buildpack** and select 'python'. Do the same step and add 'node.js'.
**PYTHON MUST BE ON TOP OF THE BUILDPACKS. IF IN YOUR CASE NODE.JS IS FIRST, CLICK AND DRAG PYTHON TO TOP AND SAVE.**
- Return back to the **Deploy** tab. From the deployment method, select 'Github' as the deployment.
- You will be asked to connect your github account. Confirm and proceed.
- Search for your repository name and connect.
- Once that is done and successfully connected, select how you want to push updates from the following options.

  _Clicking **Enable Automatic Deploys**. This will update once you push updates to your Github._

  _Selecting the correct branch for deployment from drop-down menu and pressing **Deploy Branch** button. This will have to be done everytime manually._

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="credits"></span>

## Credits

- [Stack Overflow](https://stackoverflow.com/) - Many issues I have googled brought me there as other coders were in similar situations.
- [W3 Schools](https://www.w3schools.com/) - Best resource when it comes to attributes etc. Used it many times and without it I would be more confused.
- [Github](https://github.com/Edb83) - README Layout
- [Mentor]() - I wanna thank my mentor Spencer for all his input regarding my code and being my second pair of eyes.
- [Google](https://www.google.com/) - Ammm yes.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>