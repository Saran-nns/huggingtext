docker build -f Dockerfile -t huggingtext:v0.1.0 .

docker run -p 7000:5000 -v ~/huggingtext/:/root/huggingtext -ti huggingtext:v0.1.0 /bin/bash -c "cd /src && source activate huggingtext && python app.py"