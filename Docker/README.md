# Docker Image

I will upload the Docker Image to Docker Hub once I finish the implementation, I will first use an Ubuntu 20.04 image with Python 10 and conda, where I will also try to provide the visualization of data.

In case that I do not upload the Image, I will upload the Dockerfile for compilation.


Depending on the device you are using, you can use the following code to create the Docker container.

For windows

```
docker run -p 6080:80 -p 6022:22 -p 8002:8002 -p 7042:7042 -p 5900:5900 -e VNC_PASSWORD=zahoree -p 8042:8042 -e USER=zahoree -e PASSWORD=zahoree -v /dev/shm:/dev/shm -v "e/Programasyarchivos/Archivos_escolares/Repositorios Github/ZahoreeChallenge/workspace":/home/zahoree/workspace --name zahoreechallenge devasnai/challenges:vnc-ubuntu-conda /startup.sh

```



docker run -p 6080:80 -p 6022:22 -p 8002:8002 -p 7042:7042 -p 5900:5900 -e VNC_PASSWORD=zahoree -p 8042:8042 -v /dev/shm:/dev/shm -v "e/Programasyarchivos/Archivos_escolares/Repositorios Github/ZahoreeChallenge/workspace":/home/zahoree/workspace --name zahoreechallenge devasnai/challenges:vnc-ubuntu-conda /startup.sh

https://medium.com/@potatowagon/how-to-use-gui-apps-in-linux-docker-container-from-windows-host-485d3e1c64a3

For Linux

For the workspace path you should add the path where you have this repository installed preferably.
```
docker run -p 6080:80 -p 6022:22 -p 8002:8002 -p 7042:7042 -p 5900:5900 -e VNC_PASSWORD=zahoree -p 8042:8042 -e USER=zahoree -e PASSWORD=zahoree -v /dev/shm:/dev/shm -v "c/YOURDIRECTORY/workspace":/home/zahoree/workspace --name zahoreechallenge1 dorowu/ubuntu-desktop-lxde-vnc:focal /startup.sh
```

No Dockerfile will be provided, I will upload the Docker image to Docker Hub with everything installed just so you can mount the workspace and run everything.


----------
TO BE DELETED INFO
remember to add the bashrc file
cp --backup=t /etc/skel/.bashrc ~
export PATH="/home/username/miniconda/bin:$PATH"
----------



https://community.anaconda.cloud/t/jsondecodeerror-for-many-conda-commands/60397/3