#!/usr/bin/env python3
"""
PythonAnywhere Deployment Script for ElderCare Survey
"""

import os
import shutil
import subprocess

def create_pythonanywhere_files():
    """Create files needed for PythonAnywhere deployment"""
    
    # Create wsgi.py file for PythonAnywhere
    wsgi_content = '''import sys
import os

# Add the project directory to the Python path
path = '/home/yourusername/eldercaresurvey'
if path not in sys.path:
    sys.path.append(path)

from app import app as application

if __name__ == "__main__":
    application.run()
'''
    
    with open('wsgi.py', 'w') as f:
        f.write(wsgi_content)
    
    # Create requirements.txt if it doesn't exist
    if not os.path.exists('requirements.txt'):
        requirements_content = '''Flask==2.3.3
Werkzeug==2.3.7
'''
        with open('requirements.txt', 'w') as f:
            f.write(requirements_content)
    
    print("✅ Created PythonAnywhere deployment files:")
    print("   - wsgi.py (update 'yourusername' with your actual username)")
    print("   - requirements.txt")

def create_deployment_guide():
    """Create a PythonAnywhere specific deployment guide"""
    
    guide_content = '''# PythonAnywhere Deployment Guide

## Step 1: Sign up at PythonAnywhere
1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Create a free account
3. Verify your email

## Step 2: Upload your files
1. Go to "Files" tab
2. Create a new directory: `eldercaresurvey`
3. Upload all your files to this directory

## Step 3: Create a web app
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Flask" and "Python 3.9"
4. Set the path to: `/home/yourusername/eldercaresurvey`
5. Set the WSGI file to: `/home/yourusername/eldercaresurvey/wsgi.py`

## Step 4: Install dependencies
1. Go to "Consoles" tab
2. Start a new Bash console
3. Run: `pip install -r requirements.txt`

## Step 5: Configure the app
1. Edit the WSGI file to match your username
2. Reload the web app
3. Your survey will be live at: `https://yourusername.pythonanywhere.com`

## Benefits of PythonAnywhere:
✅ Free forever (no time limits)
✅ No sleep after inactivity
✅ Reliable and stable
✅ Easy to manage
✅ Good for Flask apps
'''
    
    with open('PYTHONANYWHERE_GUIDE.md', 'w') as f:
        f.write(guide_content)
    
    print("✅ Created PythonAnywhere deployment guide: PYTHONANYWHERE_GUIDE.md")

if __name__ == "__main__":
    print("🚀 Creating PythonAnywhere deployment files...")
    create_pythonanywhere_files()
    create_deployment_guide()
    print("\n📋 Next steps:")
    print("1. Sign up at pythonanywhere.com")
    print("2. Follow the guide in PYTHONANYWHERE_GUIDE.md")
    print("3. Upload your files and configure the web app")
    print("\n🌐 Your survey will be live at: https://yourusername.pythonanywhere.com") 