#!/bin/bash

COMMAND=$1

# tmux 세션이 존재하는지 확인하고, 없으면 새로 생성
tmux has-session -t turtlebot 2>/dev/null

if [ $? != 0 ]; then
  tmux new-session -d -s turtlebot
  tmux send-keys -t turtlebot 'roscore' C-m
  sleep 5
fi

case $COMMAND in
  "bringup")
    tmux new-window -t turtlebot:1
    tmux send-keys -t turtlebot:1 'roslaunch turtlebot3_bringup turtlebot3_robot.launch' C-m
    ;;
  "slam")
    tmux new-window -t turtlebot:2
    tmux send-keys -t turtlebot:2 'export TURTLEBOT3_MODEL=waffle; roslaunch turtlebot3_slam turtlebot3_slam.launch' C-m
    ;;
  "teleop")
    tmux new-window -t turtlebot:3
    tmux send-keys -t turtlebot:3 'export TURTLEBOT3_MODEL=waffle; roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch' C-m
    ;;
  *)
    echo "Unknown command"
    ;;
esac

tmux attach -t turtlebot


