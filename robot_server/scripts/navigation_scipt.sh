#!/bin/bash
# roscore를 실행
gnome-terminal -- bash -c "roscore; exec bash"

# roscore가 시작될 때까지 대기
sleep 5

# 터미널 1: bringup 실행
gnome-terminal -- bash -c "roslaunch turtlebot3_bringup turtlebot3_robot.launch; exec bash"

# 터미널 2: 네비게이션 실행
gnome-terminal -- bash -c "export TURTLEBOT3_MODEL=waffle; roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml; exec bash"
