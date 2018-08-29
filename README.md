# VR Bike Realtime Server
This module is a part of [VR-Bike-Multiplayer](https://github.com/maxoja/kmitl-vr-bike) where you can find more details there.
###### latest update : 29 Aug 2018

To configure connection/calculation/debugging details, edit constant values within “config.py”
——————————————————————————————

The server interprets each incoming line as a command

to start the game, send the following line
“‘start’,\n”

to reset the game
“‘reset’,\n”

to set bike wheel frequency 5.2hz for player 0
“‘setFrequency’, 5.2, 0”
