# Bert model requires CUDA for faster inference
FROM nvidia/cuda:11.4.2-cudnn8-runtime-ubuntu20.04

# Set default PATH variable to virtual environment bin/ 
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

# Update and install package downlaoder and python 3
RUN apt update \
    && apt install -y wget python3-dev

# Dowload and install miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir  root/.conda \
    && sh Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

# Create virtual env
RUN conda create -y -n huggingtext python==3.8

# Copy the files to src
COPY . src/

# Activate the virtual environment and install the requirements
RUN /bin/bash -c "cd src \
    && source activate huggingtext \
    && pip install -r requirements.txt" 