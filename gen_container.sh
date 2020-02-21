#!/bin/bash

FILE1=$1
FILE2=$2

apt-get update && apt-get install -y git
git clone https://github.com/columbustech/mapfn-test.git
cp $FILE1 mapfn-test/src/foo/process.py
cp $FILE2 mapfn-test/requirements.txt

(cd mapfn-test && docker build -t mapfn-test .)
