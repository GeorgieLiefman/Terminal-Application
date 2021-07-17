#!/bin/bash

    python3 -m ensurepip --upgrade
    pip3 install virtualenv 
    virtualenv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

