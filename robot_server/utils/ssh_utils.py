import subprocess

def execute_ssh_command(ip, command):
    ssh_command = f"ssh {ip} '{command}'"
    subprocess.Popen(ssh_command, shell=True)

def execute_ros_command(ip, command):
    ssh_command = f"ssh {ip} 'bash -c \"{command}\"'"
    subprocess.Popen(ssh_command, shell=True)
