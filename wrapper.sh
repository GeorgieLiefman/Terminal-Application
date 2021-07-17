#!/bin/bash
echo "My program relies on virtual environments and the 3rd party module (Cowsay 4.0) to run. As such, if you do not have either of these installed in your device can I please run a script to install them? If you agree please enter 'yes' as the first argument."
echo ""
echo "If you've just installed venv and the module or already had them installed and want to run the application please enter 'run' as the second argument."
echo ""
echo "I am running a script to check you have the correct installation of Python to run the application."
sh environment.sh

if [[ $1 == "yes" ]]
    then
        sh installation.sh
fi

if [[ $2 == "run" ]]
    then
        python3 main.py
fi
