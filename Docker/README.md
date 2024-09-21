# Docker Image

The Docker Image is located at [my docker repository](https://hub.docker.com/repository/docker/devasnai/challenges/general) at Docker Hub, it is not stable as of now, I will try to change with with a more lighter Docker Image which you may build with a Dockerfile, the conda file is already made so there should'nt be more problem.


#   For using the no-VNC Ubuntu Image
Depending on the device you are using, you can use the following commands to create the container

For the workspace path you should add the path where you have this repository installed preferably.
```
docker run -p 6080:80 -p 6022:22 -p 8002:8002 -p 7042:7042 -p 5900:5900 -e VNC_PASSWORD=zahoree -p 8042:8042 -e USER=zahoree -e PASSWORD=zahoree -v /dev/shm:/dev/shm -v "c/YOURDIRECTORY/workspace":/home/zahoree/workspace --name zahoreechallenge1 dorowu/ubuntu-desktop-lxde-vnc:focal /startup.sh
```
Ex.
```
docker run -p 6080:80 -p 6022:22 -p 8002:8002 -p 7042:7042 -p 5900:5900 -e VNC_PASSWORD=zahoree -p 8042:8042 -e USER=zahoree -e PASSWORD=zahoree -v /dev/shm:/dev/shm -v "e/Programasyarchivos/Archivos_escolares/Repositorios Github/ZahoreeChallenge/workspace":/home/zahoree/workspace --name zahoreechallenge devasnai/challenges:vnc-ubuntu-conda /startup.sh
```

#   Dockerfile image


You may be able to have everything installed in the docker image, thus could potentially run the python program with the data analysis.

Run this to build the Docker image
```
docker build -t devasnai/challenges:song-recommender -f Dockerfile .
```

Run this to create the container
```
docker run -ti -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix -e USER=zahoree -e PASSWORD=zahoree -v /dev/shm:/dev/shm -v "e/Programasyarchivos/Archivos_escolares/Repositorios Github/ZahoreeChallenge/workspace":/home/zahoree/workspace --name song_recommender3 -it devasnai/challenges:song-recommender bash
```

**Preferably run this repository on Linux**
If you are on linux, run this to display windows on the terminal you will be working on:
```
sudo xhost +
```

To start the container
``` 
docker start song_recommender
```

To run in terminal
```
docker exec -it song_recommender bash
```

I have Windows 10 with WSL2 but I cannot prove that it works with a terminal because of trouble with my computer but the implementation must work on a Linux Debian system with the provided instructions.

You may also attach a shell on Visual Studio if you have the Docker extension.