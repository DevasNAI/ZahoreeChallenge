#   Dockerfile image (Fixed)


You may be able to have everything installed in the docker image, thus could potentially run the python program with the data analysis.

Go to the Docker Directory inside this container.
```
cd ZahoreeChallenge/Docker
```

Run this command to build the Docker image
```
docker build -t devasnai/challenges:song-recommender -f Dockerfile .
```

**Preferably run this repository on Linux**
If you are on linux, run this command to allow the externa windows on the terminal you will be working on. This is a countermeassure in case it doesn't show up, run this then create the container or access to it through bash.
```
sudo xhost +
```

Run the following code to create the container, you should change your the -v parameter to your own directory as the examples follow:

**Template execution**
docker run -ti -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix -e USER=zahoree -e PASSWORD=zahoree -v /dev/shm:/dev/shm -v ${YOUR DIRECTORY}:/home/zahoree/workspace --name song_recommender3 -it devasnai/challenges:song-recommender bash

**Windows  Example**
```
docker run -ti -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix -e USER=zahoree -e PASSWORD=zahoree -v /dev/shm:/dev/shm -v "e/Programasyarchivos/Archivos_escolares/Repositorios Github/ZahoreeChallenge/workspace":/home/zahoree/workspace --name song_recommender1 -it devasnai/challenges:song-recommender bash
```

**Linux Example**
docker run -ti -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix -e USER=zahoree -e PASSWORD=zahoree -v /dev/shm:/dev/shm -v /home/andy/Desktop/ZahoreeChallenge/workspace:/home/zahoree/workspace --name song_recommender1 -it devasnai/challenges:song-recommender bash



To start the container 
``` 
docker start song_recommender1
```

To run in terminal
```
docker exec -it song_recommender1 bash
```
Once you are inside the container, you may continue with the instructions at the [main page README](https://github.com/DevasNAI/ZahoreeChallenge/) to run the program.
You may also attach a shell on Visual Studio if you have the Docker extension.

### Known Issues
I have Windows 10 with WSL2, but I have problems because of optimization issues of WSL on Windows 10, I cannot test on Windows 11 but this version of Windows is suppoused to already have WSL 2 enabled and fully optimized, so it should work without a problem. I tested it on Ubuntu and if you follow the instructions for the Dockerfile Image, it should work without any problem.


# Docker Image No-VNC (Still on fixing)

The Docker Image is located at [my docker repository](https://hub.docker.com/repository/docker/devasnai/challenges/general) at Docker Hub, it is not stable as of now, I will try to change with with a more lighter Docker Image which you may build with a Dockerfile, the conda file is already made so there should'nt be more problem.


## Installation
Depending on the device you are using, you can use the following commands to create the container

For the workspace path you should add the path where you have this repository installed preferably.
```
docker run -p 6080:80 -p 6022:22 -p 8002:8002 -p 7042:7042 -p 5900:5900 -e VNC_PASSWORD=zahoree -p 8042:8042 -e USER=zahoree -e PASSWORD=zahoree -v /dev/shm:/dev/shm -v "c/YOURDIRECTORY/workspace":/home/zahoree/workspace --name zahoreechallenge1 dorowu/ubuntu-desktop-lxde-vnc:focal /startup.sh
```
Ex.
```
docker run -p 6080:80 -p 6022:22 -p 8002:8002 -p 7042:7042 -p 5900:5900 -e VNC_PASSWORD=zahoree -p 8042:8042 -e USER=zahoree -e PASSWORD=zahoree -v /dev/shm:/dev/shm -v "e/Programasyarchivos/Archivos_escolares/Repositorios Github/ZahoreeChallenge/workspace":/home/zahoree/workspace --name zahoreechallenge devasnai/challenges:vnc-ubuntu-conda /startup.sh
```
