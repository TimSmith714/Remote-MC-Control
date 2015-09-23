Remote-MC-Control
=================

Uses Python to control the mouse and keyboard remote for Minecraft but should be very easy to rework for other games

Requirements

pywin32 from Sourceforge and this must match the version of Python on your computer
For reference, I've used 32bit Python 3.4 (even though I'm using 64bit Windows)


You will need to download the PyUserInput files from  https://github.com/SavinaRoja/PyUserInput into the folder with the server code in and run whatever dependancies there are for your OS. I've developed this on Windows and it involved pywin32 and pyHook. I'm /hoping/ that this will run on other OSes so long as the appropriate dependancies are satisfied

At the moment the IP address of the server (machine running the game) is fixed to 192.168.2.5 It's easy to change but I may add a question when you start. Would welcome thoughts on that as compared to the hassle of entering an IP address every time you want to play, the hassle of editing the Python file seems pretty small

To use. Run the server program and then set Minecraft to run in FULLSCREEN mode. This is VERY important. Due to the way the mouse behaves in the game (returns to 'centre' every time movement stops) the view move commands work by calculating a percentage of the screen size not the window size. The maths goes very weird if Minecraft isn't running full screen and you'll find the view moving up or down as well as left and right. 
I'd also strongly recommend only using this in Creative Mode - at least for the moment. As there's not crouch toggle yet (see below) it's far too easy to fall off ledges and hurt/kill yourself

Run the client program on the other computer and use the following commands


Keyboard commands

| Key | Command |
|----|--------|
|w  | move foward |
|s | move backward|
|a | side step left|
|d | side step right|
| | |
|u | move view up |
|j | move view down|
|h | turn view left|
|k | turn view right|
| | |
|t | toggle flying mode (double-tap space bar)|
|g | move up or jump (space bar)|
|b | move down or crouch for a moment (left shift)|

I've not added the command to enter the inventory yet. The mouse reverts to a 'normal' windows mode when you do so I've got to get my head round how the controls work at that point.

TODO
Crouch - might be a good idea to toggle this key as it stops you falling off ledges - especially important given that this is designed to work with assistive technolog-es

Important Credits
I learnt how to create the two programs and have them talk to each other with this very useful tutorial at http://ilab.cs.byu.edu/python/socket/echoserver.html from  Brigham Young University
It wouldn't have happened so quickly without the PyUserInput project https://github.com/SavinaRoja/PyUserInput
I used Pycharm http://www.jetbrains.com/pycharm/ as my IDE for this project. 
I'm merely standing on the shoulders of giants

Icons from
http://www.smashingmagazine.com/2015/03/freebie-swifticons-icon-set/

