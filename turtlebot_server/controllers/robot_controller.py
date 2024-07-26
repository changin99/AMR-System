from flask import request, jsonify
import subprocess
import os
from config import config
import logging

# 로깅 설정
logging.basicConfig(level=logging.DEBUG)

def list_robots():
    return jsonify([])

def handle_send_command():
    data = request.get_json()
    logging.debug(f"Received data: {data}")
    robot_ip = data['robot_ip']
    command = data['command']
    script_path = os.path.join(config.SCRIPTS_DIR, f"{command}_script.sh")
    if not os.path.isfile(script_path):
        logging.error(f"Script not found: {script_path}")
        return jsonify({"error": "Script not found"}), 404

    ssh_command = f"sshpass -p {config.SSH_PASSWORD} ssh {config.SSH_USER}@{robot_ip} 'bash -s' < {script_path}"
    logging.debug(f"Executing SSH command: {ssh_command}")
    subprocess.Popen(ssh_command, shell=True)
    return "Command sent"

def handle_send_velocity():
    data = request.get_json()
    logging.debug(f"Received data: {data}")
    robot_ip = data['robot_ip']
    velocity = data['velocity']
    ssh_command = (
        f"sshpass -p {config.SSH_PASSWORD} ssh {config.SSH_USER}@{robot_ip} "
        f"'bash -c \"rostopic pub -r 10 /cmd_vel geometry_msgs/Twist "
        f"\\\"{{linear: {{x: {velocity['linear']}, y: 0, z: 0}}, angular: {{x: 0, y: 0, z: {velocity['angular']}}}}}\\\"\"'"
    )
    logging.debug(f"Executing SSH command: {ssh_command}")
    subprocess.Popen(ssh_command, shell=True)
    return "Velocity sent"

