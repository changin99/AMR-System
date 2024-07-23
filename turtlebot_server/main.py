from flask import Flask
from routes.robot_route import robot_bp
from config import config

app = Flask(__name__)
app.register_blueprint(robot_bp, url_prefix='/robot')

if __name__ == '__main__':
    app.run(host='172.30.1.90', port=config.ROBOT_SERVER_PORT)
