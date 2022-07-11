#!/bin/bash
python2 -m pip install argparse
python2 -m pip install requests
chmod +x gopherus.py
ln -sf $(pwd)/gopherus.py /usr/local/bin/gopherus
