import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

class Config:
    ROBOT_SERVER_PORT = int(os.getenv('ROBOT_SERVER_PORT', 5000))
    SSH_USER = os.getenv('SSH_USER', 'ubuntu')
    SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), 'scripts')

config = Config()


