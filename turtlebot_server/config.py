import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

class Config:
    TURTLEBOT_SERVER_PORT = int(os.getenv('TURTLEBOT_SERVER_PORT', 5000))
    TURTLEBOT_SERVER_HOST = os.getenv('TURTLEBOT_SERVER_HOST', '172.30.1.90')
    SSH_USER = os.getenv('SSH_USER', 'ubuntu')
    SSH_PASSWORD = os.getenv('SSH_PASSWORD')  # 수정된 부분
    SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), 'scripts')

config = Config()


