from flask import Blueprint
from controllers.robot_controller import list_robots, handle_send_command, handle_send_velocity

robot_bp = Blueprint('robot', __name__)

@robot_bp.route('/robots', methods=['GET'])
def robots_route():
    return list_robots()

@robot_bp.route('/send_command', methods=['POST'])
def send_command_route():
    return handle_send_command()

@robot_bp.route('/send_velocity', methods=['POST'])
def send_velocity_route():
    return handle_send_velocity()
