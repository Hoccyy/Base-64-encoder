#!/bin/bash

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

python3 -m venv venv
source venv/bin/activate
python main.py

deactivate