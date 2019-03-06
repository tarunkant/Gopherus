#!/bin/bash
pip2 install argparse
pip2 install requests
chmod +x gopherus.py
ln -sf $(pwd)/gopherus.py /usr/local/bin/gopherus
