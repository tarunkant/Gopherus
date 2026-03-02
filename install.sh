#!/bin/bash
sed "1s|.*|#!$(which python2)|" gopherus.py > tmp && mv tmp gopherus.py
python2 -m pip install argparse
python2 -m pip install requests
chmod +x gopherus.py
ln -sf $(pwd)/gopherus.py /usr/local/bin/gopherus
