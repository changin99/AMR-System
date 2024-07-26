from flask import request, jsonify
import subprocess
import os
from config import config
import logging

# 로깅 설정
logging.basicConfig(level=logging.DEBUG)

def list_robots():
    return jsonify([])

def setup_robot(robot_ip):
    try:
        # 스크립트 파일 업로드
        local_script_path = '/home/changin/Desktop/AMR-System/turtlebot_server/scripts/common_script.sh'
        scp_command = f"sshpass -p {config.SSH_PASSWORD} scp {local_script_path} {config.SSH_USER}@{robot_ip}:/home/ubuntu/common_script.sh"
        logging.debug(f"Uploading script with command: {scp_command}")
        subprocess.run(scp_command, shell=True, check=True)

        # 필요한 패키지 설치 및 스크립트 권한 설정
        ssh_commands = [
            f"sshpass -p {config.SSH_PASSWORD} ssh {config.SSH_USER}@{robot_ip} 'sudo apt-get update && sudo apt-get install -y tmux'",
            f"sshpass -p {config.SSH_PASSWORD} ssh {config.SSH_USER}@{robot_ip} 'chmod +x /home/ubuntu/common_script.sh'"
        ]

        for command in ssh_commands:
            logging.debug(f"Executing SSH command: {command}")
            subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error setting up robot: {e}")
        return jsonify({"error": "Failed to setup robot"}), 500

def handle_register_robot():
    data = request.get_json()
    logging.debug(f"Received registration data: {data}")
    robot_ip = data['ip']
    
    # 로봇 설정 수행
    setup_robot(robot_ip)

    # 로봇 등록 로직 추가 (예: 데이터베이스에 로봇 정보 저장)
    return "Robot registered"

def handle_send_command():
    data = request.get_json()
    logging.debug(f"Received data: {data}")
    robot_ip = data['robot_ip']
    command = data['command']

    # 명령 실행
    ssh_command = f"sshpass -p {config.SSH_PASSWORD} ssh {config.SSH_USER}@{robot_ip} 'bash /home/ubuntu/common_script.sh {command}'"
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
