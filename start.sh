#!/bin/bash
tmux new -d -s helperbot
tmux send -t helperbot "python3 main.py" ENTER
exit 0
