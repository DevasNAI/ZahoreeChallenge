# Base image
FROM ubuntu:20.04

# Install SSH server (replace with your preferred SSH server)
RUN apt-get update && apt-get install -y openssh-server
RUN apt-get install nano


RUN apt-get -qq update && apt-get -qq -y install curl bzip2 \
    && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -bfp /usr/local \
    && rm -rf /tmp/miniconda.sh \
    && conda install -y python=3 \
    && conda update conda \
    && apt-get -qq -y remove curl bzip2 \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    && conda clean --all --yes

ENV PATH /opt/conda/bin:$PATH

RUN apt-get install -y vnc

# Install Miniconda3 (adjust version and installation path if needed)
#RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh
#RUN bash miniconda.sh -b -p /opt/miniconda3
#ENV PATH="/opt/miniconda3/bin:$PATH"

# Create a new conda environment
#RUN conda create -n spotify -c anaconda -c conda-forge python=3.10
COPY environment.yml .
RUN conda env create -f environment.yml

RUN conda init

# Activate the environment
#ENV CONDA_DEFAULT_ENV spotify
#RUN conda activate spotify

# Install packages from requirements.yml
#COPY requirements.yml .
#RUN conda install --file requirements.yml

# Create a startup script
#RUN mkdir -p /etc/rc.local.d
#COPY start-ssh.sh /etc/rc.local.d/start-ssh.sh


# Expose SSH port (adjust if needed)
#EXPOSE 22

# Set command to run (replace with your desired command)
CMD ["/bin/bash"]