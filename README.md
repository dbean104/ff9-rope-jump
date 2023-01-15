# ff9-rope-jump

## Introduction
This repository provides a python script to enable players to achieve the 'Hail to the King' trophy on the rope jump game in Final Fantasy IX on the PS4 (and probably PS5 too, although it has not been tested there).

The script **rope.py** uses an algorithm taken from [septomor](https://github.com/septomor/FF9-Jump-Rope-Script), who originally wrote a script to do the same job using the AutoHotKey functionality in Windows.

Re-implementing some of this algorithm in Python allows Mac users to take advantage of it.

## Pre-Requisites
To use this script you will need the following:
1. A PC or Mac with the following installed:
    1. Python 3 - available [here](https://www.python.org/downloads/)
    2. The pynput plugin (to be installed using pip - instructions [here](https://docs.python.org/3/installing/index.html))
    3. The PlayStation Remote Play application - available [here](https://remoteplay.dl.playstation.net/remoteplay/lang/en/)

2. A PS4 (or PS5) with Final Fantasy IX

3. An internet connection

#### Recommended
For best results, the PC/Mac and the PlayStation should be connected to your internet router via Ethernet cable rather than Wi-Fi.

## Getting the Trophy
1. Copy the **rope.py** folder in this repository to your local PC/Mac, and open a terminal window ready to run the Python script
2. On the PlayStation, start a new game of Final Fantasy IX and get to the stage in Disc 1 where Vivi arrives in Alexandria and is ready to play the rope jump game. Position Vivi next to the game so that an exclamation mark appears above his head.
> Note that the rope jump game is also available in the chapel in Alexandra on Disc 4. This script should work here in the same way, but has not been tested
3. Use Remote Play to allow your PC/Mac to take control of the PlayStation
4. On your PC/Mac, switch to a terminal window and execute the script by typing the command ```python3 rope.py```.
5. Within the allowed delay (default 1 second) switch from your terminal window to the Remote Play window so that the key strokes from the script take effect in the Remote Play window
6. If you are too slow, or the rope jump game ends prematurely, switch back to the terminal window and stop the script using ```Ctrl+c```. You can then reset Vivi in the Remote Play window before attempting to run the script again.

> **For Mac Users:** The first time you run the script, you will probably get a warning to say that 'Terminal' is not authourised to send key strokes.
> To use this script, you will need to temporarily grant the Terminal this permission. To do so, go to Settings -> Privacy & Security -> Accessibility and enable Terminal. You will be prompted to give the administrator password.
> Once you have this trophy, you can revoke this permission.

## Troubleshooting
The **rope.py** script available here uses constants that worked for me when running on my setup (Mac Mini M1 connected via Ethernet, PS4 connected via Ethernet). It is possible that the same values will not work for you. However, making a few tweaks to the code and a bit of trial and error should help.

The first value to investigate is the latency - this is the delay built into the code for the first jump to try and account for the latency between the script sending the command and it reaching the PlayStation.
```python
    latency = 0.761
```

If you are finding that the game is ending around the same point each time, then try tweaking the interval values by a few milliseconds.
```python
    a = 0.667
    b = 0.532
    c = 0.466
    d = 0.434
    e = 0.383
    g = 0.400
    g2 = 0.401
```
