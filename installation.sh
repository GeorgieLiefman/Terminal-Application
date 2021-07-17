#!/bin/bash
echo "Can I please install venv on your device and the necessary modules to run my application? If you agree please enter yes as the first argument."  
if [[ $1 == "yes" ]]
    then
        python3 -m ensurepip --upgrade
        pip3 install virtualenv 
        virtualenv venv
        source venv/bin/activate
        pip3 install -r requirements.txt
fi

