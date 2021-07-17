#!/bin/bash
if [[ -x "$(command -v python)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python src/main.py
    else
        echo "You don't have the correct verion of python installed!" >&2
    fi 
else
    echo "Error: This program runs on Python, but it looks like Python is not installed. To install Python, check out https://installpython3.com" >&2
fi
