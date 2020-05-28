from dotenv import load_dotenv
import os

env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)

from app import create_app

app = create_app(os.environ.get('APP_MODE'))
if __name__ == '__main__':
    app.run()
