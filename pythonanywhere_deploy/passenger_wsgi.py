import sys
import os

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Import the Flask app
from app import app as application

# For debugging
if __name__ == '__main__':
    application.run()
