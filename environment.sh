#!/bin/bash
if [[ -x "$(command -v python)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python"* ]]
    then
        echo ""
        echo "You have the correct version of python isntalled to run this program!"
    else
        echo ""
        echo "You don't have the correct verion of python installed! To install the correct version of Python, please checkout https://www.python.org/downloads/" >&2
    fi 
else
    echo ""
    echo "Error: This program runs on Python, but it looks like Python is not installed. To install Python, please check out https://installpython3.com" >&2
fi
