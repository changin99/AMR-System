from flask import request, jsonify
import subprocess
import os
from config import config

robots = {
    "robot1": "192.168.1.2",
    "robot2": "192.168.1.3"
}

def list_robots():
    return jsonify(robots)

def handle_send_command():
    data = request.get_json()
    robot_ip = data['robot_ip']
    command = data['command']
    script_path = os.path.join(config.SCRIPTS_DIR, f"{command}_script.sh")
    ssh_command = f"ssh {config.SSH_USER}@{robot_ip} 'bash -s' < {script_path}"
    subprocess.Popen(ssh_command, shell=True)
    return "Command sent"

def handle_send_velocity():
    data = request.get_json()
    robot_ip = data['robot_ip']
    velocity = data['velocity']
    ssh_command = (
        f"ssh {config.SSH_USER}@{robot_ip} "
        f"'bash -c \"rostopic pub -r 10 /cmd_vel geometry_msgs/Twist "
        f"\\\"{{linear: {{x: {velocity['linear']}, y: 0, z: 0}}, angular: {{x: 0, y: 0, z: {velocity['angular']}}}}}\\\"\"'"
    )
    subprocess.Popen(ssh_command, shell=True)
    return "Velocity sent"
