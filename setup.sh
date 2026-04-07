#!/bin/bash
apt-get update
apt-get install -y gcc g++ make python3-dev libffi-dev
pip install --upgrade pip
pip install curl_cffi==0.5.10
