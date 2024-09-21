# Spotify Recomendations - Zahoree Challenge

This repository includes an implementation of a script that brings song recomendations to users based on their favorite songs.


This repository has a playlist and music recommendation system which suggests playlist and songs using the vector based comparison method of cosine similarity. Whenever you bring new playlists, the recommendation changes.


# Setting up environment
If you want to use this repository, you must get the Docker Image and create a container, everything will run as it should when you create the container by following the instructions found in [Docker](github.com/DevasNAI/ZahoreeChallenge/Docker/)




## Run script
You need to initialize conda and restart the shell.
```
conda init
```
Once restarted, follow the next commands:

```
conda activate spotify
cd hoome/zahoree/workspace/build
```
To run the script:
```
python3 d_gui.py
```

## Docker Container access (with image)
Once you have your docker system running, you may access to it throuch VNC Viewer or other means, just follow the following instructions.

-- I have been struggling to get the Docker image running as it should, so I exported the conda environment to be able to run it if you have Anaconda or miniconda installed.

To install the conda environment run:
```
conda env create -f environment.yml
```

To run the program, go to the build directory and run:
```
cd ZahoreeChallenge/workspace/build
python3 d_gui.py
```

## Solution UI
If everything ran as expected, you should be able to visualize the following image.
<p align="center">
<img src="https://github.com/DevasNAI/ZahoreeChallenge/blob/main/images/solution.png" width="50%" height="50%" title= "Spotify Recommendation" alt="recom">
</p>

You can select the user playlist and when you click the select button, you will see a playlist recommendation and a new playlist of 15 songs.


### VNC Viewer
Open VNC Viewer, then write the following:
```
localhost:5900
```
You will be prompted a pop-up alert, accept it and proceed to write your VNC Password.
<p align="center">
<img src="https://github.com/DevasNAI/ZahoreeChallenge/blob/main/images/vncalert.png" width="50%" height="50%" title= "VNC Viewer" alt="DFD">
</p>


Once entered, you can open a terminal by clicking the icon on the down left corner and select System Tools as shown at the image.

<p align="center">
<img src="https://github.com/DevasNAI/ZahoreeChallenge/blob/main/images/LXTerminal.png" width="50%" height="50%" title= "Find LX Terminal" alt="LX">
</p>

### novnc
Once the container has started, go to https:\\localhost:6080

You may be prompted to put your VNC Password



## File system
- Docker
- workspace
    - build


The dataset was provided by Zahoree

