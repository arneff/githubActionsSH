#!/bin/bash
python learninAuth.py

docker run -e API_KEY=${API_KEY} -e AUTH_TOKEN=${ID_TOKEN} --rm -v $(pwd):/hawk:rw -it  stackhawk/hawkscan:latest
