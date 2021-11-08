# HuggingText

**HuggingText** is a simple Python API for classifying and analysing sentiment in text. This microservice template depends on the PyPi package `germansentiment` at the backend to detect sentiment in German texts. The `germansentiment`itself is build on top of BERT architecture open sourced by Huggingface. 

For more detailed read please visit [germansentiment](https://pypi.org/project/germansentiment/) and [BERT HuggingFace](https://huggingface.co/transformers/model_doc/bert.html)     

### Supported Language(s):

At the moment **HuggingText** support only German texts

### Getting started

Please visit and download the Docker for your preferred operating system at [Linux, MacOS, Windows](https://docs.docker.com/get-started/)

### Project setup

![HuggingText directory tree](./imgs/tree.png)

The `germansentiment` model/inference code is stored at `sentimentmodel.py` and the web api code is under `app.py`.

In addition, the project has api test module `test.py`, `Dockerfile` which include commands to build and run the container and a `requirements.txt` file to setup the virtual environment.

### Build and Run Docker Container

```sh

git clone https://github.com/Saran-nns/huggingtext.git

cd huggingtext

sh run.sh

```

In case you would like to build container manually,

```sh

docker build -f Dockerfile -t huggingtext:v0.1.0 .

```
and to run the container,

```sh

docker run -p 8000:5000 -v ~/huggingtext/:/root/huggingtext -ti huggingtext:v0.1.0 /bin/bash -c "cd /src && source activate huggingtext && python app.py" 

``` 
### ENDPOINT

The Flask application has both `GET` and `POST` methods defined at `/`.

### TODO:

To deploy the containerized app to GCP,
  - Cloud Build and Container Registry
  - Cloud Run
