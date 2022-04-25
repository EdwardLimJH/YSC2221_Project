# YSC2221_Project

Help Me Study Game

About the project:
This program creates a game where you dodge obstacles and collect points using
the right and left arrow keys.

Pre-Requisites:
The version of python used to create this program was Python 3.10.2
The libraries used include pygame 2.1.2, flake8 4.0.1, pytest 7.1.0,
pytest-mock 3.7.0. 
The required libraries are all inside requirements.txt and to install the
dependencies, you can run the following code.

pip3 install -r requirements.txt

How to run the program:
Ensure that all the provided files are in the same folder.
Run the "Help_Me_Study_Game.py" to play the game.
You may run the game with the following code:
#assuming you are at the directory of Help_Me_Study_Game.py

python Help_Me_Study_Game.py

How the game works:
After running the python file, the first screen will prompt
the user to input a username. Press enter to continue

Following the login will be an instructions screen. Press
space to continue

The Game will begin and users can only press the left and 
right arrow keys to move the character to the left or 
right respectively.

After the time is up, the game will end and a Game over 
screen will be displaced. Users can press L to see the
leaderboard or press space to restart the game

If the user presses L, the leaderboard screen will show 
the users can press the "Esc" button to go back to the
game over screen.

The program will run infinitely until the user clicks on 
the "X" button at the top right corner of the window.
Pressing the "X" button at the top right corner of the
window will close and end the program.

Running Tests:
A basic test file has been provided named "test_game.py".
The test checks the core game logic and ensures that when
the user presses the left or right arrow, the game executes
the correct response. You can run the test filw using this code:
#assuming the you are in the same file directory

pytest ./test_game.py

Contributors:
Edward, Jameela, Laura, Meryl, Shikhar

Acknowledgements:

Removed background from images:
https://www.remove.bg/upload

Helvetica Font downloaded from:
https://freefontsfamily.com/helvetica-font-family/

Pokemon Font downloaded from:
https://www.fontspace.com/pokemon-gb-font-f9621

Suboleya Font downloaded from:
https://www.fontspace.com/suboleya-font-f69387

Game Background music ("rolla_costa.mp3") downloaded from:
https://www.epidemicsound.com/track/k57Jo05GQG/

Game Over sound effect ("game_over.wav") downloaded from:
https://freesound.org/people/EVRetro/sounds/533034/

Collect Book sound effect ("collect_books.wav") downloaded from:
https://freesound.org/people/jivatma07/sounds/173858/

Collect Obstacle sound effect ("negative-beeps.wav") downloaded from:
https://freesound.org/people/themusicalnomad/sounds/253886/

Movement sound effect ("movement.mp3") downloaded from:
https://freesound.org/people/Raclure/sounds/483602/

Loading bar and Loading bar Background downloaded from :
https://github.com/harsitbaral/LoadingBarPyGame

Game over background image ("no_signal.jpg") downloaded from:
https://www.google.com/search?q=no+signal+colours&tbm=isch&ved=2ahUKEwiTg8mI2u32AhXDQ2wGHcWFDtYQ2-cCegQIABAA&oq=no+signal+colour&gs_lcp=CgNpbWcQARgAMgUIABCABDIFCAAQgAQyBggAEAUQHjoHCCMQ7wMQJzoGCAAQCBAeOggIABCABBCxAzoICAAQsQMQgwE6BwgAELEDEEM6BAgAEEM6BAgAEAM6CwgAEIAEELEDEIMBOgYIABAKEBhQuAtYzitggjFoBHAAeACAAUWIAeQIkgECMjGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=PztEYtPnMMOHseMPxYu6sA0&bih=904&biw=1920#imgrc=Tz9V3zmmMqUQ4M

Login background image ("NUS.jpg") downloaded from:
https://wiki.nus.edu.sg/display/cit/NUS+images+for+Zoom+Virtual+Background
