from flask import Flask
from routes.robot_route import robot_bp
from config import config

app = Flask(__name__)
app.register_blueprint(robot_bp, url_prefix='/robot')

if __name__ == '__main__':
    app.run(host=config.TURTLEBOT_SERVER_HOST, port=config.TURTLEBOT_SERVER_PORT)
