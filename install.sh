#!/bin/bash

pip3 install -r requirements.txt
chmod +x gopherus3.py
sudo ln -sf $(pwd)/gopherus3.py /usr/local/bin/gopherus3
echo "Gopherus3 installed"
