#!/bin/bash

echo "Inside shell script!!"
source /home/adminuser/venv/bin/activate
quarto render $1 --output $2
